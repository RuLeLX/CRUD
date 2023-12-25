from django.db import models

class Cooker(models.Model):
    id_cooker = models.PositiveIntegerField(primary_key=True)
    lastname = models.TextField()
    firstname = models.TextField()
    patronym = models.TextField()
    specials = models.TextField()

class Product(models.Model):
    id_product = models.PositiveIntegerField(primary_key=True)
    name = models.TextField()

class Dish(models.Model):
    id_dish = models.PositiveIntegerField(primary_key=True)
    name = models.TextField()
    main_product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE
    )