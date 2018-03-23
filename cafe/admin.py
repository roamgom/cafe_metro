from django.contrib import admin

from .models import Cafe
from .models import Station
from .models import CafeUser
from .models import Review


admin.site.register(Cafe)
admin.site.register(Station)
admin.site.register(CafeUser)
admin.site.register(Review)
