# import libraries
import os
import random
import numpy as np
from tqdm import tqdm
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import concatenate
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Dropout, Lambda
from tensorflow.keras.layers import Conv2D, Conv2DTranspose
from plotdata import plot_segmentation_test

import fire_scout_system.system.system_data as data

# Function definition

def segmentation_keras_load(running_ops):

    """
    Runs image segmentation to produce a binary pixel based image of fire within a frame
    :param running_ops: Checks the json file and if segmentation = on, then segmentation will
    begin to run until image has been processed
    """

    """ Defining general parameters """
   
    #Define testing variables
    img_size = 512,512
    img_width = 512
    img_height = 512
    img_channels = 3
    dir_images = "segmentation/Segmentation/Data/Images"
    num_classes = 2
    test_img_path = ['Data/Images/fireframe.jpg']

    #Set image parameters
    x_val = np.zeros((len(test_img_path), img_height, img_width, img_channels), dtype=np.uint8)
 
    #Prepare the image for testing
    for n, file_ in tqdm(enumerate(test_img_path)):
        img = tf.keras.preprocessing.image.load_img(file_, target_size=img_size)
        x_val[n] = img

    #Load in the model and make predictions
    model = tf.keras.models.load_model("/home/spring2021/Desktop/Segmentation/Data/FireSegmentation.h5")
    preds_val = model.predict(x_val, verbose=1)
    preds_val_t = (preds_val > 0.5).astype(np.uint8)


    #Plot the data
    plot_segmentation_test(ypred=preds_val_t, num_samples=1)



