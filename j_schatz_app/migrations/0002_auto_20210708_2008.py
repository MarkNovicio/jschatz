# Generated by Django 2.2 on 2021-07-09 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('j_schatz_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermessage',
            old_name='name',
            new_name='username',
        ),
    ]
