# Generated by Django 3.2.18 on 2023-07-24 09:15

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("django_outbox_pattern", "0004_auto_20230403_1637"),
    ]

    operations = [
        migrations.AddField(
            model_name="published",
            name="headers",
            field=models.JSONField(default=dict),
        ),
    ]
