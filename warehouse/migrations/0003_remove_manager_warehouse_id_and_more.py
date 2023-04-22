# Generated by Django 4.0.1 on 2023-04-22 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_rename_famer_id_crop_stored_farmer_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='warehouse_id',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='crop_id',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='farmer_id',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='warehouse_id',
        ),
        migrations.DeleteModel(
            name='Crop_stored',
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
        migrations.DeleteModel(
            name='Warehouse',
        ),
    ]