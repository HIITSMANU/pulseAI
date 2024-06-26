# Generated by Django 5.0.6 on 2024-06-24 06:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HeartVital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Age', models.IntegerField()),
                ('Sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=20)),
                ('ChestPainType', models.CharField(choices=[('TA', 'Typical Angina'), ('ATA', 'Atypical Angina'), ('NAP', 'Non-Anginal Pain'), ('ASY', 'Asymptomatic')], max_length=20)),
                ('RestingBP', models.IntegerField()),
                ('Cholesterol', models.IntegerField()),
                ('FastingBS', models.CharField(choices=[('0', 'less than or equal to 120'), ('1', 'More than to 120')], max_length=20)),
                ('RestingECG', models.CharField(choices=[('Normal', 'Normal'), ('ST', 'having ST-T wave abnormality'), ('LVH', "showing probable or definite left ventricular hypertrophy by Estes' criteria")], max_length=20)),
                ('MaxHR', models.IntegerField()),
                ('ExerciseAngina', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=20)),
                ('Oldpeak', models.FloatField()),
                ('ST_Slope', models.CharField(choices=[('Up', 'upsloping'), ('Flat', 'flat'), ('Down', 'downsloping')], max_length=20)),
                ('HeartDisease', models.CharField(choices=[('1', 'heart disease'), ('0', 'Normal')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
