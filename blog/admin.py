from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'date_register', 'phone_number']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'date_publication', 'author', 'total_view', 'counter_like']
    list_filter = ['category', 'author', 'date_publication']
    search_fields = ['title', 'description']

    def counter_like(self, obj):
        return obj.likes.count()

    counter_like.short_description = 'Likes'

    def get_readonly_fields(self, request, obj=None):
        """
        Делаем поле `counter_like` только для чтения
        """
        if obj:
            return ['counter_like']
        return []

    def save_model(self, request, obj, form, change):
        """
        Обновляем счетчик лайков при изменении модели через админку
        """
        obj.counter_like = obj.likes.count()
        super().save_model(request, obj, form, change)

# admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Product, ProductAdmin)