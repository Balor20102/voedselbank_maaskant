# Generated by Django 4.1.7 on 2023-11-23 08:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("magazijn", "0007_alter_pakket_uitgiftdatum_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pakket",
            name="uitgiftdatum",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 11, 30, 8, 32, 6, 860047, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
