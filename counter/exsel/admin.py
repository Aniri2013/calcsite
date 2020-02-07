from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from .models import Product, Rubric


# class ProductAdmin(admin.ModelAdmin):
#     fields = ('name', 'composition', 'price', 'grams_per_person', 'weight', 'rubric', 'my_order')
#     list_display = ('name', 'composition', 'price', 'grams_per_person', 'rubric', 'my_order')
#     list_display_links = ('name', 'rubric')
#     search_fields = ('name', 'rubric')


@admin.register(Product)
class MyProductAdmin(SortableAdminMixin, admin.ModelAdmin):
	fields = ('name', 'composition', 'price', 'grams_per_person', 'weight', 'rubric', 'image')
    # list_display = ('name', 'composition', 'price', 'grams_per_person', 'rubric',)
    # list_display_links = ('name', 'rubric')
    # search_fields = ('name', 'rubric')


# admin.site.register(Product, ProductAdmin)
admin.site.register(Rubric)
