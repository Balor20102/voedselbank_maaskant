# Generated by Django 4.1.7 on 2023-11-23 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leverancier',
            name='leveringsfrequentie',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
