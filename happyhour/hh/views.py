from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from forms import UserForm

# Create your views here.
def register(request):
	context = RequestContext(request)

	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)

		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			registered = True

		else:
			print(user_form.errors)

	else:
		user_form = UserForm()

	return render_to_response('register.html',
	    					  {'user_form': user_form, 'registered': registered},
	                          context)

def now(request):
	return HttpResponse("This is the landing page, that shows the happy hours right now")

def bar(request, rest_name):
	return HttpResponse("This is the details for one bar/restaurant happy hour: {}".format(rest_name))

def day(request, day):
	return HttpResponse("These are all the happy hours today: {}".format(day))
