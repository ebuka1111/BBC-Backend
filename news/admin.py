from django.contrib import admin
from .models import News
# Register your models here.

# @admin.register(News)
admin.site.register(News)

class NewAdmin(admin.ModelAdmin):
    list_display = ["headline", "category", "reporter"]
    list_filter = ["category"]
    search_fields = ["headlines", "reporter"]