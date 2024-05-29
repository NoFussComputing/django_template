# Generated by Django 5.0.6 on 2024-05-25 02:42

import access.fields
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0002_alter_team_organization'),
        ('settings', '0003_create_settings_for_all_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppSettings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('created', access.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('modified', access.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False)),
                ('software_is_global', models.BooleanField(default=False, verbose_name='All Software is global')),
                ('global_organization', models.ForeignKey(blank=True, default=None, help_text='Organization global items will be created in', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='global_organization', to='access.organization')),
                ('owner_organization', models.ForeignKey(blank=True, default=None, help_text='Organization the settings belong to', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner_organization', to='access.organization')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
