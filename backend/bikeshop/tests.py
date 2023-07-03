from django.test import TestCase
from decimal import Decimal
from .models import *

class TireTest(TestCase):

    def create_tire(
        self,
        name='test',
        active=True,
        quantity=0,
        unit_price=Decimal("0.0"),
        type="Clincher"):
        
        return Tire.objects.create(
            name=name,
            active=active,
            quantity=quantity,
            unit_price=unit_price,
            type=type
            )

    def test_tire_creation(self):
        t = self.create_tire()
        self.assertTrue(isinstance(t, Tire))
        self.assertEqual(t.__str__(), t.name)


class FrameTest(TestCase):
    
    def create_frame(
        self,
        name='test',
        active=True,
        quantity=0,
        unit_price=Decimal("0.0"),
        type="Road Frame",
        material="Aluminium",
        weight=Decimal("0.0")):
        
        return Frame.objects.create(
            name=name,
            active=active,
            quantity=quantity,
            unit_price=unit_price,
            type=type,
            material=material,
            weight=weight
            )

    def test_frame_creation(self):
        f = self.create_frame()
        self.assertTrue(isinstance(f, Frame))
        self.assertEqual(f.__str__(), f.name)


class SeatTest(TestCase):
    
    def create_seat(
        self,name='test',
        active=True,
        quantity=0,
        unit_price=Decimal("0.0"),
        type="Road Bike Saddle"):
        
        return Seat.objects.create(
            name=name,
            active=active,
            quantity=quantity,
            unit_price=unit_price,
            type=type
            )

    def test_seat_creation(self):
        s = self.create_seat()
        self.assertTrue(isinstance(s, Seat))
        self.assertEqual(s.__str__(), s.name)


class WheelTest(TestCase):
    
    def create_wheel(
        self,
        name='test',
        active=True,
        quantity=0,
        unit_price=Decimal("0.0"),
        type="Road Bike Wheel"):
        
        return Wheel.objects.create(
            name=name,
            active=active,
            quantity=quantity,
            unit_price=unit_price,
            type=type
            )

    def test_wheel_creation(self):
        w = self.create_wheel()
        self.assertTrue(isinstance(w, Wheel))
        self.assertEqual(w.__str__(), w.name)


class BikeTest(TestCase):
    
    def create_tire(
        self,
        name='test',
        active=True,
        quantity=0,
        unit_price=Decimal("0.0"),
        type="Clincher"):
        
        return Tire.objects.create(
            name=name,
            active=active,
            quantity=quantity,
            unit_price=unit_price,
            type=type
            )
    
    def create_frame(
        self,
        name='test',
        active=True,
        quantity=0,
        unit_price=Decimal("0.0"),
        type="Road Frame",
        material="Aluminium",
        weight=Decimal("0.0")):
        
        return Frame.objects.create(
            name=name,
            active=active,
            quantity=quantity,
            unit_price=unit_price,
            type=type,
            material=material,
            weight=weight
            )
    
    def create_wheel(
        self,
        name='test',
        active=True,
        quantity=0,
        unit_price=Decimal("0.0"),
        type="Road Bike Wheel"):
        
        return Wheel.objects.create(
            name=name,
            active=active,
            quantity=quantity,
            unit_price=unit_price,
            type=type
            )
        
    def create_seat(
        self,name='test',
        active=True,
        quantity=0,
        unit_price=Decimal("0.0"),
        type="Road Bike Saddle"):
        
        return Seat.objects.create(
            name=name,
            active=active,
            quantity=quantity,
            unit_price=unit_price,
            type=type
            )
    
    def create_bike(
        self,
        tires,
        frame,
        seat,
        wheel,
        name='test',
        active=True,
        quantity=0,
        unit_price=Decimal("0.0")
        ):
        
        return Bike.objects.create(
            name=name,
            active=active,
            quantity=quantity,
            unit_price=unit_price,
            tires=tires,
            frame=frame,
            wheel=wheel,
            seat=seat
            )

    def test_bike_creation(self):
        t = self.create_tire()
        f = self.create_frame()
        w = self.create_wheel()
        s = self.create_seat()
        b = self.create_bike(tires=t, frame=f, wheel=w, seat=s)
        self.assertTrue(isinstance(b, Bike))
        self.assertEqual(b.__str__(), b.name)