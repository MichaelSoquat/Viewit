from dataclasses import fields
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model: CustomUser
        ALL_FIELDS = '__all__'