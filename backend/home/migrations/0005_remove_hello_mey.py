# Generated by Django 2.2.28 on 2023-05-30 16:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_hello_mey"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="hello",
            name="mey",
        ),
    ]
