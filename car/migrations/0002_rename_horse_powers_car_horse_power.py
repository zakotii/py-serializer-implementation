# Generated by Django 4.1 on 2024-12-17 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("car", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="car",
            old_name="horse_powers",
            new_name="horse_power",
        ),
    ]