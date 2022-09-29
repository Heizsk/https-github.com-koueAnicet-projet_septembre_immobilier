# Generated by Django 4.1.1 on 2022-09-27 12:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='banner',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='contact',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='otherbanner',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='otherbanner',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='otherbanner',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='siteinfos',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='siteinfos',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='siteinfos',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='sociallinks',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sociallinks',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='sociallinks',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
