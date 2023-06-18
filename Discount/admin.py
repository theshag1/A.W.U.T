from django.contrib import admin

from Discount.models import Discount


# Register your models here.

class Discounts(admin.ModelAdmin):
    list_display = ['ticket', 'old_price']
    readonly_fields = ['old_price']

    def save_model(self, request, obj, form, change):
        if not obj.old_price:
            obj.old_price = obj.ticket.ticket_price
        obj.save()

#
# class Price(admin.ModelAdmin):
#
#     def save_model(self, request, obj, form, change):
#
#         if not obj.discount_price:
#             obj.discount_price =
#
# admin.site.register(Discount, Discounts)

