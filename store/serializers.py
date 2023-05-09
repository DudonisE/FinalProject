from rest_framework import serializers
from store.models import Size, Category, Product


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ['owner','name', 'color', 'description', 'price',]

