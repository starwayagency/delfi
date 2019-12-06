# Generated by Django 2.2.7 on 2019-12-04 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buscontact',
            options={'verbose_name': 'Заказ Микроавтобуса', 'verbose_name_plural': 'Заказы Микроавтобуса'},
        ),
        migrations.AlterModelOptions(
            name='europecontact',
            options={'verbose_name': 'Заказ поездки в Европу', 'verbose_name_plural': 'Заказы поездок в Европу'},
        ),
        migrations.RemoveField(
            model_name='payment',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='payment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создан'),
        ),
        migrations.AddField(
            model_name='payment',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлен'),
        ),
        migrations.AlterField(
            model_name='buscontact',
            name='comment',
            field=models.TextField(verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='buscontact',
            name='peoples',
            field=models.IntegerField(verbose_name='Количество людей'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='comment',
            field=models.TextField(verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='europecontact',
            name='comment',
            field=models.TextField(verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='europecontact',
            name='peoples',
            field=models.IntegerField(verbose_name='Людей'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='currency',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='ip',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='IP'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='sender_card_bank',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Банк'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='sender_card_country',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='sender_card_mask2',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Маска карты'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='sender_card_type',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='sender_first_name',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='sender_last_name',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='sender_phone',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Статус'),
        ),
    ]