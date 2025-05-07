from django.contrib import admin
from .models import Destination , Booking , Subscribe , PromoCode , PayementProof , Tarif

# Register your models here.

admin.site.register(Destination)
admin.site.register(Booking)
admin.site.register(Subscribe)
admin.site.register(PromoCode)
admin.site.register(Tarif)

@admin.register(PayementProof)
class PayementProofAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'trip_title', 'transfer_date', 'screenshot')
