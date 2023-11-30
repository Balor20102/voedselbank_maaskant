# Generated by Django 4.1.7 on 2023-11-22 12:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("magazijn", "0004_alter_pakket_uitgiftdatum"),
    ]

    operations = [
        migrations.AddField(
            model_name="pakket",
            name="status",
            field=models.IntegerField(
                choices=[(1, "opgehaald"), (2, "niet opgehaald")], default=1
            ),
        ),
        migrations.AlterField(
            model_name="pakket",
            name="uitgiftdatum",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 11, 29, 12, 28, 8, 202854, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
