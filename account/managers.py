from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    """
    Пользовательский менеджер, который переопределяет методы create_user и create_superuser по умолчанию.
    """

    use_in_migrations = True  # Используется в миграциях

    def _create_user(self, email, password, **kwargs):
        """
        Создает и сохраняет пользователя с указанным email и паролем.
        """
        if not email:
            raise ValueError('Укажите email!')
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **kwargs):
        """
        Создает и сохраняет обычного пользователя с указанным email и паролем.
        """
        kwargs.setdefault('is_staff', False)  # По умолчанию не персонал
        kwargs.setdefault('is_superuser', False)  # По умолчанию не суперпользователь
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        """
        Создает и сохраняет суперпользователя с указанным email и паролем.
        """
        kwargs.setdefault('is_staff', True)  # По умолчанию персонал
        kwargs.setdefault('is_superuser', True)  # По умолчанию суперпользователь
        kwargs.setdefault('is_active', True)  # По умолчанию активен
        return self._create_user(email, password, **kwargs)
