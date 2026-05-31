from django.contrib import admin
from .models import Task
 
 
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
 
    # Columns shown in the list view
    list_display  = ['title', 'status', 'priority', 'due_date', 'created_at']
 
    # Sidebar filter options
    list_filter   = ['status', 'priority']
 
    # Search box — searches these fields
    search_fields = ['title', 'description']
 
    # Edit these fields inline in the list (no need to open each task)
    list_editable = ['status', 'priority']
 
    # Default sort order
    ordering      = ['-created_at']