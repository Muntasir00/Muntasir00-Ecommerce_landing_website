from django.db import models

# Create your models here.
#from django.urls import reverse
from datetime import datetime

class Products(models.Model):
    title=models.CharField(max_length=200)
    #address=models.CharField(max_length=200)
    #city=models.CharField(max_length=100)
    #state=models.CharField(max_length=100)
    #zipcode=models.CharField(max_length=20)
    description=models.TextField(blank=True)
    price=models.IntegerField()
    image = models.ImageField(blank=True)
    in_stock=models.BooleanField(default=True)
    sold=models.BooleanField(default=False)
    list_date=models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.title

    #def get_absolute_url(self): # new
        #return reverse('product_detail', args=[str(self.id)])


class PostImage(models.Model):
    product = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'media/photos/')
 
    def __str__(self):
        return self.product.title


        