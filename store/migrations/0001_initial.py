# Generated by Django 4.2 on 2023-06-20 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

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
                    "gender",
                    models.CharField(
                        choices=[("Man", "Man"), ("Woman", "Woman"), ("Kids", "Kids")],
                        default="notSelected",
                        max_length=50,
                    ),
                ),
                ("category_name", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Order",
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
                ("name", models.CharField(max_length=191)),
                ("email", models.EmailField(max_length=254)),
                ("postal_code", models.IntegerField()),
                ("address", models.CharField(max_length=191)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("paid", models.BooleanField(default=False)),
            ],
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
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("XS", "XS"),
                            ("S", "S"),
                            ("M", "M"),
                            ("L", "L"),
                            ("XL", "XL"),
                            ("XXL", "XXL"),
                        ],
                        max_length=200,
                    ),
                ),
                ("description", models.CharField(blank=True, max_length=200)),
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
                (
                    "description",
                    models.TextField(
                        max_length=500, verbose_name="Additional information"
                    ),
                ),
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
                    models.ImageField(
                        blank=True, default=None, upload_to="product_images"
                    ),
                ),
                (
                    "image_2",
                    models.ImageField(
                        blank=True, default=None, upload_to="product_images"
                    ),
                ),
                (
                    "image_3",
                    models.ImageField(
                        blank=True, default=None, upload_to="product_images"
                    ),
                ),
                ("category_name", models.ManyToManyField(to="store.category")),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("size", models.ManyToManyField(to="store.size")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CartItem",
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
                ("quantity", models.IntegerField(default=1, null=True)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="store.product"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]