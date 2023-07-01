# Generated by Django 4.2 on 2023-06-25 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BuyTicket', '0007_buyticket_fly_ball'),
        ('User', '0007_delete_userball'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ball', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ball', to='BuyTicket.buyticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
