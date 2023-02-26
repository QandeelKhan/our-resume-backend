from rest_framework import generics
from .models import Order, OrderProgress
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import OrderSerializer, OrderProgressSerializer


class OrderListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderProgressListCreateAPIView(generics.ListCreateAPIView):
    queryset = OrderProgress.objects.all()
    serializer_class = OrderProgressSerializer


class OrderProgressDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderProgress.objects.all()
    serializer_class = OrderProgressSerializer
