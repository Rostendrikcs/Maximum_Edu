# Generated by Django 4.2.2 on 2023-07-22 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements81', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisements81',
            name='bu',
            field=models.BooleanField(default=False, help_text='Использовался ли товар', verbose_name='б/у'),
        ),
    ]
