# Generated by Django 4.2 on 2023-06-25 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0023_alter_ticket_tiket_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='tiket_number',
            field=models.CharField(default=284326),
        ),
    ]
