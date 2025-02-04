# Generated by Django 5.0.4 on 2024-05-17 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scan_date', models.DateField()),
                ('scan_year', models.IntegerField()),
                ('application', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=255)),
                ('primary_location', models.CharField(max_length=255)),
                ('line_number', models.IntegerField()),
                ('component_full_filename', models.CharField(max_length=255)),
                ('criticality', models.CharField(max_length=50)),
                ('app_priority', models.CharField(max_length=20)),
                ('adjusted_criticality', models.CharField(max_length=20)),
                ('manager_remediation', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
                ('sla_remediation', models.CharField(max_length=50)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('seguimiento', models.TextField()),
            ],
        ),
    ]
