# Generated by Django 3.2.24 on 2024-02-09 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingsysapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='response',
            new_name='response_text',
        ),
        migrations.AddField(
            model_name='feedback',
            name='response_text',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
    ]
