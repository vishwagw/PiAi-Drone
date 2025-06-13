# in colab convert the file type into .ipynb
import tensorflow as tf
import numpy as np
import cv2

# Load data to be used for training.
data_dir = 'path/to/directory'
classes = ['object1', 'object2', 'object3']      #  Name the object you want

images = []
labels = []

for idx, class_name in enumerate(classes):
  path = os.path.join(data_dir, class_name)
  for img in os.listdir(path):
    img_path = os.path.join(path, img)
    img = cv2.imread(img_path)
    img = cv2.resize(img, (224, 224)) # change the size of image
    images.append(img)
    labels.append(idx)

