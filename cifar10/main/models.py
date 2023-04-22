from django.db import models

# Create your models here.


class CorrectedPrediction(models.Model):
    image = models.ImageField(upload_to='images-corrections/')
    predicted_label = models.CharField(max_length=30)
    corrected_label = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)


class Prediction(models.Model):
    image = models.ImageField(upload_to='images-predicted/')
    predicted_label = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
