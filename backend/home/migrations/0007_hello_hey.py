# Generated by Django 2.2.28 on 2023-05-30 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_hello_hey'),
    ]

    operations = [
        migrations.AddField(
            model_name='hello',
            name='hey',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]