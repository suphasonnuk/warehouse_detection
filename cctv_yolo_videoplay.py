import torch
import cv2
import json
# import yolov5
from ultralytics import YOLO
from roboflow import Roboflow
import matplotlib.pyplot as plt


try:
    # model = yolov5.load('yolov5n.pt') 
    # rf = Roboflow(api_key="7PWH81HNN7R0kyNexWlk")
    # project = rf.workspace().project("human-dataset-v2")
    # model = project.version(6).model
    model = YOLO('yolov8x.pt')
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

source = "rtsp://admin:admin1234@192.168.1.108:554/cam/realmonitor?channel=1&subtype=1"
# source = "rtsp://admin:hugh63110111@172.28.4.11:554/cam/realmonitor?channel=1&subtype=1"     #for yuanter network 
#source = 0

try:
    vid = cv2.VideoCapture("img/img1.jpg")
    if not vid.isOpened():
        raise ValueError("Unable to open video source")
except Exception as e:
    print(f"Error opening video source: {e}")
    exit(1)

def plot_boxes(result_dict, frame):
    for ob in result_dict:
        rec_start = (int(ob['xmin']), int(ob['ymin']))
        rec_end = (int(ob['xmax']), int(ob['ymax']))
        color = (255, 0, 0)
        thickness = 3

        if ob['name'] == 'person':
            color = (0, 0, 255)
        cv2.rectangle(frame, rec_start, rec_end, color, thickness)
        cv2.putText(frame, f"{ob['name']} {ob['confidence']:.2f}", rec_start, cv2.FONT_HERSHEY_DUPLEX, 2, color, thickness)
    return frame



frame = cv2.imread("img/img_test.jpg")
percent = 0.1
h= int(frame.shape[1] * percent)
w= int(frame.shape[0] * (percent * 2))
frame = cv2.resize(frame , (w,h) )  

results = model.track(source=frame, show =True , classes = 0 ,conf = 0.5) 

print(results)

cv2.destroyAllWindows()



vid.release()
cv2.destroyAllWindows()
