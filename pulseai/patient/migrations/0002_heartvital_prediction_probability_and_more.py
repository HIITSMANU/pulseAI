# Generated by Django 5.0.6 on 2024-06-24 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='heartvital',
            name='prediction_probability',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='heartvital',
            name='HeartDisease',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
