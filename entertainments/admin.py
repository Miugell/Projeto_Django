from django.contrib import admin
from .models import Category, Entertainment

class CategoryAdmin(admin.ModelAdmin):

    ...

admin.site.register(Category,CategoryAdmin)
# Register your models here.


@admin.register(Entertainment)
class EntertainmentAdmin(admin.ModelAdmin):

    ...