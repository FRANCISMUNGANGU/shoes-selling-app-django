from django.db import models

# Create your models here.
class Shoes(models.Model):
    shoes_name = models.CharField(max_length=100)
    shoes_image = models.URLField()
    shoes_price = models.CharField(max_length=10000000)
    class Meta:
        db_table = 'shoes'

class Adminshoe(models.Model):
    shoesname = models.CharField(db_column='shoesname', max_length=100, blank=False)
    shoesimage = models.URLField(db_column='shoesimage', blank=False)
    shoesprice = models.CharField(db_column='shoesprice', max_length=100, blank=False)
    class Meta:
        db_table = 'adminshoe'
        verbose_name = 'Adminshoe'
        verbose_name_plural = 'Adminshoes'

    def __unicode__(self):
        return self.shoesname
    def __str__(self):
        return self.shoesname


class Checkout(models.Model):
    transactionID = models.CharField(db_column='transactionID', max_length=100, blank=False)
    amount = models.CharField(db_column='amount', max_length=100, blank=False)
    phone = models.CharField(db_column='phone', max_length=100, blank=False)
    class Meta:
        db_table = 'checkout'
        verbose_name = 'Checkout'
        verbose_name_plural = 'Checkouts'

    def __unicode__(self):
        return self.transactionID
    def __str__(self):
        return self.transactionID
