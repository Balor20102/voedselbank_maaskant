# Generated by Django 4.1.7 on 2023-11-27 08:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("magazijn", "0012_alter_pakket_aangemaakt_op_alter_pakket_uitgiftdatum"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pakket",
            name="aangemaakt_op",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="pakket",
            name="uitgiftdatum",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 12, 4, 8, 41, 23, 595356, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
