# Generated by Django 5.1.3 on 2024-11-13 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_trip_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]
