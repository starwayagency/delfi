# Generated by Django 2.2.7 on 2019-12-15 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191209_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='direction',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=10, max_digits=9, null=True),
        ),
    ]