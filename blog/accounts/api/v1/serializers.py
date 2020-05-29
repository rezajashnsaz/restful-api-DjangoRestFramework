from articles.models import Article
from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            ]

    def validate_password(self , value):
        if len(value) < 5:
            raise serializers.ValidationError("طول پسورد باید بیشتر از 5 کاراکتر باشد")
        return value 