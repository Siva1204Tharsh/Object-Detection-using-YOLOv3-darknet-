import cv2
import numpy as np

#load the trained model
yolo = cv2.dnn.readNetFromDarknet("yolov3.cfg", "yolov3.weights")