from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from signup.forms import SignUpForm
import json

@login_required 
def home(request):
    return render(request, 'signup/home.html')


def signup(request):
    #if request.method == 'GET':
    #    response_data = {}
    #    response_data['result'] = 'error'
    #    response_data['message'] = 'You need to post something'
    #    return HttpResponse(json.dumps(response_data), content_type="application/json")


    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup/signup.html', {'form': form})