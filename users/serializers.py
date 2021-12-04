#rest framework imports 

from rest_framework import serializers

"""
   This is our serializer class that will be in use
"""
class UserSerializer(serializers.Serializer):
    index = serializers.IntegerField()
    isActive = serializers.BooleanField()
    picture = serializers.CharField()
    age = serializers.CharField()
    gender = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    address = serializers.CharField()
    about = serializers.CharField()
    registered = serializers.CharField()