from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.voice_response import VoiceResponse
from user_profile.models import UserProfile, AutoDriverLocation, AutoDriver
from django.urls import reverse
from twilio.twiml.messaging_response import Message, MessagingResponse
from langdetect import detect
from math import sin, cos, sqrt, atan2, radians, ceil

# Create your views here.

lang_conversions = {
    'pa': 'pun',
    'en': 'eng',
    'hi': 'hin',
    'kn': 'kan',
}


@csrf_exempt
def get_user(request):
    # Example Incommign Data ['whatsapp', '+919646273060', 'yo wssup', 'Harmanjit Singh']
    arr = str(request.GET['body']).split(":")
    name = arr[3]
    message = arr[2]
    number = arr[1]

    curr_lang = lang_conversions.get(detect(str(message)))

    if curr_lang == None:
        curr_lang = 'eng'

    try:
        usr = UserProfile.objects.get(mobile=str(number))
        new = False
    except:
        new = True
        usr = UserProfile.objects.create(
            mobile=str(number),
            name=str(name),
        )

    resp = {
        'name': usr.name,
        'mob': usr.mobile,
        'verified': usr.verified,
        'lang': curr_lang,
        'new': new,
    }
    return JsonResponse(resp)


@csrf_exempt
def get_location(request):
    #  Example ['31.300819396972656:75.59191131591797:31.2984619140625:75.58817291259766:eng']
    body = str(request.GET['body']).split(":")
    print(body)
    lang = body[4]
    lat1 = radians(float(body[0]))
    lon1 = radians(float(body[1]))
    lat2 = radians(float(body[2]))
    lon2 = radians(float(body[3]))

    print(lang, lat1, lon1, lat2, lon2)

    journey = calcDistance(lat1, lon1, lat2, lon2)
    cost = 10*journey

    drivers = ""
    l = {
        'kan': f"ನಿಮ್ಮ ಪ್ರಯಾಣದ ದೂರವು {ceil(journey)} ಕಿಮೀ ಮತ್ತು ನಿಮ್ಮ ಪ್ರಯಾಣದ ದರವು ರೂ {ceil(cost)}. ನಾವು ನಿಮಗಾಗಿ ನಮ್ಮ ಯಾತ್ರಿ ಬುಕಿಂಗ್ ಅನ್ನು ರಚಿಸಿದ್ದೇವೆ. ಚಾಲಕ ಶೀಘ್ರದಲ್ಲೇ ನಿಮ್ಮನ್ನು ಸಂಪರ್ಕಿಸುತ್ತಾನೆ. ಲಭ್ಯವಿರುವ ಚಾಲಕರ ಪಟ್ಟಿ ಇಲ್ಲಿದೆ:\n",
        "eng": f"Your journey distance is {ceil(journey)} km and the fare price for your trip is Rs {ceil(cost)}. We have created a namma yatri booking for you. A driver will contact you shortly.Here is a list of drivers available:\n",
        "hin": f"आपकी यात्रा की दूरी {ceil(journey)} किमी है और आपकी यात्रा का किराया {ceil(cost)} रुपये है। हमने आपके लिए नम्मा यात्री बुकिंग बनाई है। एक ड्राइवर पार्टनर जल्द ही आपसे संपर्क करेगा। यहाँ उपलब्ध ड्राइवरों की एक सूची है:\n",
        "pun": f"ਤੁਹਾਡੀ ਯਾਤਰਾ ਦੀ ਦੂਰੀ {ceil(journey)} ਕਿਲੋਮੀਟਰ ਹੈ ਅਤੇ ਤੁਹਾਡੀ ਯਾਤਰਾ ਦਾ ਕਿਰਾਇਆ {ceil(cost)} ਰੁਪਏ ਹੈ। ਅਸੀਂ ਤੁਹਾਡੇ ਲਈ ਨਮਾ ਯਾਤਰਾ ਬੁਕਿੰਗ ਬਣਾਈ ਹੈ। ਇੱਕ ਡਰਾਈਵਰ ਤੁਹਾਡੇ ਨਾਲ ਜਲਦੀ ਹੀ ਸੰਪਰਕ ਕਰੇਗਾ। ਇੱਥੇ ਉਪਲਬਧ ਡਰਾਈਵਰਾਂ ਦੀ ਸੂਚੀ ਹੈ:\n"
    }
    drivers += l.get(lang)

    for d2 in AutoDriver.objects.all():
        drivers += f"\nName: {d2.name}\nMobile: {d2.mobile}\nRC: {d2.registeration_number}\n"

    return JsonResponse({
        "msg": drivers,
    })


def calcDistance(lat1, lon1, lat2, lon2):
    # Approximate radius of earth in km
    R = 6373.0

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance


@csrf_exempt
def reply_sms(request):
    print(request.POST)
    # sms_number = str(request.POST['From']).split(":")[1]
    # sms_body = request.POST['Body']
    # host_name = request.POST['ProfileName']
    # print(f"Incomming Message from: {sms_number} \nMessage body: {sms_body}")

    # user = UserProfile.objects.get(mobile=str(sms_number))

    resp = MessagingResponse()
    resp.message(
        body=f'Welcome to Namma Yatri',
    )

    return HttpResponse(str(resp))


@csrf_exempt
def reply_sms_fail(request):
    print(str(request.POST))
    resp = MessagingResponse()
    resp.message(
        body='Sorry unable to reach Namma Yatri Services, Please try after some time. Thank You!'
    )

    return HttpResponse(str(resp))


@csrf_exempt
def answer(request):
    # obj = UserProfile.objects.get(phone=)
    phone_number = request.POST['From']
    print(str(request.POST))
    response = VoiceResponse()
    response.say("Wecome to Namma Yatri ")
    with response.gather(
        num_digits=1,
        action=reverse('book-auto'),
        timeout=10,
    ) as g:
        g.say(
            message="To book an auto press 1, To repeat press 9, to exit press 0 ",
        )
    return HttpResponse(str(response))


@csrf_exempt
def book_auto(request):

    response = VoiceResponse()
    digits = request.POST.get('Digits')
    print(digits)
    if digits == None or int(digits) == 0:
        with response.gather(
            num_digits=0,
            timeout=0,
            action=reverse('hangup-call-server')
        ) as g:
            g.say("Thank you for calling")
        return HttpResponse(str(response))

    if digits == 9 or digits == '9':
        with response.gather(
            num_digits=0,
            timeout=0,
            action=reverse('answer-call-server')
        ) as g:
            g.say("Repeating ")
        return HttpResponse(str(response))

    response.say(
        "Before booking auto please tell us where you are so that we can find auto's near you! Please say your closest location after this beep ")
    response.record(
        play_beep=True,
        max_length=10,
        trim='do-not-trim',
        action=reverse('dummy-url-server')
    )
    return HttpResponse(str(response))


@csrf_exempt
def hangup(request):
    response = VoiceResponse()
    response.hangup()
    return HttpResponse("Its Fucking Working Bitch!")


@csrf_exempt
def test(request):
    response = VoiceResponse()
    response.say('Its Fucking Working Bitch!')
    response.hangup()
    return HttpResponse("Its Fucking Working Bitch!")


@csrf_exempt
def test_data(request):
    print(request.POST)
    return HttpResponse("Its Fucking Working Bitch!")
