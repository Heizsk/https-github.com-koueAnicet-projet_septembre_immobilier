# Generated by Django 4.1.1 on 2022-10-14 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_banner_active_alter_contact_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinfos',
            name='body_image',
            field=models.ImageField(null=True, upload_to='body_image'),
        ),
    ]
