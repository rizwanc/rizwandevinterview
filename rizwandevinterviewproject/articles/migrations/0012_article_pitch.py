# Generated by Django 2.2.3 on 2019-07-24 11:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20190724_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pitch',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
