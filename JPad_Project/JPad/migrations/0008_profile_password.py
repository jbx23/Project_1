# Generated by Django 4.2.4 on 2024-01-25 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JPad', '0007_alter_profile_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
