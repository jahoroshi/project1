# Generated by Django 5.0.4 on 2024-05-24 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0022_alter_mappings_study_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='audio',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
