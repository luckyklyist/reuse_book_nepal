from distutils.command.upload import upload
from random import choices
from secrets import choice
from django.db import models
from django.contrib.auth.models import User

from django_google_maps import fields as map_fields

class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
    
class product(models.Model):
    seller=models.CharField(max_length=100,blank=True, null=True,default="")
    price=models.IntegerField()
    product_name=models.CharField(max_length=70)
    img=models.ImageField(upload_to="static/img_product")
    description=models.TextField()
    slug=models.CharField(max_length=500,blank=False,null=False,default="")

    def __str__(self):
        return self.product_name

gender_choices=(
    ('male','male'),
    ('female','female'),
    ('others','others'),
)

class proflie_users(models.Model):
    username=models.CharField(max_length=50)
    phone_no=models.IntegerField()
    profile_pic=models.ImageField(upload_to="static/profile_pic")
    location=models.CharField(max_length=80)
    age=models.IntegerField()
    gender=models.CharField(max_length=6,choices=gender_choices)
    
    def __str__(self):
        return self.username
    
class ask_question(models.Model):
    post=models.ForeignKey(product,on_delete=models.CASCADE,null=True)
    username=models.CharField(max_length=100)
    date_posted=models.DateTimeField()
    questions=models.TextField()
    id_ask=models.CharField(max_length=100)
    
class reply_ask(models.Model):
    id_reply=models.IntegerField()
    username=models.CharField(max_length=100)
    comment=models.ForeignKey(ask_question,on_delete=models.CASCADE,null=True)
    date_posted=models.DateTimeField()
    reply=models.TextField()
    
    


