# Generated by Django 4.1.1 on 2022-10-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_siteinfos_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='slide_1',
            field=models.ImageField(blank=True, null=True, upload_to='slide_1'),
        ),
        migrations.AddField(
            model_name='banner',
            name='slide_2',
            field=models.ImageField(blank=True, null=True, upload_to='slide_2'),
        ),
        migrations.AddField(
            model_name='banner',
            name='slide_3',
            field=models.ImageField(blank=True, null=True, upload_to='slide_3'),
        ),
    ]
