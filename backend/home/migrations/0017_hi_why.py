# Generated by Django 2.2.28 on 2023-06-13 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_remove_hi_why'),
    ]

    operations = [
        migrations.AddField(
            model_name='hi',
            name='why',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
