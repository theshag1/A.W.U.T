# Generated by Django 4.2 on 2023-06-22 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0015_alter_ticket_tiket_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='tiket_number',
            field=models.CharField(default=394260),
        ),
    ]
