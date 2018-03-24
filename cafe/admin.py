from django.contrib import admin

from .models import Cafe
from .models import Station
from .models import CafeUser
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_filter = ['cafe']


@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    list_filter = ['station']


admin.site.register(Station)
admin.site.register(CafeUser)

