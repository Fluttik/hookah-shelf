# Generated by Django 2.2.19 on 2024-03-05 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mixes', '0004_auto_20240305_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='line',
        ),
        migrations.AddField(
            model_name='lines',
            name='line',
            field=models.ForeignKey(default=str, on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='mixes.Company'),
            preserve_default=False,
        ),
    ]
