# Video Annotation and Person Detection

This project implements an end-to-end video annotation pipeline that detects persons in a video and generates an annotated output video. It uses OpenCV for video processing and YOLOv8 for real-time person detection.

## 🔍 Project Overview

The application takes a video as input, extracts frames, performs person detection on each frame using a pre-trained YOLOv8 model, and reconstructs an annotated video highlighting detected persons with bounding boxes.

This project demonstrates practical usage of computer vision and deep learning in video analytics.

## 🛠️ Technologies Used

- Python 3.10
- OpenCV
- YOLOv8 (Ultralytics)
- NumPy
- Git & GitHub

## 📂 Project Structure

video_annotation_project/
│
├── scripts/
│ ├── extract_frames.py
│ ├── person_detection.py
│ └── frames_to_video.py
│
├── input_videos/
├── output_videos/
├── requirements.txt
├── .gitignore
└── README.md

## ⚙️ How It Works

1. **Frame Extraction**  
   The input video is split into individual frames using OpenCV.

2. **Person Detection**  
   Each frame is processed using YOLOv8 to detect persons and draw bounding boxes.

3. **Video Reconstruction**  
   The annotated frames are combined back into a single output video.

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/mani-gowthami123-dev/video-annotation-person-detection.git
2.Create and activate a virtual environment (Python 3.10 recommended)

3.Install dependencies:

  pip install -r requirements.txt


4.Place your input video inside the input_videos folder.

5.Run the scripts in order:

python scripts/extract_frames.py
python scripts/person_detection.py
python scripts/frames_to_video.py


6.The final annotated video will be available in the output_videos folder.
