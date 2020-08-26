from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.
def register(request):
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.clean_data.get('username')
			messages.success(request, f'{username}, your account has been created successfully!')
			return redirect('/success/')
	else:
		form = UserRegistrationForm()
	return render(request, 'users/register.html', {'form':form})

def success(request):
	return	render(request, 'users/success.html')