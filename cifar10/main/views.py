from django.shortcuts import render
from .utils.make_prediction import make_prediction
from .models import Prediction, CorrectedPrediction
# Create your views here.
from PIL import Image
from django.conf import settings
import os


def index(request):
    return render(request, 'index.html')


def predict(request):

    if request.method == 'POST':
        image = request.FILES.get('image')
        predicted_label = make_prediction(image)
        prediction = Prediction(image=image, predicted_label=predicted_label)
        prediction.save()
        image_path = prediction.image.url
        request.session['prediction'] = prediction.pk
        # return JsonResponse({'predicted_label': predicted_label})

        return render(request, 'index.html', {"predicted_label": predicted_label, 'image_path': image_path})


def correct(request):
    if request.method == 'POST':

        corrected_label = request.POST['correction']
        prediction = request.session['prediction']
        prediction_to_correct = Prediction.objects.get(pk=prediction)
        prediction_corrected = CorrectedPrediction(
            image=prediction_to_correct.image, predicted_label=prediction_to_correct.predicted_label, corrected_label=corrected_label)
        prediction_corrected.save()
        prediction_to_correct.delete()
        # return JsonResponse({'predicted_label': predicted_label})
        return render(request, 'index.html')
