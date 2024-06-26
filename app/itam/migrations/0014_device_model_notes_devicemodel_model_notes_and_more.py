# Generated by Django 5.0.6 on 2024-06-11 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itam', '0013_alter_device_organization_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='model_notes',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='devicemodel',
            name='model_notes',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='deviceoperatingsystem',
            name='model_notes',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='devicesoftware',
            name='model_notes',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='devicetype',
            name='model_notes',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='operatingsystem',
            name='model_notes',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='operatingsystemversion',
            name='model_notes',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='software',
            name='model_notes',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='softwarecategory',
            name='model_notes',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='softwareversion',
            name='model_notes',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
