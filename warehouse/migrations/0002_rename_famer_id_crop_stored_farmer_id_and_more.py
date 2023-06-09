# Generated by Django 4.1.3 on 2023-03-12 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("warehouse", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="crop_stored",
            old_name="famer_id",
            new_name="farmer_id",
        ),
        migrations.RenameField(
            model_name="reservation",
            old_name="famer_id",
            new_name="farmer_id",
        ),
        migrations.RemoveField(
            model_name="warehouse",
            name="phone_number",
        ),
        migrations.AlterField(
            model_name="manager",
            name="phone_number",
            field=models.CharField(max_length=10),
        ),
    ]
