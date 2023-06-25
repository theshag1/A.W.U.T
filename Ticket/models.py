from django.db import models
from functions.choices import tiket_class
import random


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
        null=False,
    )
    ticket_price = models.CharField(
        null=False,

    )
    time = models.TimeField(null=False)
    tiket_number = models.CharField(default=random.randint(100000, 999999), null=False)
    bugges = models.SmallIntegerField(null=False, default=20)
    hand_bugges = models.SmallIntegerField(null=False, default=8)
    ball = models.CharField(max_length=1000, default=5, null=False)
    class_tiket = models.CharField(choices=tiket_class, null=False)

    def __str__(self):
        return f'{self.Ticket_from} - {self.Ticket_to}'

#
# pay_opition = models.CharField(
#       null=False,
#       choices=payment_choices,
#       help_text=_('You can choices Payment method'),
#       error_messages={'error': 'You dont choices Payment method'}
#   )
