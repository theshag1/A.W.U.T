from django.contrib import admin

from User.models import User


# Register your models here.

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['username', 'email', 'user_phone', ]
    readonly_fields = ['user_ball']
