from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    dob=models.DateField()
    gender=models.CharField(max_length=20)
    phone=models.IntegerField()
    email=models.EmailField()
    location=models.CharField(max_length=100)
    profilepic=models.ImageField(upload_to='customer_pics')