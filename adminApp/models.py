from datetime import timezone
from email import message
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.forms import ValidationError
from django.utils import timezone
from django.core.validators import MinValueValidator
import re

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)
    offer = models.IntegerField()
    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.category


class SubCategory(models.Model):
    brand_name = models.CharField(max_length=100)
    c_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:
        db_table = 'subcategory'

    def __str__(self):
        return self.brand_name
    


def FindOnlyDigit( value, field):
    if str(value).isdigit() == False:
        raise ValidationError(
            {field : "only numbers are allowded"})

ProcessorChoice = (
    ('Snapdragon', 'Snapdragon'),
    ('MediaTek', 'MediaTek'),
    ('bionic', 'bionic'),

)

class products(models.Model):

    product_name = models.CharField(max_length=200)

    date = models.DateTimeField(default=timezone.now)


    battery = models.BigIntegerField(validators=[MinValueValidator(1)], null=True)


    rom = models.IntegerField(null=True, validators=[MinValueValidator(1)])
    front_camera = models.IntegerField(null=True, validators=[MinValueValidator(1)])
    back_camera = models.IntegerField(null=True, validators=[MinValueValidator(1)])
    brand_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    img1= models.ImageField(upload_to='images/', null=True)
    img2= models.ImageField(upload_to='images/', null=True)
    img3= models.ImageField(upload_to='images/', null=True)
    offer = models.IntegerField(default=0)

    processor = models.CharField(max_length=20 , choices=ProcessorChoice)


    class Meta:
        db_table = "products"
    

    def __str__(self):
        return self.product_name

    def clean(self):
        FindOnlyDigit(self.battery, 'battery')
        FindOnlyDigit(self.rom, 'rom')
        FindOnlyDigit(self.battery, 'battery')
        FindOnlyDigit(self.front_camera, 'front_camera')
        FindOnlyDigit(self.back_camera, 'back_camera')



class VariantAndPrice(models.Model):
    variant = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.BigIntegerField(validators=[MinValueValidator(1)])
    product_id = ForeignKey(products, on_delete=models.CASCADE, null=True, related_name='allvariants')
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    final_price = models.BigIntegerField(default=0)
    class Meta:
        db_table = "variantandprice"


class Banner(models.Model):
    bannerimg= models.ImageField(upload_to='images/', null=True)
    p_id = ForeignKey(products, on_delete=models.CASCADE)


class Coupen(models.Model):
    coupen_offer = models.IntegerField()
    coupen_code = models.CharField(max_length=20, unique=True)

