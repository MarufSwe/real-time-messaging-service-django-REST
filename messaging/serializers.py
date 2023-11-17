# from rest_framework import serializers
# from .models import Message
#
#
# class MessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Message
#         fields = ['id', 'sender', 'content', 'timestamp']


# messaging/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()  # UserSerializer for the sender field

    class Meta:
        model = Message
        fields = ['id', 'sender', 'content', 'timestamp']
