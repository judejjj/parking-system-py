# Generated by Django 3.2.24 on 2024-02-12 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkingsysapp', '0011_auto_20240212_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='usertype',
        ),
    ]
