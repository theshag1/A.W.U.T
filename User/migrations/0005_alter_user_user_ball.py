# Generated by Django 4.2 on 2023-06-22 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_alter_user_user_ball'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_ball',
            field=models.CharField(default=0, help_text='You collect ball next you change your ball to someone our  items'),
        ),
    ]
