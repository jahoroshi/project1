# Generated by Django 5.0.4 on 2024-04-25 19:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side1', models.CharField(max_length=255)),
                ('side2', models.CharField(max_length=255)),
                ('transcription', models.CharField(max_length=255)),
                ('audio', models.URLField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('login', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mappings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repetition', models.IntegerField(default='0')),
                ('status', models.IntegerField(default='0')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.cards')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.categories')),
            ],
        ),
        migrations.AddField(
            model_name='categories',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cards.users'),
        ),
    ]
