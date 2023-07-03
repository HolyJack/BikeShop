from django.db import models

class Frame(models.Model):
    color = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return self.color
    
    def is_available(self):
        if self.quantity > 0:
            return True
        
        return False


class Seat(models.Model):
    color = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return self.color

    def is_available(self):
        if self.quantity > 0:
            return True
        
        return False


class Tire(models.Model):
    type = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return self.type

    def is_available(self):
        if self.quantity > 2:
            return True
        
        return False


class Attachment(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return 'Basket'

    def is_available(self):
        if self.quantity > 0:
            return True
        return False


class Bike(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    tires = models.ForeignKey(Tire, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def is_available(self):
        if self.frame.is_available() and self.tires.is_available() and self.seat.is_available():
            return True
        
        return False



class Order(models.Model):
    pass

class 