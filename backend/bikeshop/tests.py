from django.test import TestCase
from decimal import Decimal
from .models import *

class ModelInstanceCreator(TestCase):
    
    @staticmethod
    def create_tire(
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
    
    @staticmethod
    def create_frame(
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
    
    @staticmethod
    def create_wheel(
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
    
    @staticmethod
    def create_seat(
        name='test',
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
    
    @staticmethod
    def create_bike(
        name='test',
        active=True,
        quantity=0,
        unit_price=Decimal("0.0")
        ):
        
        tires = ModelInstanceCreator.create_tire()
        frame = ModelInstanceCreator.create_frame()
        wheel = ModelInstanceCreator.create_wheel()
        seat = ModelInstanceCreator.create_seat()
        
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
        

class ItemIdTest(TestCase):
    
    def test_tire_id_creation(self):
        t = ModelInstanceCreator.create_tire()
        i = ItemId.objects.all().filter(id=t.id)[0]
        self.assertEqual(t.id, i.id)


class TireTest(TestCase):

    def test_tire_creation(self):
        t = ModelInstanceCreator.create_tire()
        self.assertTrue(isinstance(t, Tire))
        self.assertEqual(t.__str__(), t.name)


class FrameTest(TestCase):
    
    def test_frame_creation(self):
        f = ModelInstanceCreator.create_frame()
        self.assertTrue(isinstance(f, Frame))
        self.assertEqual(f.__str__(), f.name)


class SeatTest(TestCase):

    def test_seat_creation(self):
        s = ModelInstanceCreator.create_seat()
        self.assertTrue(isinstance(s, Seat))
        self.assertEqual(s.__str__(), s.name)


class WheelTest(TestCase):

    def test_wheel_creation(self):
        w = ModelInstanceCreator.create_wheel()
        self.assertTrue(isinstance(w, Wheel))
        self.assertEqual(w.__str__(), w.name)


class BikeTest(TestCase):
    
    def test_bike_creation(self):
        b = ModelInstanceCreator.create_bike()
        self.assertTrue(isinstance(b, Bike))
        self.assertEqual(b.__str__(), b.name)