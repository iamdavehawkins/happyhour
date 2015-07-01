from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def now(request):
	return HttpResponse("This is the landing page, that shows the happy hours right now")

def bar(request, rest_name):
	return HttpResponse("This is the details for one bar/restaurant happy hour: {}".format(rest_name))

def day(request, day):
	return HttpResponse("These are all the happy hours today: {}".format(day))

