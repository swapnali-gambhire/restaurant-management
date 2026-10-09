from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, MenuItem, Table, Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "table", "status", "created_at")
    list_filter = ("status",)
    inlines = [OrderItemInline]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "is_available")
    list_filter = ("category", "is_available")


admin.site.register(Category)
admin.site.register(Table)