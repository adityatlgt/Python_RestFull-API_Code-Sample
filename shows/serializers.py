from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User
from shows.models import Screens, Bookings


# Serializer for users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']


class ScreensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screens
        fields = ('__all__')


class BookingsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Bookings
        fields = ('__all__') 

class BookingsSerializerPost(serializers.ModelSerializer):
    class Meta: 
        model = Bookings
        fields = ('email','mobile','show_booked')                      