# # import the necessary packages
# import CONST
import numpy as np
import cv2
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import os
import time
import tensorflow as tf
from keras import applications
# from gtts import gTTS
from pygame import mixer
import shutil

from django.conf import settings

# Global variables
RANDOM_SEED = 2017

FRAMES_PER_VIDEO = 50
IMAGE_SIZE = 150

SAVE_DIR = os.path.join(os.path.join(settings.BASE_DIR, 'spaceapps', 'core'), 'saved_models')
CRAPPY_MODEL = 'crappy_model.h5'
BOTTLENECK_MODEL = 'bottleneck_model.h5'

FONT = cv2.FONT_HERSHEY_SIMPLEX


from keras.backend.tensorflow_backend import set_session
import tensorflow as tf


# #load labels
# labels = os.listdir('./dataset')

# #store the sound of each label
# # if os.path.exists("./sounds") == True:
# #     shutil.rmtree("./sounds")
    
# # os.makedirs("./sounds")
# # (gTTS(text=labels[0], lang='en')).save("./sounds/0.mp3")
# # (gTTS(text=labels[1], lang='en')).save("./sounds/1.mp3")
# # (gTTS(text=labels[2], lang='en')).save("./sounds/2.mp3")
# # mixer.init()

# # Turn on the webcam
# cap = cv2.VideoCapture(0)
# time.sleep(2)

# print ('Press q to exit')
# y_pred_old = '-1'
# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
def ai_predict(imgPath):    
#     #preprocessing frame to predict its label
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True  # dynamically grow the memory used on the GPU
    config.log_device_placement = True  # to log device placement (on which device the operation ran)
    sess = tf.Session(config=config)

    # #load previously trained model
    model = applications.VGG16(include_top=False, weights='imagenet', input_shape=(IMAGE_SIZE,IMAGE_SIZE,3)) 
    top_model = load_model(os.path.join(SAVE_DIR, BOTTLENECK_MODEL))
    frame2 = cv2.imread(imagePath)
    frame2 = cv2.resize(frame, (IMAGE_SIZE, IMAGE_SIZE))
    frame2 = img_to_array(frame2)
    frame2 = np.array(frame2, dtype="float32") / 255
#     # generating a prdiction of the frame  
    y_pred = model.predict_classes(frame2[None,:,:,:])
    
    y_pred = top_model.predict_classes(model.predict(frame2[None,:,:,:]))
    print("y_pred:", y_pred)
    return y_pred
#     # if(y_pred[0] != y_pred_old): 
#     #     mixer.music.load("./sounds/"+str(y_pred[0])+'.mp3')
#     #     mixer.music.play()
    
#     y_pred_old = y_pred[0]
    
#     # cv2.putText(frame, labels[y_pred[0]] , (10, 30), FONT, 1, (0, 255, 0), 2, cv2.LINE_AA)
#     cv2.putText(frame, "Press q to exit", (10, 450), FONT, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
#     # Display the resulting frame
#     cv2.imshow('frame',frame)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # release the capture
# cap.release()
# cv2.destroyAllWindows()
#remove sounds folder
