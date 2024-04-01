from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class CustomUser(AbstractUser):
    """
    Модель CustomUser, наследуемая от модели Django AbstractUser.
    Эта модель добавляет дополнительные поля, такие как адрес электронной почты, имя, фамилия,
    имя пользователя, код активации, аватар и is_active.
    """

    email = models.EmailField(_('email'), unique=True)
    first_name = models.CharField(_('first Name'), max_length=150)
    last_name = models.CharField(_('last Name'), max_length=150)
    username = models.CharField(max_length=100, blank=True)
    activation_code = models.CharField(max_length=150, blank=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, default='avatars/default_avatar.jpg.png')
    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        """
        Returns the email of the user.
        """
        return f'{self.email}'

    def create_activation_code(self):
        """
        Создает уникальный код активации для пользователя и сохраняет его в
        Поле активации_кода.
        """
        code = str(uuid4())
        return code

    def save(self, *args, **kwargs):
        self.activation_code = self.create_activation_code()
        super().save(*args, **kwargs)
