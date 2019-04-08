from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(requests):
	count = User.objects.count()
	return render(requests,'home.html',{
		'count':count
		})

def signup(requests):
	if requests.method == 'POST':
		form = UserCreationForm(requests.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(requests,'registration/signup.html',{
		'form':form
		})