# Generated by Django 4.2 on 2023-06-07 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_alter_bodymeasurements_bust_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bodymeasurements",
            name="bust",
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="bodymeasurements",
            name="chest",
            field=models.FloatField(
                blank=True, max_length=10, null=True, verbose_name="Chest"
            ),
        ),
        migrations.AlterField(
            model_name="bodymeasurements",
            name="comment",
            field=models.TextField(
                blank=True,
                max_length=250,
                null=True,
                verbose_name="Additional information",
            ),
        ),
        migrations.AlterField(
            model_name="bodymeasurements",
            name="hips",
            field=models.FloatField(
                blank=True, max_length=10, null=True, verbose_name="Hips"
            ),
        ),
        migrations.AlterField(
            model_name="bodymeasurements",
            name="last_updated",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="bodymeasurements",
            name="measure_model",
            field=models.ImageField(
                blank=True, default="body_measurements.jpg", null=True, upload_to=""
            ),
        ),
        migrations.AlterField(
            model_name="bodymeasurements",
            name="neck",
            field=models.FloatField(
                blank=True, max_length=10, null=True, verbose_name="Neck"
            ),
        ),
        migrations.AlterField(
            model_name="bodymeasurements",
            name="shoulder",
            field=models.FloatField(
                blank=True, max_length=10, null=True, verbose_name="Shoulder"
            ),
        ),
        migrations.AlterField(
            model_name="bodymeasurements",
            name="shoulder_to_floor",
            field=models.FloatField(
                blank=True, max_length=10, null=True, verbose_name="Shoulder to floor"
            ),
        ),
        migrations.AlterField(
            model_name="bodymeasurements",
            name="shoulder_to_waist",
            field=models.FloatField(
                blank=True, max_length=10, null=True, verbose_name="Shoulder to waist"
            ),
        ),
        migrations.AlterField(
            model_name="bodymeasurements",
            name="sleeve",
            field=models.FloatField(
                blank=True, max_length=10, null=True, verbose_name="Sleeve"
            ),
        ),
        migrations.AlterField(
            model_name="bodymeasurements",
            name="waist",
            field=models.FloatField(
                blank=True, max_length=10, null=True, verbose_name="Waist"
            ),
        ),
    ]