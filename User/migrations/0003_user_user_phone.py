# Generated by Django 4.2 on 2023-06-22 07:26

from django.db import migrations, models
import validate


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_alter_user_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_phone',
            field=models.CharField(default='+99890*******', help_text='You must be enter phone number', max_length=18, validators=[validate.phone_validate]),
            preserve_default=False,
        ),
    ]