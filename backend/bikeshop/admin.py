from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    exclude = ('id',)


class FrameAdmin(ItemAdmin):
    pass


class SeatAdmin(ItemAdmin):
    pass


class TireAdmin(ItemAdmin):
    pass


class WheelAdmin(ItemAdmin):
    pass


class BikeAdmin(ItemAdmin):
    pass


admin.site.register(Frame, FrameAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Tire, TireAdmin)
admin.site.register(Wheel, WheelAdmin)
admin.site.register(Bike, BikeAdmin)