# Generated by Django 5.1.4 on 2025-01-26 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=300)),
                ('speed', models.IntegerField(default=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
