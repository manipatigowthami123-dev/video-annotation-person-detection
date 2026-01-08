from ultralytics import YOLO
import cv2
import os

BASE_DIR = r"C:\Users\manip\OneDrive\Desktop\video_annotation_project"

frames_dir = os.path.join(BASE_DIR, "frames")
output_dir = os.path.join(BASE_DIR, "output_videos", "detected_frames")

os.makedirs(output_dir, exist_ok=True)

print("Frames directory:", frames_dir)
print("Output directory:", output_dir)
print("Number of frames found:", len(os.listdir(frames_dir)))

model = YOLO("yolov8n.pt")

for frame_name in sorted(os.listdir(frames_dir)):
    frame_path = os.path.join(frames_dir, frame_name)

    frame = cv2.imread(frame_path)
    if frame is None:
        print("Skipped:", frame_name)
        continue

    results = model(frame, conf=0.4)

    for r in results:
        for box in r.boxes:
            if int(box.cls[0]) == 0:  # person
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, "Person", (x1, y1 - 8),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    out_path = os.path.join(output_dir, frame_name)
    cv2.imwrite(out_path, frame)
    print("Saved:", out_path)

print("Person detection completed successfully.")
