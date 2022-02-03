from django.contrib import admin
from rango.models import Category, Page


class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Page, ModuleAdmin)
admin.site.register(Category, CategoryAdmin)
