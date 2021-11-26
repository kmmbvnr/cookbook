# Generated by Django 3.1 on 2020-12-14 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "stage",
                    models.IntegerField(
                        choices=[
                            (1, "New"),
                            (2, "Approved"),
                            (3, "Rejected"),
                            (4, "Published"),
                            (5, "Hidden"),
                            (6, "Removed"),
                        ]
                    ),
                ),
                ("published", models.DateTimeField(blank=True, null=True)),
                ("title", models.CharField(max_length=250)),
                ("text", models.TextField()),
                ("comment", models.TextField(blank=True, null=True)),
                (
                    "approver",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReviewChangeLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("changed", models.DateTimeField(default=django.utils.timezone.now)),
                ("source", models.IntegerField()),
                ("target", models.IntegerField()),
                ("ip_address", models.GenericIPAddressField(blank=True, null=True)),
                ("diff", models.TextField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "review",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="review.review"
                    ),
                ),
            ],
        ),
    ]
