# Generated by Django 3.0.5 on 2020-06-19 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('value', models.BooleanField(verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Option',
                'verbose_name_plural': 'Options',
            },
        ),
        migrations.CreateModel(
            name='Push',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created date')),
                ('push_date', models.DateField(verbose_name='Push date')),
                ('pushed', models.BooleanField(verbose_name='Pushed')),
                ('count', models.PositiveSmallIntegerField(verbose_name='Push count')),
            ],
            options={
                'verbose_name': 'Push',
                'verbose_name_plural': 'Pushes',
            },
        ),
    ]
