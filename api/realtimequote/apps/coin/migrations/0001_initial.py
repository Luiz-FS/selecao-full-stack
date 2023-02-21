# Generated by Django 4.1.7 on 2023-02-17 20:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Coin",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=30, unique=True)),
                ("description", models.CharField(max_length=250)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
