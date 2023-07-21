# Fish-detection
This code is a Python script that creates a graphical user interface (GUI) application using the Tkinter library. The purpose of this application is to predict the species of fish in an image or video. It uses a pre-trained deep learning model called InceptionV3, which is trained on the ImageNet dataset


![Screenshot (17)](https://github.com/manshal01/Fish-detection/assets/93897590/539994a6-67c2-4c0d-87b4-11e548d80883)

Let's go through the code line by line:

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input, decode_predictions
This imports the necessary libraries for the application, including Tkinter for the GUI, PIL (Python Imaging Library) and ImageTk for image processing and display, NumPy for numerical operations, and TensorFlow for the deep learning model.

model = tf.keras.applications.InceptionV3()
This line loads the InceptionV3 model pre-trained on the ImageNet dataset.

![Screenshot (18)](https://github.com/manshal01/Fish-detection/assets/93897590/abb729eb-54fa-40aa-8af5-992fd989be7d)


def predict_image():
    ...
This function is called when the "Predict Image" button is clicked. It performs prediction on an image by first getting the image path from the entry field, loading and resizing the image to (299, 299) using PIL, converting the image to a NumPy array, preprocessing the image using the InceptionV3 preprocessing function, using the InceptionV3 model to predict the species of fish in the image, decoding the predictions to get the top 5 predicted species, and updating the result label with the predicted species.

def predict_species():
    ...
This function is called when the "Predict Species" button is clicked. It is not fully implemented, but it is intended to perform prediction on a video. It gets the video path from the entry field and uses the InceptionV3 model to predict the species of fish in the video. However, the code for this functionality is missing and needs to be added.

![Screenshot (19)](https://github.com/manshal01/Fish-detection/assets/93897590/7e93fa96-5250-4294-a5cf-631028e864c8)


def reset_input():
    ...
This function is called when the "Reset Input" button is clicked. It clears the input fields and updates the result label with an empty string.

window = Tk()
window.title("Fish Species Predictor")
window.geometry("400x400")
These lines create the main window of the GUI and set its title and size.

video_path_entry = Entry(window, width=30)
select_video_button = Button(window, text="Select Video", command=lambda: 
                             video_path_entry.insert(0, filedialog.askopenfilename()))
image_path_entry = Entry(window, width=30)
select_image_button = Button(window, text="Select Image", command=lambda: image_path_entry.insert(
    0, filedialog.askopenfilename()))

predict_button = Button(window, text="Predict Species", width=20,
                        command=predict_species)
predict_image_button = Button(window, text="Predict Image", width=20, command=predict_image)
reset_button = Button(window, text="Reset Input", width=20, command=reset_input)

result_label = Label(window, text="", width=40, height=6, justify="left", anchor="w", font=("Arial", 10))
These lines create the UI elements of the application, including two entry fields for the image and video paths, two buttons for selecting an image or video, two buttons for predicting the species of fish in an image or video, one button for resetting the input fields, and one label for displaying the predicted species.

video_path_entry.pack(pady=10)
select_video_button.pack(pady=10)
image_path_entry.pack(pady=10)
select_image_button.pack(pady=10)

predict_button.pack(pady=10)
These lines of code are packing the user interface elements created earlier using the pack() method. The pack() method is used to organize the widgets in blocks before placing them in the parent widget.

Here, pady=10 is used as an argument to add 10 pixels of vertical padding between each widget.

The first four lines are packing two Entry widgets (video_path_entry and image_path_entry) and two Button widgets (select_video_button and select_image_button) that allow the user to select a video and an image to analyze.

The fifth line is packing a Button widget (predict_button) that will execute the predict_species() function when clicked.

Note that predict_image_button and reset_button are also created earlier in the code, but they are not included in this packing section. This is because they are intended to be used separately from the main prediction button.
