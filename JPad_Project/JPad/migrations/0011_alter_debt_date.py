# Generated by Django 4.2.4 on 2024-01-27 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JPad', '0010_alter_debt_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
