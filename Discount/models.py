from django.db import models


# Create your models here.


class Discount(models.Model):
    ticket = models.ForeignKey('Ticket.Ticket', on_delete=models.CASCADE, related_name='discount_tickets')
    percentage = models.CharField(max_length=100, null=False)
    old_price = models.CharField(null=False)
    discount_price = models.CharField()


