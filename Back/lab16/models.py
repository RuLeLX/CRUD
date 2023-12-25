from django.db import models

class Users(models.Model):
    email = models.TextField(primary_key=True)
    password = models.TextField()
    lastname = models.TextField()
    firstname = models.TextField()
    patronym = models.TextField()
    level_acces = models.PositiveIntegerField(default=1)


