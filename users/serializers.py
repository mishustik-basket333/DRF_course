from random import random
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор пользователя"""

    # def validate_password(self, value: str) -> str:
    #     """ Создание пароля"""
    #     return make_password(value)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        instance.is_active = True

        if password is not None:
            instance.set_password(password)
        else:
            word_list = list("Password12345")
            password = "".join(random.sample(word_list, len(word_list)))
            instance.set_password(password)
        instance.save()

        return instance

    class Meta:
        model = User
        fields = '__all__'
