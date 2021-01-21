from django.contrib import admin
from . import models

# Register your models here.

class GroupMemebrInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
