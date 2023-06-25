from django.contrib import admin

from Discount.models import Discount
from functions.function import percentage


# Register your models here.

class Discounts(admin.ModelAdmin):
    list_display = ['ticket', 'old_price', 'discount_price']
    readonly_fields = ['old_price', 'discount_price']

    def save_model(self, request, obj, form, change):
        if not obj.old_price:
            obj.old_price = obj.ticket.ticket_price
        obj.save()
        number = percentage(int(obj.old_price), int(obj.percentage.split('%')[0]))
        if not obj.discount_price:
            obj.discount_price = str(number)
            obj.save()


admin.site.register(Discount, Discounts)
