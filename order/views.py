from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from order import serializers
from order.models import Order
from order.serializers import OrderSerializer


class OrderAPIView(ListCreateAPIView):
    serializer_class = serializers.OrderSerializer
    def get(self, request, *args, **kwargs):
        user = request.user
        orders = user.orders.all()
        serializer = serializers.OrderSerializer(instance=orders, many=True)
        return Response(serializer.data, status=200)

class OrderHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)