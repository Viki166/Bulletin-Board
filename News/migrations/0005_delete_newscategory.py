# Generated by Django 4.0.5 on 2022-11-25 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0004_newscategory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewsCategory',
        ),
    ]