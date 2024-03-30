
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response


from . import serializers
from .send_mail import send_confirmation_email
from rest_framework.permissions import AllowAny, IsAuthenticated


User = get_user_model()

class UserViewSet(ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [IsAuthenticated()]
        return [AllowAny()]

    #api/v1/accounts/register/
    @action(['POST'], detail=False)
    def register(self, request, *args, **kwargs):
        serializer = serializers.RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            try:
                send_confirmation_email(user.email, user.activation_code)
            except Exception as e:
                print('!!!!')
                return Response({'msg': 'Registered, but troubles with email!',
                                 'data': serializer.data}, status=201)
        return Response({'message': 'Registered and sent mail', 'data': serializer.data},
                        status=201)
