# Generated by Django 2.2.19 on 2024-03-05 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixes', '0006_auto_20240305_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lines',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Линейка'),
        ),
    ]
