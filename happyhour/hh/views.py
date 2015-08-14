from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from forms import UserForm, HappyHourForm

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

def user_login(request):
	context = RequestContext(request)

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/hh/')
			else:
				return HttpResponse("Your Rango account is disabled.")
		else:
			return HttpResponse('Sorry! These credentials are incomplete or not valid.')

	else:
		return render_to_response('user_login.html', {}, context)

@login_required
def user_logout(request):
	logout(request)

	return HttpResponseRedirect('/')

def index(request):
	context = RequestContext(request)
	return render_to_response('index.html', {}, context)

@login_required
def add_hh(request):
	context = RequestContext(request)

	if request.method == 'POST':
		# TODO: pass the user object in here
		form = HappyHourForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			# TODO: show this in the template
			print(form.errors)
	else:
		form = HappyHourForm()

	return render_to_response('add_hh.html', {'form':form}, context)

def bar(request, rest_name):
	return HttpResponse("This is the details for one bar/restaurant happy hour: {}".format(rest_name))

def day(request, day):
	return HttpResponse("These are all the happy hours today: {}".format(day))
