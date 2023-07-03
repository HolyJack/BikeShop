from django.db import models
from django.utils.crypto import get_random_string
from .constants import *


class ItemId(models.Model):
    ID_LENGHT = 6
    
    id = models.CharField(primary_key=True, max_length=ID_LENGHT, unique=True, editable=False, blank=False)
    
    
class Item(models.Model):
    ID_LENGHT = 6
    
    id = models.CharField(primary_key=True, max_length=ID_LENGHT, unique=True, editable=False, blank=False) 
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    date_added =  models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.generate_unique_id()
        
        ItemId(id=self.id).save()
        super().save(*args, **kwargs)
    
    def generate_unique_id(self):
        MAX_RETRIES = 10
        length = self.ID_LENGHT
        retries = 0
        ids = ItemId.objects.all()
        
        while retries < MAX_RETRIES:
            id = get_random_string(length=length)
            
            if not ids.filter(id=id).exists():
                return id
            retries += 1
        
        raise ValueError("Failed to generate new ID.")
    
    
class Tire(Item):    
    type = models.CharField(max_length=50, choices=TIRE_TYPES)


class Frame(Item):    
    type = models.CharField(max_length=50, choices=FRAME_TYPES) 
    material = models.CharField(max_length=50, choices=MATERIALS)
    weight = models.DecimalField(max_digits=5, decimal_places=2)


class Seat(Item):
    type = models.CharField(max_length=50, choices=SEATS_TYPES)
    
    
class Wheel(Item):   
    type = models.CharField(max_length=50, choices=WHEEL_TYPES)


class Bike(Item):
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    tires = models.ForeignKey(Tire, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    wheel = models.ForeignKey(Wheel, on_delete=models.CASCADE)


class Order(models.Model):
    ID_LENGHT = 4
    
    id = models.CharField(primary_key=True, max_length=ID_LENGHT, unique=True, editable=False, blank=False)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.generate_unique_id()
        
        ItemId(id=self.id).save()
        super().save(*args, **kwargs)
    
    def generate_unique_id(self):
        MAX_RETRIES = 10
        length = ID_LENGHT
        retries = 0
        ids = ItemId.objects.all()
        
        while retries < MAX_RETRIES:
            id = get_random_string(length=length)
            
            if not ids.filter(id=id).exists():
                return id
            retries += 1
        
        raise ValueError("Failed to generate new ID.")