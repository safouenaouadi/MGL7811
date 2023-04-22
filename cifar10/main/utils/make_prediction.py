# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np

from PIL import Image


def make_prediction(image):
    model = tf.keras.models.load_model('main/utils/cifar10-validation.h5')
    img = Image.open(image)
    img = img.resize((32, 32))
    labels = '''Airplane Car Bird Cat Deer Dog Frog Horse Ship Truck'''.split()
    # Convert the image to a NumPy array and normalize the pixel values
    img_array = np.array(img) / 255.0

    # Add a batch dimension to the image
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)

    # Get the index of the predicted class
    predicted_class = np.argmax(prediction)
    predicted_label = labels[predicted_class]
    return predicted_label
