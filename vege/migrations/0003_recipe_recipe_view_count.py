# Generated by Django 5.1.4 on 2025-02-02 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_recipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_view_count',
            field=models.IntegerField(default=1),
        ),
    ]
