# Object Detection w/ YOLO Models
This as an implementation of **Ultralytics YOLO** for object detection.
## Introduction
**YOLO** is _state of the art_ model for computer vision tasks from **[Ultralytics](https://www.ultralytics.com)**. In this project, We have implemented it for _flying object detection_ task.
## Features
1. Real time object detection via Webcam
2. Object detection in an uploaded video/image file
## Technologies Used
1. Ultralytics YOLO v8m/v8s/v5m/v5s (Model)
2. OpenCV (Video Processing)
3. Roboflow Supervision (Video Processing)
4. Streamlit (UI)
## Project Structure - GUI
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
opencv_python==4.9.0.80
opencv_python_headless==4.8.1.78
Pillow==9.4.0
PyYAML==6.0.1
streamlit==1.26.0
supervision==0.17.1
ultralytics==8.1.3
moviepy
supervision
```
## How to Install and Run
1. Clone the repository.
```
$ git clone https://github/repository/link
```
2. Get into the Project Directory
```
$ cd GUI
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
- Airport security
- Border patrol
- Military defense
- Event security
- Wildlife conservation
- And much more.
## Contributing
Contributions are welcomed and appreciated.
## License
This project is released under 'MIT License'.
## Conclusion
In conclusion, this project leverages the power of Ultralytics YOLO models 
for real-time flying object detection. With features like webcam-based detection
and processing of uploaded video and image files, it offers a versatile solution for
various applications.
