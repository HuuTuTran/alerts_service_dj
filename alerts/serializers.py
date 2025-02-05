from rest_framework import serializers
from .models import alerts , IAMRoles , IAMUsers
from datetime import datetime
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        return token




class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = alerts
        fields = '__all__'
        # read_only_fields = ["alert_id"]
    def update(self, instance, validated_data):
        validated_data['updated'] = int(datetime.now().timestamp())
        return super().update(instance, validated_data)


class IamUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = IAMUsers
        fields = '__all__'
        read_only_fields = ["username","_id", "created" ]
    def update(self, instance, validated_data):
        validated_data['updated'] = int(datetime.now().timestamp())
        return super().update(instance, validated_data)

class IAMRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = IAMRoles
        fields = '__all__'
        read_only_fields = ["_id"]
    def update(self, instance, validated_data):
        validated_data['updated'] = int(datetime.now().timestamp())
        return super().update(instance, validated_data)