# Generated by Django 2.2.3 on 2019-07-22 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo_main',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
    ]
