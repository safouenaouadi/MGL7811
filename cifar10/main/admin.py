from django.contrib import admin
from .models import CorrectedPrediction, Prediction
# Register your models here.
from django.utils.html import format_html


class correctedPredictionAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'predicted_label',
                    'corrected_label', 'created_at')

    def image_tag(self, obj):
        return format_html("<img src='{}' width='250px'  heigh='100px'/>".format(obj.image.url))
    image_tag.short_description = 'Image'


class predictionAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html("<img src='{}' width='250px'  heigh='100px'/>".format(obj.image.url))
    image_tag.short_description = 'Image'

    list_display = ('image_tag', 'predicted_label', 'created_at')


admin.site.register(CorrectedPrediction, correctedPredictionAdmin)

admin.site.register(Prediction, predictionAdmin)
