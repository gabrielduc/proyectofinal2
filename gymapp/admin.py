from django.contrib import admin

from .models import Profesional, ClienteGimnasio, Servicio
# Register your models here.

admin.site.register(Profesional)
admin.site.register(ClienteGimnasio)
admin.site.register(Servicio)