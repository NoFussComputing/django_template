# Generated by Django 5.0.6 on 2024-06-02 20:51

import access.fields
import config_management.models.groups
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0002_alter_team_organization'),
        ('config_management', '0001_initial'),
        ('itam', '0012_alter_device_serial_number_alter_device_uuid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='configgroups',
            options={},
        ),
        migrations.AlterField(
            model_name='configgroups',
            name='config',
            field=models.JSONField(blank=True, default=None, null=True, validators=[config_management.models.groups.ConfigGroups.validate_config_keys_not_reserved]),
        ),
        migrations.CreateModel(
            name='ConfigGroupHosts',
            fields=[
                ('is_global', models.BooleanField(default=False)),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('created', access.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('modified', access.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config_management.configgroups')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itam.device', validators=[config_management.models.groups.ConfigGroupHosts.validate_host_no_parent_group])),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='access.organization')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
