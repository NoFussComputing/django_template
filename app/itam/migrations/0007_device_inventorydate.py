# Generated by Django 5.0.6 on 2024-05-20 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itam', '0006_alter_devicesoftware_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='inventorydate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Last Inventory Date'),
        ),
    ]
