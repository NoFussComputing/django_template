# Generated by Django 5.0.6 on 2024-06-05 09:16

import access.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0003_alter_team_organization'),
        ('config_management', '0002_alter_configgroups_options_alter_configgroups_config_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configgrouphosts',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='access.organization', validators=[access.models.TenancyObject.validatate_organization_exists]),
        ),
        migrations.AlterField(
            model_name='configgroups',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='access.organization', validators=[access.models.TenancyObject.validatate_organization_exists]),
        ),
    ]