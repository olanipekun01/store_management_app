from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Department)
admin.site.register(Items)
admin.site.register(MicroHistory)
admin.site.register(HaemHistory)
admin.site.register(ChemHistory)
admin.site.register(HistoHistory)
admin.site.register(SessionUser)