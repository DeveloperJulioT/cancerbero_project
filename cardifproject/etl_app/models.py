from django.db import models

# Create your models here.

class HistoricoVulnerabilidadesFortify(models.Model):
    scan_date = models.DateField()
    scan_year = models.IntegerField()
    application = models.CharField(max_length=100)
    category = models.CharField(max_length=255)
    primary_location = models.CharField(max_length=255)
    line_number = models.IntegerField()
    component_full_filename = models.CharField(max_length=255)
    criticality = models.CharField(max_length=50)
    app_priority = models.CharField(max_length=20)
    adjusted_criticality = models.CharField(max_length=20)
    manager_remediation = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    sla_remediation = models.CharField(max_length=50)
    date_start = models.DateField()
    date_end = models.DateField()
    seguimiento = models.TextField()