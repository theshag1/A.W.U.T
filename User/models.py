from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


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

    date_joined = models.DateTimeField(_("date joined"), default=datetime.now)

    user_ball = models.BigIntegerField(
        default=0,
        null=True,
        help_text=_(
            "You collect ball next you change your ball to someone our  items"

        )

    )
