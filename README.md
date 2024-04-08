# Object Detection w/ YOLO v8
This as an implementation of **Ultralytics YOLO v8** for object detection.
## Introduction
**YOLO v8** is _state of the art_ model for computer vision tasks from **[Ultralytics](https://www.ultralytics.com)**. In this project, I have implemented it for _object detection_ task.
## Features
1. Real time object detection via Webcam
2. Object detection in an uploaded video file
## Technologies Used
1. Ultralytics YOLO v8 (Model)
2. OpenCV (Video Processing)
3. Roboflow Supervision (Video Processing)
4. Streamlit (UI)
## Project Structure
```
├─── models/
│     └─── __init__.py
├─── outputs/
├─── research/
│     └─── trials.ipynb
├─── sources/
├─── utils/
│     └─── __init__.py
├─── variables/
│     └─── __init__.py
├─── app.py
├─── template.py
├─── README.md
├─── requirements.txt
├─── LICENSE
└─── .gitignore
```
## Dependencies
```text
streamlit~=1.26.0
ultralytics~=8.1.1
supervision~=0.17.1
opencv-python~=4.9.0.80
pathlib~=1.0.1
pillow~=9.4.0
tqdm~=4.65.0
pyyaml~=6.0
```
## How to Install and Run
1. Clone the repository.
```
$ git clone https://github/repository/link
```
2. Get into the Project Directory
```
$ cd Object-Detection-w-YOLOv8
```
3. Install the required dependencies.
```
$ pip install -r requirements.txt
```
4. Run the app.
```
$ streamlit run app.py
```
5. Choose the mode and model.
6. Upload a video if **Video File** mode is selected.
7. Click the ```Start Detecting``` button.
## Use Cases
- It can be used to count cars entered and left a parking lot.
- To count live stock.
- Counting people that entered and left a shop.
- Other than counting, it can be used to detect any motion in a frame.
- And much more.
## Contributing
Contributions are welcomed and appreciated.
## License
This project is released under 'MIT License'.
## Conclusion
In conclusion, this project leverages the power of Ultralytics YOLO v8 
for real-time object detection. With features like webcam-based detection
and processing of uploaded video files, it offers a versatile solution for
various applications.
