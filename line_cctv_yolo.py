import torch
import cv2
import json
import yolov5
import requests
import time

model = yolov5.load('yolov5s.pt') 

def plot_boxes(result_dict, frame):
    people_count = 0
    for ob in result_dict:
        if ob['name'] == 'person':
            people_count += 1
            rec_start = (int(ob['xmin']), int(ob['ymin']))
            rec_end = (int(ob['xmax']), int(ob['ymax']))
            color = (0, 0, 255)  
            thickness = 3
            cv2.rectangle(frame, rec_start, rec_end, color, thickness)
            cv2.putText(frame, f"Person {ob['confidence']:.2f}", rec_start,
                         cv2.FONT_HERSHEY_DUPLEX, 1, color, thickness)
    return frame, people_count

def send_image_to_line(token, image_path, people_count):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {token}'}
    msg = {'message': f"Frame from Video Capture. People Count: {people_count}"}
    files = {'imageFile': open(image_path, 'rb')}
    
    response = requests.post(url, headers=headers, data=msg, files=files)

    if response.status_code != 200:
        print(f"Error sending message: {response.status_code}")
        print(f"Response details: {response.text}")

    files['imageFile'].close()

def main():
    source = "rtsp://admin:hugh63110111@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0"
    token  = 'gKQejJvAmBhFXDjfcP3W9dEUaWaGsBY7QnKWttgYAKY'
    token_group = "RRUQILGYQljG87XlI92TIOME3oxvnkU6NCRht7bj9iz"

    cap = cv2.VideoCapture(source)
    if not cap.isOpened(): 
        raise Exception("video device not open")

    last_sent_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        results = model(frame)
        result_jsons = results.pandas().xyxy[0].to_json(orient="records")
        result_dict = json.loads(result_jsons)

        frame, people_count = plot_boxes(result_dict, frame)
        cv2.imshow('YOLO', frame)

        second = 5
        if time.time() - last_sent_time > second:
            image_path = './data/frame.jpg'
            cv2.imwrite(image_path, frame)
            send_image_to_line(token_group, image_path, people_count)
            last_sent_time = time.time()

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
