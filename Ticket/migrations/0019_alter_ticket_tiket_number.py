# Generated by Django 4.2 on 2023-06-22 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0018_alter_ticket_tiket_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='tiket_number',
            field=models.CharField(default=801338),
        ),
    ]
