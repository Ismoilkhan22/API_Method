from rest_framework import serializers

from core.models import Category, Product, User


class UserSerialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CtgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
