from rest_framework import serializers
from api_app.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category','name','owner']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','description']