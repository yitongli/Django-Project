from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def monthly_challenges_by_numbers(request,month):
    return HttpResponse(month)


def monthly_challenge(request,month):
    challenge_text = None
    if month == 'january':
        challenge_text = "not eat meat"
    elif month == 'february':
        challenge_text = "walk 20 minutes everyday!!!"
    else:
        return HttpResponseNotFound("this month is not supported")
    return HttpResponse(challenge_text)
