# Generated by Django 4.2.4 on 2024-07-25 06:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactus",
            name="saveimg",
            field=models.ImageField(blank=True, null=True, upload_to="contactimage"),
        ),
    ]