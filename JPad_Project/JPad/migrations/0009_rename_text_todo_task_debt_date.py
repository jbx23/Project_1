# Generated by Django 4.2.4 on 2024-01-27 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JPad', '0008_profile_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='text',
            new_name='task',
        ),
        migrations.AddField(
            model_name='debt',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
