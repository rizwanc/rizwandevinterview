# Generated by Django 2.2.3 on 2019-07-23 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20190722_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockquotes',
            name='Change',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='stockquotes',
            name='CurrentPrice',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='stockquotes',
            name='PercentChange',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
