# Generated by Django 5.0.6 on 2024-06-29 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='guests_can_pause',
            new_name='guest_can_pause',
        ),
    ]