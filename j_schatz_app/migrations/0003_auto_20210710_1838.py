# Generated by Django 2.2 on 2021-07-11 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('j_schatz_app', '0002_auto_20210708_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessage',
            name='message',
            field=models.TextField(),
        ),
    ]
