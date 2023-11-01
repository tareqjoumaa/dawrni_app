# Generated by Django 4.2.6 on 2023-10-27 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dawrni_app', '0004_alter_company_about_alter_company_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='about',
        ),
        migrations.RemoveField(
            model_name='company',
            name='address',
        ),
        migrations.RemoveField(
            model_name='company',
            name='licence',
        ),
        migrations.RemoveField(
            model_name='company',
            name='name',
        ),
        migrations.AddField(
            model_name='company',
            name='about_ar',
            field=models.TextField(default=None, verbose_name='About (Arabic)'),
        ),
        migrations.AddField(
            model_name='company',
            name='about_en',
            field=models.TextField(default=None, verbose_name='About (English)'),
        ),
        migrations.AddField(
            model_name='company',
            name='address_ar',
            field=models.TextField(default=None, verbose_name='Address (Arabic)'),
        ),
        migrations.AddField(
            model_name='company',
            name='address_en',
            field=models.TextField(default=None, verbose_name='Address (English)'),
        ),
        migrations.AddField(
            model_name='company',
            name='name_ar',
            field=models.CharField(default=None, max_length=255, verbose_name='Name (Arabic)'),
        ),
        migrations.AddField(
            model_name='company',
            name='name_en',
            field=models.CharField(default=None, max_length=255, verbose_name='Name (English)'),
        ),
    ]
