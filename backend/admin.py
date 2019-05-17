from django.contrib import admin

from .models import Item, Mob, Zone


admin.site.register(Mob)
admin.site.register(Zone)
admin.site.register(Item)
