from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

def signup_view(request):
	if request.method == 'GET':
		form = UserCreationForm()
	elif request.method== 'POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			user=form.save()
			login(request,user)

			return redirect('/')

	return render(request,'users/signup.html',{'form':form})

def login_view(request):
	if request.method=='POST':
		form=AuthenticationForm(data=request.POST)
		if form.is_valid():
			#log em in
			user=form.get_user()
			login(request,user)
			return redirect('/')
	else:
		form=AuthenticationForm()

	return render(request,'users/login.html',{'form':form})

def logout_view(request):
	logout(request)
	return redirect('/')
