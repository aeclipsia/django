from django.db import models

# Create your models here.

class Usuario(models.Model):
    usuario=models.CharField(max_length=30,primary_key=True)
    password=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    tel=models.DecimalField(max_digits=4,decimal_places=0)
    registro=models.DateField()
    acceso=models.DateField()