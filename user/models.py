from django.db import models

# Create your models here.
class contactUs(models.Model):
    fullname=models.CharField( max_length=50)
    email=models.EmailField(max_length=254)
    message=models.CharField(max_length=50)



    
    # python manage.py makemigrations
    # python manage.py migrate