# Generated by Django 3.2.24 on 2024-02-12 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingsysapp', '0008_auto_20240212_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='usertype',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
