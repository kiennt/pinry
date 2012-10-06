from django.contrib import admin

from pinry.pins.models import Pin
from pinry.core.models import Member


class PinAdmin(admin.ModelAdmin):
    list_display = ['published', 'description']


admin.site.register(Pin, PinAdmin)
admin.site.register(Member)
