from django.contrib import admin

from User.models import User, UserBall


# Register your models here.

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['username', 'email', 'user_phone', ]
    readonly_fields = []


@admin.register(UserBall)
class AdminUser(admin.ModelAdmin):
    list_display = ['user', 'ball']
    readonly_fields = ['ball']

    def save_model(self, request, obj, form, change):
        if not obj.ball:
            obj.ball = obj.ticket.fly_ball
            obj.save()


