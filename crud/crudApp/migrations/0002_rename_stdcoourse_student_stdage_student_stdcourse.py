# Generated by Django 5.0 on 2023-12-24 08:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='stdCoourse',
            new_name='stdAge',
        ),
        migrations.AddField(
            model_name='student',
            name='stdCourse',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
