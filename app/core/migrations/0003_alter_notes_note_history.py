# Generated by Django 5.0.6 on 2024-05-23 03:59

import access.fields
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_notes_serial_number_alter_notes_device_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='note',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Note'),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('created', access.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('before', models.TextField(blank=True, default=None, help_text='JSON Object before Change', null=True)),
                ('after', models.TextField(blank=True, default=None, help_text='JSON Object After Change', null=True)),
                ('action', models.IntegerField(choices=[('1', 'Create'), ('2', 'Update'), ('3', 'Delete')], default=None, null=True)),
                ('item_pk', models.IntegerField(default=None, null=True)),
                ('item_class', models.CharField(default=None, max_length=50, null=True)),
                ('item_parent_pk', models.IntegerField(default=None, null=True)),
                ('item_parent_class', models.CharField(default=None, max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
