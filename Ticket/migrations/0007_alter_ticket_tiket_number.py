# Generated by Django 4.2 on 2023-06-17 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0006_alter_ticket_tiket_number_alter_ticket_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='tiket_number',
            field=models.CharField(default=203626),
        ),
    ]