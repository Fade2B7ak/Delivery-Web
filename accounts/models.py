from tkinter import CASCADE
from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=20, null=True)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=50, null=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):


    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    name= models.CharField(max_length=500, null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=100, choices=CATEGORY, null=True)
    description=models.CharField(max_length=5000, null=True, blank=True)
    day_created=models.DateField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    day_created = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, choices=STATUS ,null=True)

    def __str__(self):
        return self.product.name