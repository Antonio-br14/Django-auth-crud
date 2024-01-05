from django.contrib import admin
from .models import Task

class Taskadmin(admin.ModelAdmin):
    readonly_fields = ('created',)
admin.site.register(Task, Taskadmin)
