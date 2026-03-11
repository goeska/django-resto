from django.contrib import admin
from .models import Resto, RestoTag


class RestoTagInline(admin.TabularInline):
    model = RestoTag
    extra = 1

@admin.register(Resto)
class RestoAdmin(admin.ModelAdmin):
    list_display = ('name', 'area', 'address', 'opening_hours', 'map')
    search_fields = ('name', 'area', 'address', 'opening_hours')
    list_filter = ('area',)
    inlines = [RestoTagInline]
