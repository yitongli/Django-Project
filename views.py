from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect

monthly_challenges = {
    "january":"not eat meat",
    "february":"walk 20 minutes everyday!!!"
}

# Create your views here.
def monthly_challenges_by_numbers(request,month):
    months_list = list(monthly_challenges.keys())
    if month > len(months_list):
        return HttpResponseNotFound("this month is not supported!")
    forward_month = months_list[month-1]
    #redirect function, convert int month to string month
    return HttpResponseRedirect("/challenges/"+forward_month)


def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("this month is not supported!")
    
