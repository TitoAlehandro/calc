from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=30)
    user_id = models.ForeignKey(User)
    def __unicode__(self):
        return unicode(self.name)

class Place(models.Model):
    name = models.CharField(max_length=30)
    user_id = models.ForeignKey(User)
    def __unicode__(self):
        return unicode(self.name)

class Product(models.Model):
    name = models.CharField(max_length=30)
    user_id = models.ForeignKey(User)
    def __unicode__(self):
        return unicode(self.name)

class Balance(models.Model):
    user_id = models.ForeignKey(User)
    cur_date = models.DateField(auto_now_add=True)
    calc_date = models.DateField()
    balance = models.FloatField()
    def __unicode__(self):
        return unicode(self.name)   

class Book(models.Model):
    #date = models.DateField(auto_now_add=True)
    date = models.DateField()
    branch_id = models.ForeignKey(Branch)
    price = models.FloatField()
    place_id = models.ForeignKey(Place)
    product_id = models.ForeignKey(Product)
    user_id = models.ForeignKey(User)
    def __unicode__(self):
        return unicode(self.date)
class InfoNews(models.Model):
    date = models.DateField()
    inf = models.CharField(max_length=255)
    def __unicode__(self):
        return unicode(self.inf)