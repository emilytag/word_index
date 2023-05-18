# Generated by Django 4.2.1 on 2023-05-18 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wordindex',
            name='line_number',
        ),
        migrations.AddField(
            model_name='wordindex',
            name='index_data',
            field=models.JSONField(default=dict),
        ),
    ]
