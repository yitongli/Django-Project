from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january":"not eat meat",
    "february":"walk 20 minutes everyday!!!"
}

# Create your views here.
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge",args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    #"<li><li>" create month list 
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenges_by_numbers(request,month):
    months_list = list(monthly_challenges.keys())
    if month > len(months_list):
        return HttpResponseNotFound("this month is not supported!")

    forward_month = months_list[month-1]
    #redirect function, convert int month to string month
    redirect_path = reverse("month-challenge",args=[forward_month]) #challenge/month
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>this month is not supported!</h1>")
    
