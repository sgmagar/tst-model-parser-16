# Generated by Django 2.2.28 on 2023-05-31 15:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0010_remove_hello_hey"),
    ]

    operations = [
        migrations.AddField(
            model_name="hello",
            name="hey",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
