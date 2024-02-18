# This directory is still **Under Construction**. Arranging files and folders as objects, and arrange code aren't meaned to be finished yet. OK?   

# Explanation of each file:
- **cctv_videoplay**
    - [cctv_yolo_videoplay.py](https://github.com/hughnaaek/capstone_intelligence_system/blob/main/cctv_yolo_videoplay.py) and[cctv_yolo_videoplay_new_arrange.py](https://github.com/hughnaaek/capstone_intelligence_system/blob/main/cctv_yolo_videoplay_new_arrange.py) are the file for running streaming with yolov5.  
    - [cctv_HOG_videoplay.py](https://github.com/hughnaaek/capstone_intelligence_system/blob/main/cctv_HOG_videoplay.py) is the file for running streaming with HOG.
    - [cctv_videoplay.py](https://github.com/hughnaaek/capstone_intelligence_system/blob/main/cctv_videoplay.py) is the file for running streaming without model.
- **line**
    - [line_notify_imgtext.py](https://github.com/hughnaaek/capstone_intelligence_system/blob/main/line_notify_imgtext.py) is the file for sending img or text via line. 
    - [line_cctv_image.py](https://github.com/hughnaaek/capstone_intelligence_system/blob/main/line_cctv_image.py) is the file for sending frame of cctv via line. 
    - [line_notify_yolo.py](https://github.com/hughnaaek/capstone_intelligence_system/blob/main/line_notify_yolo.py) is the file for sending yolo detected frame of cctv and human counting via line. 
    

# RSTP streaming DAHUA via VLC  
how to connect the cctv with your device 
- `192.168.1.108` is the default ip of the cctv
- `172.28.4.11` is the ipV4 of Yuanter 

```python
#source = "rtsp://admin:hugh63110111@192.168.1.108:554/cam/realmonitor?channel=1&subtype=1"
source = "rtsp://admin:hugh63110111@172.28.4.11:554/cam/realmonitor?channel=1&subtype=1"     #for yuanter network
```
- Those lines of code are found in the python files, whose name stating with cctv.
- **subtype = 0** is **main** streaming and **subtype = 1** is **sub** streaming

## Network Configuration Details: how to set your ethernet for connect ip of the cctv
- **Laptop**
  - IPv4 address: `172.28.4.14`
  - Subnet mask: `255.255.255.0`
  - Default gateway: `172.28.4.1`

- **CCTV Camera**
  - IPv4 address: `172.28.4.11`
  - Subnet mask: `255.255.255.0`
  - Default gateway: `172.28.4.1`

- **NVR**
  - IPv4 address: `172.28.4.12`
  - Subnet mask: `255.255.255.0`
  - Default gateway: `172.28.4.1`

To open web brower of ip-cctv, you need to input the CCTV Camera  `172.28.4.11` as URL. 

This link below is the test to RTSP connection by VLC application: [dahua wiki website](https://dahuawiki.com/Remote_Access/RTSP_via_VLC)

# Line notification 
Using to generate token for the python files, whose name stating with line.   
```python
# Insert your Line token into those line of code in the files
# "token" is the token of my personal line notify   
token       = 'gKQejJvAmBhFXDjfcP3W9dEUaWaGsBY7QnKWttgYAKY'
# "token group" is the token of line notify in our capstone line group 
token_group = "RRUQILGYQljG87XlI92TIOME3oxvnkU6NCRht7bj9iz"
```
Personal line notify: 

![image](https://github.com/hughnaaek/capstone_intelligence_system/assets/94478009/7ad44f37-c887-4026-afdc-e60da50fd7b7)

Line notify in our capstone line group: 

![image](https://github.com/hughnaaek/capstone_intelligence_system/assets/94478009/15a59f2b-9c12-46b1-a82f-607bbeb1a87b)


Here is the link to generate to token: [Token creation](https://notify-bot.line.me/th/)

# Yolov.8 
## Yolo v8 Library and Installation
- Treating the yolo as python lib for downloading and testing of the model. 
  - [Yolo v8 Library and Installation](https://yolov8.com/)
- Pip website with detail of usage of the lib. *recommend to read 
  - [pip website](https://pypi.org/project/ultralytics/) 
## Yolo v8 Documentation
- [Yolo v8 Documentation](https://docs.ultralytics.com/)
## Yolo v8 GitHub Repository
- [Yolo v8 GitHub Repository](https://github.com/ultralytics/yolov5)

# Roboflow: how to use 
## Roboflow Raspberry Pi Integration
- How is the methods of how to integrate our Rasp PI with Roboflow. If Yolov.8 isn't fast enough for the intelligence system, here is what we gonna continue. 
  - [Roboflow Raspberry Pi Integration](https://docs.roboflow.com/deploy/raspberry-pi)
## Roboflow Python API
- Using the API by Python programming, we wanna try with pc or raspberry pi. 
  - [Roboflow Python API](https://docs.roboflow.com/deploy/hosted-api/object-detection)

The code below is the example of how using Python API of Roboflow looks like 
```python
from roboflow import Roboflow
rf = Roboflow(api_key="API_KEY")
project = rf.workspace().project("MODEL_ENDPOINT")
model = project.version(VERSION).model

# infer on a local image
print(model.predict("your_image.jpg", confidence=40, overlap=30).json())

# visualize your prediction
# model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())
```

# ConvNeXt-V2: Son of the ResNet-based and Transformer-based.   
- Using in the worst case that Yolov.8 and Roboflow are unavailable. The server request is submitted as Ive sent in our line group. 
  - [Link of the model](https://github.com/facebookresearch/ConvNeXt-V2)
"# warehouse_detection" 
