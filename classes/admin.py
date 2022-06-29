from django.contrib import admin
from .models import FitnessClass


class FitnessClassAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'instructor',
        'spaces',
        'image_url',
        'image',
        'date',
        'description',
    )
    ordering = ('date',)

admin.site.register(FitnessClass, FitnessClassAdmin)
