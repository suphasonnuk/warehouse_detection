import requests
import cv2
import time

def send_image_to_line(token, image_path):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {token}'}
    msg = {'message': "Frame from Video Capture"}
    files = {'imageFile': open(image_path, 'rb')}
    
    response = requests.post(url, headers=headers, data=msg, files=files)
    print(response)
    files['imageFile'].close()

def main():
    source = "rtsp://admin:hugh63110111@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0"
    token  = "gKQejJvAmBhFXDjfcP3W9dEUaWaGsBY7QnKWttgYAKY"

    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise Exception("video device not open")

    last_sent_time = time.time()

    while True:
        ret, frame = cap.read()

        if not ret:
            print("No receiving frame and Streaming ends")
            break

        cv2.imshow('frame', frame)

        second = 2
        if time.time() - last_sent_time > second:
            
            image_path = './data/frame.jpg'
            cv2.imwrite(image_path, frame)

            send_image_to_line(token, image_path)
            
            last_sent_time = time.time()

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
