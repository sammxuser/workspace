from datetime import datetime, timedelta
from django.contrib import admin
from .models import Task,TaskFile, Writer


class TaskInLine(admin.StackedInline):
    model = TaskFile
    extra = 1

class TaskAdmin(admin.ModelAdmin):
    inlines = [TaskInLine]
    list_display = ('task_number','topic','pages','slides','style','date_due',
                    'task_cost','task_cpp','sources','task_status')
    list_filter = ['date_due', 'task_status']
    search_fields = ['task_number']
    date_hierarchy = 'date_due'

admin.site.register(Task, TaskAdmin)
admin.site.register(Writer)
