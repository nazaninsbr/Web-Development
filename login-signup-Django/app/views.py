
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

import logging
logger = logging.getLogger(__name__)

# MAIN PAGE
@csrf_exempt
def index(request):
    c = {}
    c.update(csrf(request))
    logger.error('index')
    # return render(request, 'app/index.html')


class LoginView(views.APIView):

    msgs = {
        'login_success': "User has successfully logged in. User: {0}",
        'login_msg': 'LOGIN_SUCCESSFUL',
        'cannot_login': 'CAN_NOT_LOGIN',
        'combination_invalid': 'COMBINATION_INVALID'
    }

    @csrf_exempt
    def post(self, request):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        # password = make_password(password, '1')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            token = Token.objects.get(user=user)
            token.save()
            request.session['SoCkey']=token.key
            request.session.set_expiry(30000000)
            return Response({
                'token': token.key,
                'status': 'Success',
                'message': self.msgs['login_msg'],
            }, status=status.HTTP_200_OK)

        else:
            logger.info('User attempts to login with credentials and do not exist')
            return Response({
                'status': 'Unauthorized',
                'message': self.msgs['cannot_login']
            }, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        return render(request, 'app/index.html')

# LOGIN PAGE
@csrf_exempt
def login_view(request):
    # if request.user.is_authenticated():
    key = request.session.get("SoCkey")
    if key:
        return HttpResponseRedirect(reverse('app:index'))

    try:
        username = request.POST['username']
        password = request.POST['password']
        # password = make_password(password, '1')
        print(password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            new_token = Token.objects.get(user=user)
            new_token.save()
            request.session['SoCkey']=new_token.key
            request.session.set_expiry(300)
            return HttpResponseRedirect(reverse('app:index'))
        else:
            return render(request, 'app/login.html', {'message': 'Invalid Credential'})
    except:
        return render(request, 'app/login.html', {'message': 'unsuccessful'})

from rest_framework.decorators import api_view

# LOGOUT PAGE
@csrf_exempt
# @login_required(login_url='/app/login')
@api_view(['GET' ])
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        # request.session.clear()
        return Response({
            'message': 'logged out successfully'
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'message': 'failed'
        }, status=status.HTTP_401_UNAUTHORIZED)


# # REST TEST
from django.http import JsonResponse
@csrf_exempt
@login_required(login_url='/app/login')
def json_test(request):
    return JsonResponse({'foo': 'bar'})
