# Generated by Django 4.2.4 on 2024-01-21 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('JPad', '0004_todo_debt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='debt',
            old_name='username',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='username',
            new_name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.TextField(),
        ),
    ]
