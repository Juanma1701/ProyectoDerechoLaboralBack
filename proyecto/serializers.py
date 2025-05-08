from rest_framework import serializers
from .models import Users
from rest_framework.routers import DefaultRouter

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'