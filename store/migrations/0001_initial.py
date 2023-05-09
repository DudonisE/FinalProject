# Generated by Django 4.2 on 2023-05-04 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category_name",
                    models.CharField(
                        choices=[("Man", "Man"), ("Woman", "Woman"), ("Kids", "Kids")],
                        max_length=50,
                    ),
                ),
                ("description", models.CharField(max_length=500)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Size",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("color", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=500)),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "discount_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "image_1",
                    models.ImageField(default=None, upload_to="product_images"),
                ),
                (
                    "image_2",
                    models.ImageField(default=None, upload_to="product_images"),
                ),
                (
                    "image_3",
                    models.ImageField(default=None, upload_to="product_images"),
                ),
                ("category_name", models.ManyToManyField(to="store.category")),
                ("size", models.ManyToManyField(to="store.size")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]