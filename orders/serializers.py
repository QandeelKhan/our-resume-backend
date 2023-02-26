from rest_framework import serializers
from .models import Order, OrderProgress


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'user',
            'order_type',
            'status',
            'payment_status',
            'description',
            'project_name',
            'project_description',
            'total_price',
            'created_at',
            'due_date',
            'updated_at'
        )


class OrderProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProgress
        fields = (
            'id',
            'order',
            'frontend_percentage',
            'backend_percentage',
            'design_percentage',
            'created_at',
            'updated_at'
        )
