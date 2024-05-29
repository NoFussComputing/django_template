# Generated by Django 5.0.6 on 2024-05-23 10:58

import access.fields
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0002_alter_team_organization'),
        ('core', '0004_notes_is_null'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('is_global', models.BooleanField(default=False)),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('created', access.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('modified', access.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', access.fields.AutoSlugField()),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='access.organization')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
