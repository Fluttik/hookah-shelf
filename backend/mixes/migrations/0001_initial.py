# Generated by Django 2.2.19 on 2024-03-01 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название компании производителя')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Flavor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Аромат')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Аромат',
                'verbose_name_plural': 'Ароматы',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Mixes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Микс')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mix', to=settings.AUTH_USER_MODEL, verbose_name='Автор микса')),
            ],
            options={
                'verbose_name': 'Микс',
                'verbose_name_plural': 'Миксы',
            },
        ),
        migrations.CreateModel(
            name='Strength',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Крепкость')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Крепость',
                'verbose_name_plural': 'Крепость',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Tobacco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tobacco_line', models.CharField(db_index=True, max_length=100, verbose_name='Линейка табака')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание табака')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mixes.Company')),
                ('flavor', models.ManyToManyField(db_index=True, related_name='mixes', to='mixes.Flavor')),
                ('strength', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mixes', to='mixes.Strength')),
            ],
            options={
                'verbose_name': 'Табак',
                'verbose_name_plural': 'Табаки',
                'ordering': ('company', 'tobacco_line', 'name'),
            },
        ),
        migrations.CreateModel(
            name='MixesTobacco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(verbose_name='Процент')),
                ('mix', models.ForeignKey(help_text='Микс', on_delete=django.db.models.deletion.CASCADE, related_name='mix_tobacco', to='mixes.Mixes', verbose_name='Микс')),
                ('tobacco', models.ForeignKey(help_text='Табак', on_delete=django.db.models.deletion.CASCADE, to='mixes.Tobacco', verbose_name='Табак')),
            ],
        ),
        migrations.AddField(
            model_name='mixes',
            name='tobaccos',
            field=models.ManyToManyField(db_index=True, through='mixes.MixesTobacco', to='mixes.Tobacco'),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tobacco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mixes.Tobacco', verbose_name='Избранный табак')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Избранное',
                'verbose_name_plural': 'Избранное',
            },
        ),
    ]
