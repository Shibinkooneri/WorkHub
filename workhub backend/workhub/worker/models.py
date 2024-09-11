from django.db import models
from customer.models import Customer

# Create your models here.
class Worker(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    dob=models.DateField()
    gender=models.CharField(max_length=20)
    phone=models.IntegerField()
    email=models.EmailField()
    location=models.CharField(max_length=100)
    options=(
        ('coolie','coolie'),
        ('plumber','plumber'),
        ('Electrician','Electrician'),
        ('Mechanic','Mechanic')
    )
    work_profile=models.CharField(max_length=100,choices=options)
    profilepic=models.ImageField(upload_to='worker_pics')


class Works(models.model):
    worker=models.CharField(max_length=50,primary_key=Worker)
    work_id=models.IntegerField(auto_created=True)
    customer_id=models.IntegerField(primary_key=Customer)
    