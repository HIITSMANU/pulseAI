# Generated by Django 5.0.6 on 2024-06-24 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_alter_heartvital_fastingbs_alter_heartvital_maxhr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heartvital',
            name='FastingBS',
            field=models.CharField(choices=[('0', 'less than or equal to 120'), ('1', 'More than to 120')], max_length=20, verbose_name='Fasting Blood Pressure (60-900)'),
        ),
        migrations.AlterField(
            model_name='heartvital',
            name='MaxHR',
            field=models.IntegerField(verbose_name='Maximum Heart Rate (60-220)'),
        ),
        migrations.AlterField(
            model_name='heartvital',
            name='Oldpeak',
            field=models.FloatField(verbose_name='Old peak(-2.5 - +2.5)'),
        ),
        migrations.AlterField(
            model_name='heartvital',
            name='RestingBP',
            field=models.IntegerField(verbose_name='Resting Blood Pressure (60-220)'),
        ),
    ]