from django.contrib.auth.models import User
from rest_framework import serializers
from .models import TCUser, School

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
        extra_kwargs = {'username': {'read_only': True}}

    def update(self, instance, validated_data):
        instace.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('name',)

class TCUserProfileSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    school = SchoolSerializer()

    class Meta:
        model = TCUser
        fields = ('nickname', 'school', 'user')
    
    def update(self, instance, validated_data):
        print(validated_data)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.save()
        return instance

class TCUserSerializer(serializers.ModelSerializer):
    pass
