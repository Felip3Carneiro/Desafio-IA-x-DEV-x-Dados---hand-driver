import os
from tensorflow.keras.models import load_model # type: ignore # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np
import threading

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("E:\\vscode\\Python\\Cool-projects\\Carro-mao\\code\\camera\\keras_model.h5", compile=False)

# Load the labels
class_names = open("E:\\vscode\\Python\\Cool-projects\\Carro-mao\\code\\camera\\labels.txt", "r").readlines()

# CAMERA can be 0 -> Default camera or 1 -> OBS based on default camera of your computer
camera = cv2.VideoCapture(0)

os.system("cls")  # Roda o comando cls

#variáveis
class_name = ""
confidence_score = 0

def process():
    global class_name, confidence_score
    while True:
        # Grab the webcamera's image.
        ret, image = camera.read()

        # If frame not captured, wait and continue
        if not ret or image is None:
            # small sleep to avoid busy loop
            cv2.waitKey(10)
            continue

        # Resize the raw image into (224-height,224-width) pixels
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

        # Show the image in a window
        cv2.imshow("Webcam Image", image)

        # Make the image a numpy array and reshape it to the models input shape.
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normalize the image array
        image = (image / 127.5) - 1

        # Predicts the model
        prediction = model.predict(image)
        index = np.argmax(prediction)
        class_name = class_names[index].strip()
        confidence_score = float(prediction[0][index])

        # Print prediction and confidence score
        print(f"Class: {class_name[2:]}")
        print(f"Confidence Score: {int(np.round(confidence_score * 100))}%")
        print("Github:")
        print("\033[4A\033[J", end="")

        # Listen to the keyboard for presses.
        keyboard_input = cv2.waitKey(1) & 0xFF

        # 27 is the ASCII for the esc key on your keyboard.
        if keyboard_input == 27:
            break

    # cleanup when loop exits
    camera.release()
    cv2.destroyAllWindows()

camera_thread = threading.Thread(target=process, daemon=True)
camera_thread.start()