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

# Preprocess the data. Normalize images and convert labels to one-hot encoding form.
images = np.array(images) / 255.0
labels = tf.keras.utils.to_categorical(labels)
    
# Design the model. This example uses the VGG16 model
model = tf.keras.applications.VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

for layer in model.layers:
  layer.trainable = False

  x = tf.keras.layers.Flatten()(model.output)
  x = tf.keras.layers.Dense(256, activation='relu')(x)
  x = tf.keras.layers.Dropout(0.5)(x)
  x = tf.keras.layers.Dense(len(classes), activation='softmax')(x)

  model = tf.keras.models.Model(model.input, x)
