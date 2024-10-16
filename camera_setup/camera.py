<<<<<<< HEAD
import cv2
import os
import supervision as sv
from ultralytics import YOLOv10

model = YOLOv10(r'C:\Users\Fer\Desktop\yolov10\fire\runs\detect\train\weights\best.pt')

bounding_box_annotator = sv.BoxAnnotator()
label_annotator = sv.LabelAnnotator()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

output_dir = 'output_images'
os.makedirs(output_dir, exist_ok=True)

img_counter = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    results = model(frame)[0]
    detections = sv.Detections.from_ultralytics(results)

    annotated_image = bounding_box_annotator.annotate(
        scene=frame, detections=detections)
    annotated_image = label_annotator.annotate(
        scene=annotated_image, detections=detections)

    cv2.imshow("GoPro_Webcam", annotated_image)

    k = cv2.waitKey(1)

    if k % 256 == 27:
        print("Escape hit, closing...")
=======
import cv2
import os
import supervision as sv
from ultralytics import YOLOv10

model = YOLOv10(r'C:\Users\Fer\Desktop\yolov10\fire\runs\detect\train\weights\best.pt')

bounding_box_annotator = sv.BoxAnnotator()
label_annotator = sv.LabelAnnotator()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

output_dir = 'output_images'
os.makedirs(output_dir, exist_ok=True)

img_counter = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    results = model(frame)[0]
    detections = sv.Detections.from_ultralytics(results)

    annotated_image = bounding_box_annotator.annotate(
        scene=frame, detections=detections)
    annotated_image = label_annotator.annotate(
        scene=annotated_image, detections=detections)

    cv2.imshow("GoPro_Webcam", annotated_image)

    k = cv2.waitKey(1)

    if k % 256 == 27:
        print("Escape hit, closing...")
>>>>>>> a6f8be59f3aabedc51739f18d978192a9c985c39
        break