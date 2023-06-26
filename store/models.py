from django.db import models

from .utils import *
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(max_length = 500)
    
class MicroHistory(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    item_name = models.CharField(max_length = 500)
    amount = models.CharField(max_length = 500)
    bal = models.CharField(max_length = 500, null=True, blank=True)
    dept = models.ForeignKey(Department, related_name="micro_history_category",
                                        on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=2000, null=True, blank=True)
    
class HaemHistory(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    item_name = models.CharField(max_length = 500)
    amount = models.CharField(max_length = 500)
    bal = models.CharField(max_length = 500, null=True, blank=True)
    dept = models.ForeignKey(Department, related_name="haem_history_category",
                                        on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=2000, null=True, blank=True)
    
class ChemHistory(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    item_name = models.CharField(max_length = 500)
    amount = models.CharField(max_length = 500)
    bal = models.CharField(max_length = 500, null=True, blank=True)
    dept = models.ForeignKey(Department, related_name="chem_history_category",
                                        on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=2000, null=True, blank=True)
        
class HistoHistory(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    item_name = models.CharField(max_length = 500)
    amount = models.CharField(max_length = 500)
    bal = models.CharField(max_length = 500, null=True, blank=True)
    dept = models.ForeignKey(Department, related_name="histo_history_category",
                                        on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=2000, null=True, blank=True)
    

class Items(models.Model):
    item_id = models.IntegerField()
    item_name = models.CharField(max_length = 500)
    amount = models.DecimalField(max_digits=15, decimal_places=1, default=0.0)
    dept = models.ForeignKey(Department, related_name="item_category",
                                        on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=2000, null=True, blank=True)

@receiver(pre_save, sender=Items)
def pre_save_receiver(sender, instance, *args, **kwargs):
   if not instance.slug:
       instance.slug = unique_slug_generator(instance)
       


