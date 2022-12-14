# Generated by Django 4.0.5 on 2022-06-28 13:45

import ckeditor_uploader.fields
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
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=225, verbose_name='Заголовок')),
                ('content_upload', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текстовое поле')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ads.ad')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ads.users')),
            ],
            options={
                'verbose_name': 'Отклик',
                'verbose_name_plural': 'Отклики',
            },
        ),
        migrations.AddField(
            model_name='ad',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ads.category'),
        ),
        migrations.AddField(
            model_name='ad',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ads.game'),
        ),
        migrations.AddField(
            model_name='ad',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ads.users'),
        ),
    ]
