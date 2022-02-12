from django.db import models
from django.contrib.auth.models import AbstractUser
from adminApp.models import *
from django.utils import timezone
import uuid

# Create your models here.

class CustomUser(AbstractUser):
    number = models.CharField(max_length=100, unique=True)
    block = models.BooleanField(default=0)


# cart management
class cart(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE,  null=True)
    variant_id = models.ForeignKey(VariantAndPrice, on_delete=models.CASCADE)
    quantity = models.BigIntegerField(default=1)
    subtotal = models.BigIntegerField(default=1)
    guest_user = models.CharField(max_length=250, null=True)
    class Meta:
        db_table = "cart"


class address(models.Model):
    full_name=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    mobile_number=models.CharField(max_length=10)
    zipcode=models.CharField(max_length=6)
    address=models.TextField()
    user_id=models.ForeignKey(CustomUser, on_delete=models.CASCADE)




class order(models.Model):
    total_qty = models.BigIntegerField()
    date = models.DateTimeField(default=timezone.now)
    # address_id = models.ForeignKey(address, on_delete=models.SET_NULL, null=True)
    order_status = models.CharField(max_length=100, default="Order Placed")
    userId = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    variant_id = models.ForeignKey(VariantAndPrice, on_delete=models.SET_NULL, null=True, related_name='orders')
    subtotal = models.BigIntegerField()
    order_id = models.UUIDField(default=uuid.uuid4, editable=False)
    payment_method = models.CharField(max_length=100)
    address = models.TextField()
    coupen_id = models.ForeignKey(Coupen, on_delete=models.SET_NULL, null=True )    