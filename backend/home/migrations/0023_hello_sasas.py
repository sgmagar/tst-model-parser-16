# Generated by Django 2.2.28 on 2023-07-19 16:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0022_remove_hello_ssssdsd"),
    ]

    operations = [
        migrations.AddField(
            model_name="hello",
            name="sasas",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
