from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsOwnerOrAdmin(BasePermission):
    """
    Пользовательское разрешение для разрешения только владельцам объекта его редактировать.
    Предполагается, что модель пользователя имеет поле `user`.
    """

    def has_object_permission(self, request, view, obj):
        """
        Проверяет, является ли пользователь суперпользователем или является ли он владельцем объекта.
        """
        if request.user.is_superuser:
            return True
        return obj.user == request.user
