from django.contrib import admin
from .models import Tag, TagRelation

# Register your models here.
@admin.register(Tag, TagRelation)
class DefaultAdmin(admin.ModelAdmin):
    pass
