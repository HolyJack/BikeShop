from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    date_added =  models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name
    
    
class Tire(Item):
    TIRE_TYPES = [
        ("Clincher", "Clincher"),
        ("Tubular", "Tubular"),
        ("Tubeless", "Tubeless")
        ]
    
    type = models.CharField(max_length=8, choices=TIRE_TYPES)
    
class Frame(Item):
    MATERIALS = [
        ("Aluminium", "Aluminium"),
        ("Steel", "Steel"),
        ("Carbon fiber", "Carbon fiber"),
        ("Titanium", "Titanium")]
    BIKE_TYPES = [
        ("Road Frame", "Road Frame"),
        ("Mountain Bike Frame", "Mountain Bike Frame"),
        ("Hybrid Frame", "Hybrid Frame"),
        ("Cyclocross Frame", "Cyclocross Frame"),
        ("Touring Frame", "Touring Frame"),
        ("Folding Frame", "Folding Frame"),
        ("BMX Frame", "BMX Frame")
        ]
    
    type = models.CharField(max_length=19, choices=BIKE_TYPES) 
    material = models.CharField(max_length=12, choices=MATERIALS)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

class Seat(Item):
    SEATS_TYPES = [
        ("Road Bike Saddle", "Road Bike Saddle"),
        ("Mountain Bike Saddle", "Mountain Bike Saddle"),
        ("Commuter/Comfort Saddle", "Commuter/Comfort Saddle"),
        ("Hybrid Bike Saddle", "Hybrid Bike Saddle"),
        ("Touring Saddle", "Touring Saddle"),
        ("Triathlon/Time Trial Saddle", "Triathlon/Time Trial Saddle"),
        ("Gel Saddle", "Gel Saddle"),
        ("Leather Saddle", "Leather Saddle"),
        ("Women's Saddle", "Women's Saddle"),
        ("Men's Saddle", "Men's Saddle")
        ]
    
    type = models.CharField(max_length=27, choices=SEATS_TYPES)
    
class Wheel(Item):
    WHEEL_TYPES = [
        ("Road Bike Wheel", "Road Bike Wheel"),
        ("Mountain Bike Wheel", "Mountain Bike Wheel"),
        ("Hybrid Bike Wheel", "Hybrid Bike Wheel"),
        ("Cyclocross Bike Wheel", "Cyclocross Bike Wheel"),
        ("Touring Bike Wheel", "Touring Bike Wheel"),
        ("BMX Bike Wheel", "BMX Bike Wheel"),
        ("Fat Bike Wheel", "Fat Bike Wheel"),
        ("Gravel Bike Wheel", "Gravel Bike Wheel"),
        ("Triathlon Bike Wheel", "Triathlon Bike Wheel")
    ]
    
    type = models.CharField(max_length=21, choices=WHEEL_TYPES)

class Bike(Item):
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    tires = models.ForeignKey(Tire, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    wheel = models.ForeignKey(Wheel, on_delete=models.CASCADE)