from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели пользователя (User).
    Этот сериализатор исключает поле пароля.
    """
    class Meta:
        model = User
        exclude = ('password',)



class RegisterSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации нового пользователя.

    Этот сериализатор исключает поле пароля из вывода, так как оно будет
    сгенерировано автоматически методом create.

    Поля password и password2 валидируются, чтобы убедиться, что они совпадают, и
    что пароль соответствует минимальным требованиям по длине.

    Метод create создает новый объект пользователя, используя валидированные данные.

    Параметры:
    - `email`: Email нового пользователя.
    - `password`: <ПАРОЛЬ>.
    - `password2`: Второе поле пароля для подтверждения.
    - `first_name`: Имя нового пользователя.
    - `last_name`: Фамилия нового пользователя.
    - `avatar`: Аватар нового пользователя.
    - `username`: Имя пользователя нового пользователя.

    Возвращает:
    - Новый объект пользователя, с полем пароля исключенным.
    """
    password = serializers.CharField(
        min_length=8, max_length=20, required=True, write_only=True
    )
    password2 = serializers.CharField(
        min_length=8, max_length=20, required=True, write_only=True
    )

    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "password2",
            "first_name",
            "last_name",
            "avatar",
            "username",
        )

    def validate(self, attrs: dict) -> dict:
        """
        Валидация входящих данных.

        Убедитесь, что пароли совпадают и что пароль соответствует минимальным
        требованиям по длине.

        Параметры:
        - `attrs`: Входящие данные.

        Возвращает:
        - Валидированные данные.
        """
        password = attrs['password']
        password2 = attrs.pop('password2')

        if password != password2:
            raise serializers.ValidationError(
                {"password": "Пароли не совпадают."}
            )

        validate_password(password)

        return attrs

    def create(self, validated_data: dict) -> User:
        """
        Создание нового пользователя.

        Параметры:
        - `validated_data`: Валидированные данные.

        Возвращает:
        - Новый пользователь.
        """
        user = User.objects.create_user(**validated_data)
        return user
