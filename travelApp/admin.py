from django.contrib import admin
from .models import Destination , booking , Subscribe , PromoCode , PayementProof , Tarif

# Register your models here.

admin.site.register(Destination)
admin.site.register(booking)
admin.site.register(Subscribe)
admin.site.register(PromoCode)
admin.site.register(PayementProof)
admin.site.register(Tarif)
