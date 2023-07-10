# Generated by Django 4.2 on 2023-07-03 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
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
                ("title", models.CharField(max_length=200, verbose_name="Service")),
                (
                    "price",
                    models.FloatField(
                        null=True,
                        validators=[validators.validate_positive],
                        verbose_name="Price",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderReview",
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
                    "date_created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Date"),
                ),
                ("content", models.TextField(max_length=5000, verbose_name="Text")),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="service.service",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Review",
                "verbose_name_plural": "Reviews",
                "ordering": ["-date_created"],
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
                ("date", models.DateTimeField(auto_now_add=True, verbose_name="Date")),
                ("quantity", models.IntegerField(verbose_name="Quantity")),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Pending", "Pending"),
                            ("Accepted", "Accepted"),
                            ("In progress", "In progress"),
                            ("Shipped", "Shipped"),
                            ("Completed", "Completed"),
                            ("Cancelled", "Cancelled"),
                            ("Refunded", "Refunded"),
                        ],
                        default="Pending",
                        max_length=200,
                        verbose_name="Status",
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="service.service",
                        verbose_name="Service",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
