from django.contrib import admin
from . models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'completed', 'created')
    prepopulated_fields = ['slug'  ('title',)]
    
admin.site.register(Task, TaskAdmin)