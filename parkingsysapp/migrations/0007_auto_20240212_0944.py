# Generated by Django 3.2.24 on 2024-02-12 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkingsysapp', '0006_user_usertype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='fresponse_text',
        ),
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
