from django.db import models
from django.utils.translation import gettext_lazy as _
from choices import gander
from validate import Passport_validate
from rest_framework.exceptions import ValidationError


# Create your models here.
class BuyTicket(models.Model):
    first_name = models.CharField(
        max_length=300,
        null=False,
        help_text=_('You must enter your first name'),
        error_messages={'error': 'You dont enter name '}
    )
    last_name = models.CharField(
        max_length=300,
        null=False,
        help_text=_('You must enter your first name'),
        error_messages={'error': 'You dont enter name '}
    )

    date_of_brith = models.CharField(
        max_length=100,
        help_text=_('Please input your brith "2000/01/01" format '),
        null=False
    )
    gander = models.CharField(choices=gander, null=False)
    passport = models.CharField(
        max_length=9,
        validators=[Passport_validate],
        help_text=_('Please enter Passport example "AD1234578" '),
        error_messages={'error': 'Your  passport must be start "AD"'}

    )
    phone = models.CharField(max_length=100, null=False, help_text=_('Please input your phone'),
                             error_messages={'error': 'You dont input phone'})

    email = models.EmailField(max_length=100, null=False, help_text=_('Please input your email'),
                              error_messages={'error': 'You dont input email'})

    def __str__(self):
        return self.first_name
