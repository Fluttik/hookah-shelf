# Generated by Django 2.2.19 on 2024-03-07 10:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixes', '0009_auto_20240306_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mixes',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='mixes',
            name='tobaccos',
            field=models.ManyToManyField(db_index=True, through='mixes.MixesTobacco', to='mixes.Tobacco', verbose_name='Табаки'),
        ),
        migrations.AlterField(
            model_name='mixestobacco',
            name='amount',
            field=models.PositiveSmallIntegerField(default=50, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Процент'),
        ),
    ]
