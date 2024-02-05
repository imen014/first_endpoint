from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api_app.models import Product,Category
from api_app.serializer import ProductSerializer, CategorySerializer



class ProductView(APIView):

    def get(self, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'products':serializer.data})


class CategoryView(APIView):
    def get(APIView):
        def get(self, *args, **kwargs):
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response({'categories':serializer.data})