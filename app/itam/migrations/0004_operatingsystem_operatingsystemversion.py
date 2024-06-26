# Generated by Django 5.0.6 on 2024-05-18 08:51

import access.fields
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0001_initial'),
        ('itam', '0003_devicesoftware_version'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('is_global', models.BooleanField(default=False)),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('created', access.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('modified', access.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', access.fields.AutoSlugField()),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='access.organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OperatingSystemVersion',
            fields=[
                ('is_global', models.BooleanField(default=False)),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('created', access.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('modified', access.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False)),
                ('name', models.CharField(max_length=50)),
                ('operating_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itam.operatingsystem')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='access.organization')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
