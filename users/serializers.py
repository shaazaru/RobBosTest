from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'f_name', 'l_name')
        extra_kwargs = {
            'password': {'write_only': True}
        }
