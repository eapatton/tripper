# Generated by Django 3.0.5 on 2020-04-09 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=250)),
                ('description', models.TextField(max_length=250)),
                ('cost', models.IntegerField()),
                ('hours', models.CharField(max_length=100)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.City')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.TextField(max_length=250)),
                ('budget', models.IntegerField()),
                ('city', models.ManyToManyField(to='main_app.City')),
                ('things_to_do', models.ManyToManyField(to='main_app.Thing')),
            ],
        ),
    ]
