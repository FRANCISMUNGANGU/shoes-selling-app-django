from django.db import models

# Create your models here.
class Shoes(models.Model):
    shoes_name = models.CharField(max_length=100)
    shoes_image = models.URLField()
    shoes_price = models.CharField(max_length=1000000)
    class Meta:
        db_table = 'shoes'
