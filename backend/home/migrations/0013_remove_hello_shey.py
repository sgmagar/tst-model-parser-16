# Generated by Django 2.2.28 on 2023-06-12 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_hello_shey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hello',
            name='shey',
        ),
    ]
