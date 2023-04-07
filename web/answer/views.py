from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.voice_response import VoiceResponse
from user_profile.models import UserProfile

# Create your views here.


@csrf_exempt
def answer(self):
    # obj = UserProfile.objects.get(phone=)
    response = VoiceResponse()
    print(str(self))
    response.say('Hello, and thank you for your call.')
    return HttpResponse(str(response))


def test(self):
    return HttpResponse("Its Fucking Working Bitch!")