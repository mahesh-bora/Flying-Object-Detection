import streamlit as st
from models import Model
from utils import load_yaml_as_dict, save_file
import cv2
from moviepy.editor import VideoFileClip
import tempfile

VARIABLES = load_yaml_as_dict('variables/variables.yaml')
MODELS = VARIABLES['MODELS']
PATHS = VARIABLES['PATHS']

st.title("Flying Object Detection")  # Add the title

model_variant = st.selectbox('Select a model from below', options=MODELS)
model = Model(model_variant)

select_mode = st.radio('Select mode (Webcam or video file)', ['Webcam', 'Video File'], index=1)
mode = 0 if select_mode == 'Webcam' else 1

if mode == 1:
    upload = st.file_uploader(
        'Upload a video or an image!',
        type=['mov', 'avi', 'mp4', 'mpg', 'mpeg', 'm4v', 'wmv', 'mkv'],
        disabled=(mode == 0)
    )
    if upload is not None:
        save_file(upload, PATHS['SOURCES'] + upload.name)
        if st.button('Start detecting'):
            model.predict_video(
                source=PATHS['SOURCES'] + upload.name,
                target=PATHS['OUTPUTS'] + 'detected - ' + upload.name
            )
            # Display the detected video
            detected_video_path = PATHS['OUTPUTS'] + 'detected - ' + upload.name
            clip = VideoFileClip(detected_video_path)
            with tempfile.NamedTemporaryFile(suffix='.mp4', delete=False) as temp_file:
                clip.write_videofile(temp_file.name, codec="libx264")
                st.video(temp_file.name)
else:
    if st.button('Start detecting'):
        model.predict_web_cam()
        # Display the detected objects and their coordinates
        ret, frame = model.cap.read()
        height, width, _ = frame.shape
        detections = model.get_detections(frame)
        for detection in detections:
            x1, y1, x2, y2 = [int(x) for x in detection[:4]]
            label = detection[4]
            confidence = detection[5]
            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)
            coords_text = f"({center_x}, {center_y})"
            cv2.putText(frame, coords_text, (center_x, center_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36, 255, 12), 2)
            cv2.line(frame, (width // 2, height // 2), (center_x, center_y), (0, 0, 255), 2)
        st.image(frame, use_column_width=True)

