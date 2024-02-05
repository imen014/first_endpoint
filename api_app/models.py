from django.db import models


class Category(models.Model):
    name= models.CharField(max_length=50)
    description = models.CharField(max_length=255)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=50)