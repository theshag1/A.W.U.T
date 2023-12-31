# Generated by Django 4.2 on 2023-06-25 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BuyTicket', '0007_buyticket_fly_ball'),
        ('User', '0008_userball'),
    ]

    operations = [
        migrations.AddField(
            model_name='userball',
            name='ticket',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ball', to='BuyTicket.buyticket'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userball',
            name='ball',
            field=models.CharField(),
        ),
    ]
