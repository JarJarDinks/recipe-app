# Generated by Django 4.2.5 on 2023-10-20 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0004_instruction_recipe_instructions"),
    ]

    operations = [
        migrations.AddField(
            model_name="instruction",
            name="recipe",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="recipes.recipe",
            ),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="instructions",
            field=models.ManyToManyField(
                related_name="recipes", to="recipes.instruction"
            ),
        ),
    ]
