# Generated by Django 5.0.6 on 2024-06-02 14:48

import access.fields
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('access', '0002_alter_team_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigGroups',
            fields=[
                ('is_global', models.BooleanField(default=False)),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('created', access.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('modified', access.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False)),
                ('name', models.CharField(max_length=50)),
                ('config', models.JSONField(blank=True, default=None, null=True)),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='access.organization')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='config_management.configgroups')),
            ],
            options={
                'verbose_name': 'Config Groups',
            },
        ),
    ]