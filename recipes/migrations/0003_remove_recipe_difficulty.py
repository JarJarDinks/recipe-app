# Generated by Django 4.2.5 on 2023-10-09 20:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0002_recipe_pic"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipe",
            name="difficulty",
        ),
    ]
