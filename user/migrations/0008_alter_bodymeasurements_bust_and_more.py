# Generated by Django 4.2 on 2023-06-19 18:02

from django.db import migrations, models
import validators


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0007_bodymeasurements_last_updated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bodymeasurements",
            name="bust",
            field=models.PositiveIntegerField(
                blank=True, max_length=10, null=True, verbose_name="Bust"
            ),
        ),
        migrations.AlterField(
            model_name="bodymeasurements",
            name="chest",
            field=models.PositiveIntegerField(
                blank=True, max_length=10, null=True, verbose_name="Chest"
            ),

        ),
        migrations.AlterField(
            model_name="bodymeasurements",
            name="neck",
            field=models.PositiveIntegerField(
                blank=True, max_length=10, null=True, verbose_name="Neck"
            ),
        ),
        migrations.AlterField(
            model_name="bodymeasurements",
            name="shoulder",
            field=models.PositiveIntegerField(
                blank=True, max_length=10, null=True, verbose_name="Shoulder"
            ),
        ),
        migrations.AlterField(
            model_name="bodymeasurements",
            name="shoulder_to_floor",
            field=models.PositiveIntegerField(
                blank=True, max_length=10, null=True, verbose_name="Shoulder to floor"
            ),
        ),
        migrations.AlterField(
            model_name="bodymeasurements",
            name="shoulder_to_waist",
            field=models.PositiveIntegerField(
                blank=True, max_length=10, null=True, verbose_name="Shoulder to waist"
            ),
        ),
        migrations.AlterField(
            model_name="bodymeasurements",
            name="sleeve",
            field=models.PositiveIntegerField(
                blank=True, max_length=10, null=True, verbose_name="Sleeve"
            ),
        ),
        migrations.AlterField(
            model_name="bodymeasurements",
            name="waist",
            field=models.PositiveIntegerField(
                blank=True, max_length=10, null=True, verbose_name="Waist"
            ),
        ),
    ]
