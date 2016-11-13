from rest_framework import serializers
from .models import TCUser

class TCUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TCUser
        fields = ('nickname', 'school')
