# Generated by Django 4.2 on 2023-06-18 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0011_alter_ticket_tiket_number'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BuyTicket', '0004_buyticket_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyticket',
            name='fly',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='fly_ticket', to='Ticket.ticket'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='buyticket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_fly', to=settings.AUTH_USER_MODEL),
        ),
    ]