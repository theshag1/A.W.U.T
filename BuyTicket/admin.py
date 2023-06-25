from django.contrib import admin

from BuyTicket.models import BuyTicket


# Register your models here.

@admin.register(BuyTicket)
class Buyticket(admin.ModelAdmin):
    list_display = ['user', 'fly']
    readonly_fields = ['fly_ball']

    def save_model(self, request, obj, form, change):
        if not obj.fly_ball:
            obj.fly_ball = obj.fly.ball
            obj.save()
        if obj.fly.ball:
            obj.user.user_ball += obj.fly_ball
            obj.save()
