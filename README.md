# Programming drone in Raspberry Pi with basic autonomous control

This project is built as a learning experience for prototyping an autonomous drone.

## Tech stack:
 * Python
 * Jupyter notebook
 * Google-colab (optional)
 * Open CV
 * tensorflow
 * YOLO

## Subfields of AI:
1. Computer vision
2. Deep learning
 
## Purpose:
1. Build and program a drone with basic autonomous abilities
2. learning about the technology behind autonomous drone building and programming
3. understand the basic role of AI in autonomous vehicle engineering

## Components:
1. Raspberry Pi zero/2/3/4/5 - onboard computer for decision making
2. Drone Frame
3. Propellers and motors 
4. flight controller unit (APM, Pixhawk)
5. battery unit
6. GPS module
7. ESC

## Controlling from PC:
This require a strong WiFi connection with the drone. (pi-zero and model 2 are not WiFI enabled)
Download and intall the Raspberry pi OS in the computer unit. It is an open-source linux-based free OS. 
The basic control procedures are:
1. motor_control.py - controlling the motors of the drones 
2. move_drones.py - liftoff and moving the drone
3. rotate_drone.py - rotating the drone while airborne
4. velocity_change.py - changing the velocity of the drone
5. keyboard_control.py - controlling the drone manually via computer key board
6. up_down.py - moving the drone up and down between specific altitudes

## import installations:
To install special packages and libraries, run follwing command in the terminal

 * pip install cv2
 * pip install dronekit-python
 * pip install pymavlink
 * pip install numpy


## Steps to Create a Deep Learning Model for Object Recognition Using Video Footage:

### Introduction: The following are the sequential steps to create a deep learning model for object recognition by capturing images from a video and then using those images to train a model. This step-by-step guide will walk you through the entire process, from video processing to model training.

Steps:

### 1) Capture Video Footage:

Record the video footage of the object you want to recognize. This video should have clear shots from various angles to provide sufficient training data.

### 2) Extract Frames from Video:

Use video processing tools (e.g., OpenCV) to extract frames from the video. These frames will be saved as individual images to use as training data.
It is important to save frames periodically to cover different views and conditions of the object.

### 3) Label Images:

Manually label the extracted images with the appropriate object categories. This step is crucial to prepare a labeled dataset for supervised learning.
Tools like LabelImg can be used to make the labeling process easier.

### 4) Data Preprocessing:

Resize the images to a uniform size, normalize pixel values, and split the dataset into training, validation, and testing sets.
This preprocessing ensures that the model can learn effectively from the data.

### 5) Define and Compile a Deep Learning Model:

Define a convolutional neural network (CNN) model using deep learning frameworks like TensorFlow or PyTorch.
Compile the model by selecting an appropriate optimizer (e.g., Adam) and loss function (e.g., categorical cross-entropy).

### 6) Train the Model:

Train the model using the labeled image dataset. This involves feeding the data into the model, allowing it to learn the features of the object.
Monitor metrics like accuracy and loss to evaluate the training process.

### 7) Evaluate the Model:

Use the validation and test datasets to evaluate the performance of the trained model.
Make adjustments if necessary, such as fine-tuning hyperparameters to improve accuracy.

### 8) Save and Deploy the Model:

Save the trained model to a file for future use.
Deploy the model to recognize the desired object in real-time video footage or images.

