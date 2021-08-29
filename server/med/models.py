from django.db import models

class Questions(models.Model):
    prevQuestion = models.CharField(max_length=1000, blank=True, null=True)
    prevAnswer = models.CharField(max_length=50, blank=True, null=True)
    question = models.CharField(max_length=1000, blank=True, null=True)
    btn0Text = models.CharField(max_length=50, blank=True, null=True)
    btn1Text = models.CharField(max_length=50, blank=True, null=True)
    btn2Text = models.CharField(max_length=50, blank=True, null=True)
    btn0UserText = models.CharField(max_length=100, blank=True, null=True)
    btn1UserText = models.CharField(max_length=100, blank=True, null=True)
    btn2UserText = models.CharField(max_length=100, blank=True, null=True)
    checkSymptom = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        app_label = 'med'

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
