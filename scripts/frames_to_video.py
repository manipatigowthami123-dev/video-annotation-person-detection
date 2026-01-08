import cv2
import os

BASE_DIR = r"C:\Users\manip\OneDrive\Desktop\video_annotation_project"

frames_dir = os.path.join(BASE_DIR, "output_videos", "detected_frames")
output_video_path = os.path.join(BASE_DIR, "output_videos", "annotated_output.mp4")

# Get all frame names
frames = sorted(os.listdir(frames_dir))

if not frames:
    print("No frames found to create video.")
    exit()

# Read first frame to get size
first_frame = cv2.imread(os.path.join(frames_dir, frames[0]))
height, width, _ = first_frame.shape

# Create VideoWriter
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video = cv2.VideoWriter(output_video_path, fourcc, 20, (width, height))

for frame_name in frames:
    frame_path = os.path.join(frames_dir, frame_name)
    frame = cv2.imread(frame_path)
    video.write(frame)

video.release()
print("Annotated video created successfully.")
print("Saved at:", output_video_path)
