import cv2

def main():

    source = "rtsp://admin:admin1234@192.168.1.108:554/cam/realmonitor?channel=1&subtype=1"
    # source = "rtsp://admin:hugh63110111@172.28.4.11:554/cam/realmonitor?channel=1&subtype=1"     #for yuanter network 

    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise Exception("video device not open")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("No receiving frame and Streaming ends")
            break

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

