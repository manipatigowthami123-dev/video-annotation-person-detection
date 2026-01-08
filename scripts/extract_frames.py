import cv2
import os

BASE_DIR = r"C:\Users\manip\OneDrive\Desktop\video_annotation_project"

video_path = os.path.join(BASE_DIR, "input_videos", "sample.mp4")
frames_dir = os.path.join(BASE_DIR, "frames")

os.makedirs(frames_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video")
    exit()

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_name = f"frame_{frame_count:04d}.jpg"
    frame_path = os.path.join(frames_dir, frame_name)

    cv2.imwrite(frame_path, frame)
    frame_count += 1

cap.release()
print("Frame extraction completed.")
print("Total frames:", frame_count)
