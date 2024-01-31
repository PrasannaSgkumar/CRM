
from django.db import models
from .models import  *
#gets all customers
customer=Customer.objects.all()

#to get first customer
firstcustomer=Customer.objects.first()

#to get last customer
lastcustomer=Customer.objects.last()

#Customer by name

customerbyname=Customer.objects.get(name="Kiran")

#Get customer by id

customerbyid=Customer.objects.get(id=4)

#Return all the orders relatedd to customer

firstcustomer=Orders_set.all()

# Returns orders customers name:

orders=Orders.objects.all()
parentname=orders.customer.name

#retrun products from product tabel

products=Products.objects.filter(category="Outdoor")

allorders={}

for i in firstcustomer.Order_set.all():
    if i.product.name in allorders:
        allorders[i.product.name]+=1
    else:
        allorders[i.product.name]=1

class ParentModel(models.Model):
    name=models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
    parent=models.ForeignKey(ParentModel)
    name=models.CharField(max_length=200, null=True)

parent=ParentModel.objects.first()

parent.ChildModel_set.all()


