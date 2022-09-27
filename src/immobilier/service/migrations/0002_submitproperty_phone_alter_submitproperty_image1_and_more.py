# Generated by Django 4.1.1 on 2022-09-27 17:46

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submitproperty',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default=4546565657, max_length=128, region='CI'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='submitproperty',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='img1'),
        ),
        migrations.AlterField(
            model_name='submitproperty',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='img2'),
        ),
        migrations.AlterField(
            model_name='submitproperty',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='img3'),
        ),
        migrations.AlterField(
            model_name='submitproperty',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='img4'),
        ),
        migrations.AlterField(
            model_name='submitproperty',
            name='videos2',
            field=models.ImageField(blank=True, null=True, upload_to='videos2'),
        ),
    ]
