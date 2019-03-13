from django.contrib import admin

# Register your models here.
from . import models
class todoadmin(admin.ModelAdmin):
    list_display = ("title",  "created", "due_date")
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
admin.site.register(models.todo, todoadmin)
admin.site.register(models.Category, CategoryAdmin)