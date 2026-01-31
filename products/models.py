from django.db import models

class Product(models.Model):
    item_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
