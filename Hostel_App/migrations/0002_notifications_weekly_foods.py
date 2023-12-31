# Generated by Django 4.2.7 on 2023-12-17 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hostel_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Weekly_Foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10)),
                ('breakfast', models.CharField(max_length=50)),
                ('lunch', models.CharField(max_length=50)),
                ('dinner', models.CharField(max_length=50)),
            ],
        ),
    ]
