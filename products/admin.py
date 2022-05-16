from django.contrib import admin
from .models import Product, Category

# Register your models here.
# removed 'rating' as not important to Barre Fitness shop
# will be removed possibly add instock number


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'brand',
        'category',
        'variants',
        'stock',
        'price',
        'image',
    )
    ordering = ('brand',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
