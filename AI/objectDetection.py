import time
from absl import logging
from absl.flags import FLAGS
import cv2
import os
import glob
import time
import numpy as np
import tensorflow as tf
import fire_scout_system.system.system_data as data
from yolov3_tf2.models import (
    YoloV3, YoloV3Tiny
)
from yolov3_tf2.dataset import transform_images
from yolov3_tf2.utils import draw_outputs


def run(running_ops):

    yolo = YoloV3(classes=4)

    yolo.load_weights('./weights/yolov3.tf').expect_partial()
    print('weights loaded')

    class_names = [c.strip() for c in open('./data/labels/obj.names').readlines()]
    print('classes loaded')
  
    raw_images = []

    # This retrieves all images from images
    newest = ("/home/Data/Images/")
    
    img_raw = tf.image.decode_image(open(newest, 'rb').read(), channels=3)
        
    raw_images.append(img_raw)

    num = 0    

    for raw_img in raw_images:
        num+=1
        img = tf.expand_dims(raw_img, 0)
        img = transform_images(img, 416)

        t1 = time.time()
        boxes, scores, classes, nums = yolo(img)
        t2 = time.time()
        logging.info('time: {}'.format(t2 - t1))

        print('detections:')
        for i in range(nums[0]):
            print('\t{}, {}, {}'.format(class_names[int(classes[0][i])],
                                            np.array(scores[0][i]),
                                            np.array(boxes[0][i])))

        img = cv2.cvtColor(raw_img.numpy(), cv2.COLOR_RGB2BGR)
        img = draw_outputs(img, (boxes, scores, classes, nums), class_names)
        #timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
        cv2.imwrite('./test_images/Object_Det/obj_det_0.jpg', img)
        #print('output saved to: {}'.format('./test_images/Object_Det' + 'obj_det_0') + '.jpg')
