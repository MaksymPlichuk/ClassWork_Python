from rest_framework import serializers
from .models import CustomUser

#вхідний DTO для логіну. write_only=True означає, що поле приймається на вхід, але ніколи не серіалізується назад у відповідь (тобто пароль не потрапить у JSON-відповідь).
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'password',
        ]

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    image = serializers.FileField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'password',
            'confirm_password',
            'first_name',
            'last_name',
            'email',
            'image'
        ]

    # #перевизначаємо метод  при новихх полях треба переписувати тому закоментований
    # def create(self, validated_data): 
    #     # create_user сам викликає set_password() і хешує пароль (PBKDF2/argon2 залежно від settings)
    #                                 #**validated_data - розпакування цього словника 'username': 'user1234' --> username='user1234'
    #     user=CustomUser.objects.create_user(**validated_data)
    #     return user

#вихідний DTO для представлення користувача (без пароля взагалі).
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'image_small',
            'image_medium',
            'image_large'
        ]