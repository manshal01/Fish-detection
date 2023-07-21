from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input, decode_predictions

# Load the InceptionV3 model pre-trained on ImageNet dataset
model = tf.keras.applications.InceptionV3()

# Define the function to perform prediction on an image
def predict_image():
    # Get the selected image path from the entry field
    image_path = image_path_entry.get()

    # Load the image and resize it to (299, 299)
    img = Image.open(image_path)
    img = img.resize((299, 299))

    # Convert the image to a NumPy array and preprocess it
    img_array = image.img_to_array(img)
    processed_img = preprocess_input(img_array)

    # Use the model to predict the species of fish in the image
    predictions = model.predict(np.array([processed_img]))

    # Decode the predictions and get the top 5 predicted species
    decoded_predictions = decode_predictions(predictions, top=5)[0]

    # Update the result label with the predicted species
    species = "\n".join([f"{name}: {round(score * 100, 2)}%" for (i, name, score) in decoded_predictions])
    result_label.config(text=f"The predicted species of Image is:\n{species}")


# Define the function to perform prediction on a video
def predict_species():
    # Get the selected video path from the entry field
    video_path = video_path_entry.get()

    # TODO: Use the model to predict the species of fish in the video

    # Update the result label with the predicted species
    result_label.config(text="The predicted species of fish is: " + "Nemo")


# Define the function to reset the input fields
def reset_input():
    image_path_entry.delete(0, END)
    video_path_entry.delete(0, END)
    result_label.config(text="")


# Create the main window
window = Tk()
window.title("Fish Species Predictor")
window.geometry("400x400")

# Create the UI elements
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

# Add the UI elements to the window
video_path_entry.pack(pady=10)
select_video_button.pack(pady=10)
image_path_entry.pack(pady=10)
select_image_button.pack(pady=10)

predict_button.pack(pady=10)
predict_image_button.pack(pady=10)
reset_button.pack(pady=10)

result_label.pack(pady=10)

# Run the main event loop
window.mainloop()
