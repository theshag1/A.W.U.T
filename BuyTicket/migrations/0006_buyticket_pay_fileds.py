# Generated by Django 4.2 on 2023-06-18 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BuyTicket', '0005_buyticket_fly_alter_buyticket_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyticket',
            name='pay_fileds',
            field=models.CharField(choices=[('Uzcard/Humo (UZS)', 'Uzs humo'), ('Uzcard(Corparate) (UZS)', 'Uzs corparate'), ('Visa/Mastercard (USD)', 'Visa master usd'), ('Another card Payment ()', 'another')], default=1, error_messages={'error': 'You dont select payment information'}, help_text='Please select your payment information '),
            preserve_default=False,
        ),
    ]