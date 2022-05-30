from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='img/products')

    