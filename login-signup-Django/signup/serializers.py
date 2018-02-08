from rest_framework import  serializers
from django.contrib.auth.models import User

# from signup.models import Signup

class SignupSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=500, allow_blank=True)
    password = serializers.CharField(max_length=30, allow_blank=True)
    # password2 = serializers.CharField(max_length=30, allow_blank=True)
    first_name = serializers.CharField(max_length=30, required=False)
    last_name = serializers.CharField(max_length=30, required=False)
    email = serializers.EmailField(max_length=254, required=True)

    def create(self, validated_data):
        return User.objects.create(**validated_data)
