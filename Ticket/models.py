from django.db import models
from django.utils.translation import gettext_lazy as _
from choices import payment_choices


# Create your models here.

class Ticket(models.Model):
    Ticket_from = models.CharField(
        max_length=1000,
        null=False,
    )
    Ticket_to = models.CharField(
        max_length=1000,
        null=False,
    )
    date = models.DateField(
        auto_created=True,
        null=False,
    )
    pay_opition = models.CharField(
        null=False,
        choices=payment_choices,
        help_text=_('You can choices Payment method'),
        error_messages={'error': 'You dont choices Payment method'}
    )



