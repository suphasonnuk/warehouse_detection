# from roboflow import Roboflow
import cv2
import matplotlib.pyplot as plt

from roboflow import Roboflow


source = "rtsp://admin:admin1234@192.168.1.108:554/cam/realmonitor?channel=1&subtype=1"

import cv2
import inference
import supervision as sv

annotator = sv.BoxAnnotator()

def render(predictions, image):
    print(predictions)
    image = annotator.annotate(
        scene=image, detections=sv.Detections.from_roboflow(predictions)
    )

    cv2.imshow("Prediction", image)
    cv2.waitKey(1)

inference.Stream(
    source = "rtsp://admin:admin1234@192.168.1.108:554/cam/realmonitor?channel=1&subtype=1", # replace with your camera IP
    model="human-dataset-v2/6",
    output_channel_order="BGR",
    use_main_thread=True,
    on_prediction=render,
)

# frame = cv2.resize(frame , (w,h) )  
# while True:
#     ret, frame = vid.read()

#     gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
#     blur = cv2.GaussianBlur(frame , (5,5) , 0) 
#     results = model.predict(gray, confidence=40, overlap=30).json()

#     for i in results['predictions']:
#         x0 = i['x'] - i['width'] / 2
#         x1 = i['x'] + i['width'] / 2
#         y0 = i['y'] - i['height'] / 2
#         y1 = i['y'] + i['height'] / 2

#         start_point = (int(x0), int(y0))
#         end_point = (int(x1), int(y1))
#         cv2.rectangle(frame , start_point, end_point , (0,255,0) , 3)


#     cv2.imshow("result", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# visualize your prediction
# model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())