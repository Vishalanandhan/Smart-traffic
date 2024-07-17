import cv2
import torch
import numpy as np
from tracker import *

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)