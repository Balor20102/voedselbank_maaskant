# Generated by Django 4.1.7 on 2023-11-30 08:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "magazijn",
            "0017_alter_pakket_uitgiftdatum_alter_product_varkesvlees_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="pakket",
            name="uitgiftdatum",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 12, 7, 8, 40, 40, 483737, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]