import torch
import cv2
import json
import yolov5


model_folder = fr'yolov5_model'

model_size = {
    'l': fr'{model_folder}/yolov5l.pt',
    'm': fr'{model_folder}/yolov5m.pt',
    'n': fr'{model_folder}/yolov5n.pt',
    's': fr'{model_folder}/yolov5s.pt',
    'x': fr'{model_folder}/yolov5x.pt'
}

#source = "rtsp://admin:hugh63110111@192.168.1.108:554/cam/realmonitor?channel=1&subtype=1"
#source = "rtsp://admin:hugh63110111@172.28.4.11:554/cam/realmonitor?channel=1&subtype=1"     #for yuanter network 
source = 0


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

def init_streaming():
    try:
        vid = cv2.VideoCapture(source)
        if not vid.isOpened():
            raise ValueError("Unable to open video source")
    except Exception as e:
        print(f"Error opening video source: {e}")
        exit(1)
    return vid 

def init_model(size):
    try:
        model = yolov5.load(fr"{model_size[size]}") 
        return model 
    except Exception as e:
        print(f"No model: {e}")
        return None 

def model_result(model,frame):
    try:
        result = model(frame)
        result_jsons = result.pandas().xyxy[0].to_json(orient="records")
        result_dict = json.loads(result_jsons)
        frame2 = plot_boxes(result_dict, frame)
        return frame2
    except Exception as e:
        print(f"No model: {e}")


def streaming_run(vid=None,model=None):
    if vid == None: 
        print(f"streaming not init yet")
        exit(1)

    while(True):
        ret, frame = vid.read()
        if not ret:
            print("Failed to read from video source")
            break

        if model == None: 
            cv2.imshow('YOLO', frame)
        else: 
            try: 
                frame2 = model_result(model,frame)
                cv2.imshow('YOLO', frame2)
            except:
                cv2.imshow('YOLO', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()

def main():
    vid = init_streaming()
    model = init_model("n")
    streaming_run(vid=vid,model=model)


if __name__ == "__main__":
    main()