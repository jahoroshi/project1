# Generated by Django 5.0.4 on 2024-05-04 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0008_testsides'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsides',
            name='relation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cards.testsides'),
        ),
    ]
