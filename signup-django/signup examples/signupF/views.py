from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from signupF.forms import SignUpForm

@login_required 
def homeF(request):
    return render(request, 'signupF/home.html')


def signupF(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homeF')
    else:
        form = SignUpForm()
    return render(request, 'signupF/signup.html', {'form': form})