from django.contrib.auth.models import User
from rest_framework import serializers

"""
Serializing and deserializing the users instances into representations such as json.
"""


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', ]
