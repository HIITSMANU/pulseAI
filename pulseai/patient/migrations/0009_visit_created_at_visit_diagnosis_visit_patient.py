# Generated by Django 5.0.6 on 2024-06-27 05:03

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0008_visit'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visit',
            name='diagnosis',
            field=models.TextField(default=datetime.datetime(2024, 6, 27, 5, 2, 31, 656964, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visit',
            name='patient',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
            preserve_default=False,
        ),
    ]
