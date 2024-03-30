from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Goods(models.Model):

    SIZES=[("S","Small"),("M","Medium"),("L","Large"),("XL","Xtra large")]
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    description=models.TextField()
    size=models.CharField(max_length=2,choices=SIZES)
    image_name=models.CharField(max_length=50)
    stock_controller=models.ForeignKey(User,on_delete=models.CASCADE)



