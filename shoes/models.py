from django.db import models

# Create your models here.
class Shoes(models.Model):
    shoes_name = models.CharField(max_length=100)
    shoes_image = models.URLField()
    shoes_price = models.CharField(max_length=1000000)
    class Meta:
        db_table = 'shoes'

# class Persons(models.Model):
#     persons_phonenumber = models.CharField(max_length=20)
#     class Meta:
#         db_table = 'persons'
