# Generated by Django 2.2.7 on 2019-12-03 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('title_ru', models.CharField(max_length=20, null=True)),
                ('title_uk', models.CharField(max_length=20, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('description_uk', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('title_ru', models.CharField(max_length=20, null=True)),
                ('title_uk', models.CharField(max_length=20, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('description_uk', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блог',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('title_ru', models.CharField(max_length=20, null=True)),
                ('title_uk', models.CharField(max_length=20, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('description_uk', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('title_ru', models.CharField(max_length=20, null=True)),
                ('title_uk', models.CharField(max_length=20, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('description_uk', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Главная',
                'verbose_name_plural': 'Главная',
            },
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('title_ru', models.CharField(max_length=20, null=True)),
                ('title_uk', models.CharField(max_length=20, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('description_uk', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Автопарк',
                'verbose_name_plural': 'Автопарк',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Услуги',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
