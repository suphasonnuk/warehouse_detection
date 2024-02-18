import cv2
import numpy as np

#source = "rtsp://admin:hugh63110111@192.168.1.108:554/cam/realmonitor?channel=1&subtype=1"
source = "rtsp://admin:admin1234@192.168.1.108:554/cam/realmonitor?channel=1&subtype=1"    #for yuanter network 
#source = 0


def plot_boxes(frame, detections):
    for (x, y, w, h) in detections:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return frame

def main():

    # ========================= open video streaming =========================
    try:
        cap = cv2.VideoCapture(source)
        if not cap.isOpened():
            raise ValueError("Unable to open video source")
    
    except Exception as e:
        print(f"Error opening video source: {e}")
        exit(1)

    # ========================= initiate hog model============================

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    center_tolerance = 5; 
        # =================== read each frame and human detection ================
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # resizing for faster detection
        frame = cv2.resize(frame, (240, 240))
        # detect people in the image
        # returns the bounding boxes for the detected objects
        boxes, weights = hog.detectMultiScale(frame, winStride=(1,1), scale = 1.05)
        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
        centers = []
        for box in boxes:
            #get the distance from the center of each box's center x cord to the center of the screen and ad them to a list
            center_x = ((box[2]-box[0])/2)+box[0]
            x_pos_rel_center = (center_x-70)
            dist_to_center_x = abs(x_pos_rel_center)
            centers.append({'box': box, 'x_pos_rel_center': x_pos_rel_center, 'dist_to_center_x':dist_to_center_x})    
        if len(centers) > 0:
            #sorts the list by distance_to_center
            sorted_boxes = sorted(centers, key=lambda i: i['dist_to_center_x'])
            #draws the box
            center_box = sorted_boxes[0]['box']
            for box in range(len(sorted_boxes)):
            # display the detected boxes in the colour picture
                if box == 0:
                    cv2.rectangle(frame, (sorted_boxes[box]['box'][0],sorted_boxes[box]['box'][1]), (sorted_boxes[box]['box'][2],sorted_boxes[box]['box'][3]), (0,255, 0), 2)
                else:
                    cv2.rectangle(frame, (sorted_boxes[box]['box'][0],sorted_boxes[box]['box'][1]), (sorted_boxes[box]['box'][2],sorted_boxes[box]['box'][3]),(0,0,255),2)
            #retrieves the distance from center from the list and determins if the head should turn left, right, or stay put and turn lights on
            Center_box_pos_x = sorted_boxes[0]['x_pos_rel_center']  
        #resizes the video so its easier to see on the screen
        frame = cv2.resize(frame,(720,720))
        # Display the resulting frame
        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.waitKey(1)
            break

        # When everything done, release the capture
    cap.release()
        # finally, close the window
    cv2.destroyAllWindows()

    # =======================================================================


if __name__ == "__main__":
    main()
