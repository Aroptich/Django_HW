from django.contrib import admin
from hw2.models import Product, Order, Client

@admin.action(description="Сбросить количество")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'quantity', 'price']
    ordering = ['name', '-quantity']
    list_filter = ['price']
    search_fields = ['description']
    search_help_text = 'Поиск по Описание продукта (description)'
    actions = [reset_quantity]


    fields = ['name', 'description', 'quantity', 'price']
    readonly_fields = ['name']

class ClientAdmin(admin.ModelAdmin):

    list_display = ['name', 'email', 'phone', 'address', 'date_registered']
    ordering = ['name', 'phone']
    list_filter = ['name']
    search_fields = ['name', 'email', 'phone']
    search_help_text = 'Поиск по полю name (description)'



    fields = ['name', 'email', 'phone', 'address', 'date_registered']
    readonly_fields = ['name', 'date_registered']

class OrderAdmin(admin.ModelAdmin):



    def _products(self, row):
        return ','.join([x.name for x in row.products.all()])

    def _customer(self, row):
        return row.customer.name

    list_display = ['_customer', '_products', 'total_price', 'date_ordered']
    ordering = ['customer', 'total_price', 'date_ordered']
    list_filter = ['total_price']
    search_fields = ['customer', 'date_ordered']



    # """Заказ."""
    fields = ['customer', 'products', 'total_price', 'date_ordered']
    readonly_fields = ['date_ordered']





admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)