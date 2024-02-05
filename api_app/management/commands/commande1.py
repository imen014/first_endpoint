from django.core.management.base import BaseCommand
from api_app.models import Product,Category


class Command(BaseCommand):

    help= "this class is created for testing command, it created some product"
    def handle(self,*args,**kwargs):
        categorie1=Category.objects.create(name="categorie1",description="this is the first category")
        categorie2=Category.objects.create(name="categorie2",description="this is the second category")
        categorie3=Category.objects.create(name="categorie3",description="this is the third category")


        name1="product1"
        name2="product2"
        name3="product3"
        owner1="first owner of first product"
        owner2="second owner of second product"
        owner3="third owner of third product"

        Product.objects.create(category=categorie1,name=name1,owner=owner1)
        Product.objects.create(category=categorie2,name=name2,owner=owner2)
        Product.objects.create(category=categorie3,name=name3,owner=owner3)
        Product.objects.create(category=categorie1,name=name1,owner=owner1)
        Product.objects.create(category=categorie2,name=name2,owner=owner2)
        Product.objects.create(category=categorie3,name=name3,owner=owner3)