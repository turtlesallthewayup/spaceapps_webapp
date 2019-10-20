#keras

import numpy as np
import os
import cv2
import time
from imutils import paths
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import img_to_array
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Activation, Dropout, Flatten, Dense, Conv2D, MaxPooling2D
import matplotlib.pyplot as plt
from PIL import Image
from keras import optimizers
import numpy as np

import os
import cv2
# Global variables
RANDOM_SEED = 2017

FRAMES_PER_VIDEO = 50
IMAGE_SIZE = 150

SAVE_DIR = os.path.join(os.getcwd(), 'saved_models')
CRAPPY_MODEL = 'crappy_model.h5'
BOTTLENECK_MODEL = 'bottleneck_model.h5'

FONT = cv2.FONT_HERSHEY_SIMPLEX


EPOCHS = 15
BATCH_SIZE = 15
NUM_CLASSES = 3
TEST_SIZE = 0.25
TRAIN_SAMPLES = FRAMES_PER_VIDEO*NUM_CLASSES*(1-TEST_SIZE) #112
VAL_SAMPLES = FRAMES_PER_VIDEO*NUM_CLASSES*TEST_SIZE #38

data = []
labels = [] 

# helper function to plot a history of model's accuracy and loss
# def plot_model_history(model_history):
#     fig, axs = plt.subplots(1,2,figsize=(15,5))
#     # summarize history for accuracy
#     axs[0].plot(range(1,len(model_history.history['acc'])+1),model_history.history['acc'])
#     axs[0].plot(range(1,len(model_history.history['val_acc'])+1),model_history.history['val_acc'])
#     axs[0].set_title('Model Accuracy')
#     axs[0].set_ylabel('Accuracy')
#     axs[0].set_xlabel('Epoch')
#     axs[0].set_xticks(np.arange(1,len(model_history.history['acc'])+1),len(model_history.history['acc'])/10)
#     axs[0].legend(['train', 'val'], loc='best')
#     # summarize history for loss
#     axs[1].plot(range(1,len(model_history.history['loss'])+1),model_history.history['loss'])
#     axs[1].plot(range(1,len(model_history.history['val_loss'])+1),model_history.history['val_loss'])
#     axs[1].set_title('Model Loss')
#     axs[1].set_ylabel('Loss')
#     axs[1].set_xlabel('Epoch')
#     axs[1].set_xticks(np.arange(1,len(model_history.history['loss'])+1),len(model_history.history['loss'])/10)
#     axs[1].legend(['train', 'val'], loc='best')
#     plt.show()
    
# # PREPROCESSING DATASET -----------------
# print("[INFO] loading dataset...")

# #grab the paths to our input images followed by shuffling them 
# imagePaths = sorted(list(paths.list_images('dataset')))

# # loop over the input images
def ai_train(images_labels):
    data = []
    labels = []
    for i, d in images_labels:
        for d1 in d:
            data.append(np.asarray(d1))
            labels.append(i)
    
    print(len(data))
    print(len(labels))
    # scaling the data points from [0, 255] to the range [0, 1]
    # data = np.array(data, dtype="float32") / 255.0
    labels = np.array(labels)

    # # partition the data into training and testing splits using 75% of
    # # the data for training and the remaining 25% for testing
    (X_train, X_test, y_train, y_test) = train_test_split(data, labels, test_size=TEST_SIZE, random_state=RANDOM_SEED, stratify=labels)
    
    # # convert the labels from integers to vectors
    y_train = to_categorical(y_train, NUM_CLASSES).astype(int)
    y_test = to_categorical(y_test, NUM_CLASSES).astype(int)

    ## to make sure  images look correct
    Image.fromarray((X_train[-1]* 255).round().astype(np.uint8))
    
    #from collections import Counter
    Counter(y_train)
    Counter(y_test)
    
    ## TRAINING THE MODEL -----------------
    print("[INFO] training the model...")
    
    model = Sequential()
    model.add(Conv2D(32, (3, 3), input_shape=X_train[0].shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(NUM_CLASSES, activation='sigmoid'))
    
    sgd = optimizers.SGD(lr=0.01)
    
    model.compile(loss='categorical_crossentropy',
                  optimizer=sgd,
                  metrics=['accuracy'])
    
    start = time.time()
    model_info = model.fit(
            X_train, y_train,
            batch_size=BATCH_SIZE,
            epochs=EPOCHS,
            validation_data=(X_test, y_test),
            shuffle=True,
            verbose=1)
    end = time.time()
    
    print ("\nModel training time: %0.1fs\n" % (end - start))
    
    # plot_model_history(model_info)
    
    # # Evaluating the trained model
    scores = model.evaluate(X_test, y_test)
    print("\nTest Loss:  %.2f%%" % (scores[0]*100))
    print("Test Accuracy: %.2f%%\n" % (scores[1]*100))
    
    # # Saving model
    if not os.path.isdir(SAVE_DIR):
        os.makedirs(SAVE_DIR)
    model_path = os.path.join(SAVE_DIR, CRAPPY_MODEL)
    model.save(model_path)
    print('\nSaved trained model at %s ' % model_path)