from django.db import models

class Symptoms(models.Model):
    disease = models.CharField(max_length=100, blank=True, null=True)
    symptom_1 = models.CharField(max_length=100, blank=True, null=True)
    symptom_2 = models.CharField(max_length=100, blank=True, null=True)
    symptom_3 = models.CharField(max_length=100, blank=True, null=True)
    symptom_4 = models.CharField(max_length=100, blank=True, null=True)
    symptom_5 = models.CharField(max_length=100, blank=True, null=True)
    symptom_6 = models.CharField(max_length=100, blank=True, null=True)
    symptom_7 = models.CharField(max_length=100, blank=True, null=True)
    symptom_8 = models.CharField(max_length=100, blank=True, null=True)
    symptom_9 = models.CharField(max_length=100, blank=True, null=True)
    symptom_10 = models.CharField(max_length=100, blank=True, null=True)
    symptom_11 = models.CharField(max_length=100, blank=True, null=True)
    symptom_12 = models.CharField(max_length=100, blank=True, null=True)
    symptom_13 = models.CharField(max_length=100, blank=True, null=True)
    symptom_14 = models.CharField(max_length=100, blank=True, null=True)
    symptom_15 = models.CharField(max_length=100, blank=True, null=True)
    symptom_16 = models.CharField(max_length=100, blank=True, null=True)
    symptom_17 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'symptoms'
        app_label = 'med'
