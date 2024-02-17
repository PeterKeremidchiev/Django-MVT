from django.contrib import admin

from Class_based_views_basics.web.models import TodoList, Category


# Register your models here.
@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'deadline', 'date_created', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
