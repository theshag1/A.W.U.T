from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from validate import phone_validate


# Create your models here.


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    user_phone = models.CharField(
        max_length=18,
        validators=[phone_validate],
        help_text=_('You must be enter phone number')
    )
    balls = models.CharField(max_length=125656)

    @property
    def ball(self):
        return self.user_s.count()


class UserBall(models.Model):
    user = models.ForeignKey('User.User', on_delete=models.CASCADE, related_name='user_s')
    ticket = models.ForeignKey('BuyTicket.BuyTicket', on_delete=models.CASCADE, related_name='ball_sum')
    ball = models.CharField(max_length=1000)
