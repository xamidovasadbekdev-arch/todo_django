from django.contrib import admin
from .models import Todo


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'priority', 'status', 'due_date', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'priority', 'user')
    list_editable = ('status', 'priority')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)