# Generated by Django 4.2.7 on 2024-06-04 06:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0024_alter_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2024, 6, 4), null=True),
        ),
    ]
