# Generated by Django 2.2 on 2021-07-11 01:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('j_schatz_app', '0003_auto_20210710_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermessage',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
