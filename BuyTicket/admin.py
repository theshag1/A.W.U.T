from django.contrib import admin

from BuyTicket.models import BuyTicket


# Register your models here.

@admin.register(BuyTicket)
class BuyTickets(admin.ModelAdmin):
    list_display = ['first_name', 'fly', 'passport' , 'pay_fileds']
