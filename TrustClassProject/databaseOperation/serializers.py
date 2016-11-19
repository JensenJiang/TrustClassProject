from django.contrib.auth.models import User
from rest_framework import serializers
from .models import TCUser, School

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
        extra_kwargs = {'username': {'read_only': True}}

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('name', 'pk')

class SchoolUpdateSerializer(serializers.Serializer):
    pk = serializers.IntegerField()

class TCUserProfileSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    school = SchoolSerializer()
    class Meta:
        model = TCUser
        fields = ('nickname', 'school', 'user')
 
class TCUserProfileUpdateSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    school = SchoolUpdateSerializer()

    class Meta:
        model = TCUser
        fields = ('nickname', 'school', 'user')
    
    def update(self, instance, validated_data):
        self.get_fields()['user'].update(instance.user, validated_data.get('user'))
        new_pk = validated_data.get('school').get('pk', instance.school.pk)
        if new_pk != instance.school.pk:
            try:
                instance.school = School.objects.get(pk=new_pk)
            except School.DoesNotExist:
                pass
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.save()
        return instance

class TCUserSerializer(serializers.ModelSerializer):
    pass
