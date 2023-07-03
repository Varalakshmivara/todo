from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display=('task','is_completed','modified_at')
    search_fields=('task',)

# Register your models here.
admin.site.register(Task,TaskAdmin)
