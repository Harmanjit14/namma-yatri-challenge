from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.voice_response import VoiceResponse
from user_profile.models import UserProfile
from django.urls import reverse

# Create your views here.


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
            message="To book an auto press 1, to exit press 0           ",
            loop=3,
        )
    return HttpResponse(str(response))


@csrf_exempt
def book_auto(request):
    response = VoiceResponse()
    digits = request.POST.get('Digits')
    if digits == None or int(digits) == 0:
        response.say("Thank you for calling!")
        response.hangup()
        return

    response.say(
        "Before booking auto please tell us where you are so that we can find auto's near you! ")

    with response.gather(
        input='speech',
        timeout=30,
    ) as g:
        g.say(
            message=' Please wait '
        )
    return HttpResponse(str(response))


def test(request):
    return HttpResponse("Its Fucking Working Bitch!")
