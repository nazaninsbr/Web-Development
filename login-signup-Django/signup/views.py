from django.contrib.auth import login, authenticate
# from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from signup.serializers import SignupSerializer
import json
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse

# @login_required
# def home(request):
#     return render(request, 'signup/home.html')
import logging
logger = logging.getLogger(__name__)


@csrf_exempt
def signup(request):
    if request.method == 'GET':
       response_data = {}
       response_data['result'] = 'error'
       response_data['message'] = 'You need to post something'
       return HttpResponse(json.dumps(response_data), content_type="application/json")


    if request.method == 'POST':
        signupdata = JSONParser().parse(request)
        serializer = SignupSerializer(data = signupdata)
        if serializer.is_valid():
            # serializer.save()
            jsonfile = serializer.data
            username = jsonfile["username"]
            password = jsonfile["password"]
            logger.info(username)
            logger.info(password)
            password = make_password(password, '1')
            user = User(username=username, password=password)
            user.save()
            new_token = Token.objects.create(user=user)
            new_token.save()
            request.session["SoCkey"]=new_token.key
            request.session.set_expiry(30000000)
            login(request, user)
            return JsonResponse({"key":new_token.key})
        else:
            return JsonResponse(serializer.errors)
        # username = signupdata.cleaned_data.get('username')
        # raw_password = signupdata.cleaned_data.get('password1')
        # user = authenticate(username=username, password=raw_password)

        # form = Signup(request.POST)
        # if form.is_valid():
        #     form.save()
        #     username = form.cleaned_data.get('username')
        #     raw_password = form.cleaned_data.get('password1')
        #     user = authenticate(username=username, password=raw_password)
        #     login(request, user)
        #     return redirect('home')
    # else:
    #     form = SignUpForm()
    # return render(request, 'signup/signup.html', {'form': form})
