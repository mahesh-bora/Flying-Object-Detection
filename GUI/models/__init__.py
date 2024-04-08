from ultralytics import YOLO
import cv2
from supervision.utils.video import VideoInfo, VideoSink, get_video_frames_generator
from supervision.detection.core import Detections
from supervision.detection.annotate import BoxAnnotator
from utils import create_colorpalette, hex_to_rgb
import streamlit as st

colors = [
    "#a351fb", "#e6194b", "#3cb44b", "#ffe119", "#0082c8", "#f58231", "#911eb4", "#46f0f0", "#f032e6",
    "#d2f53c", "#fabebe", "#008080", "#e6beff", "#aa6e28", "#fffac8", "#800000", "#aaffc3",
]


class Model:
    def __init__(self, variant='best.pt'):
        self.model = YOLO('models/' + variant)
        self.CLASS_NAMES_DICT = self.model.model.names

    def predict_web_cam(self, source=0, show=True, save=False):
        cap = cv2.VideoCapture(source)  # Use 0 for the default camera

        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        size = (frame_width, frame_height)

        while True:
            ret, img0 = cap.read()

            self.model.predict(img0, show=show)

            # Check for the "Esc" key to break out of the loop
            key = cv2.waitKey(1)
            if key == 27:  # ASCII code for "Esc" key
                break

        # Release the webcam and close any open windows
        cap.release()
        cv2.destroyAllWindows()

    def predict_video(self, source: str, target: str):
        generator = get_video_frames_generator(source)
        box_annotator = BoxAnnotator(color=create_colorpalette(hex_to_rgb(colors)), thickness=4, text_thickness=1,
                                     text_scale=1)
        video_info = VideoInfo.from_video_path(source)
        total, current = video_info.total_frames, 0
        progress_text = f'Frames: {current}/{total}, {round(100*current/total, 1)}% | The video is being processed!'
        progress_bar = st.progress(current/total, progress_text)
        with VideoSink(target, video_info) as sink:
            for frame in generator:
                progress_text = f'Frames: {current}/{total}, {round(100*current/total, 1)}% | The video is being processed!'
                current += 1
                progress_bar.progress(current/total, 'Completed!' if current == total else progress_text)
                results = self.model(frame)

                detections = Detections(
                    xyxy=results[0].boxes.xyxy.cpu().numpy(),
                    confidence=results[0].boxes.conf.cpu().numpy(),
                    class_id=results[0].boxes.cls.cpu().numpy().astype(int)
                )
                labels = [
                    f'{self.CLASS_NAMES_DICT[class_id]} {confidence:0.2f}'
                    for _, _, confidence, class_id, _,
                    in detections
                ]

                key = cv2.waitKey(1)
                if key == 27:  # ASCII code for "Esc" key
                    break

                frame = box_annotator.annotate(frame, detections=detections, labels=labels)

                sink.write_frame(frame)
    
    def predict_image(self, image_path):
            # Load the image
            image = cv2.imread(image_path)
            results = self.model(image)
            # Perform object detection (this is just a placeholder, replace with your actual detection logic)
            detections = Detections(
                    xyxy=results[0].boxes.xyxy.cpu().numpy(),
                    confidence=results[0].boxes.conf.cpu().numpy(),
                    class_id=results[0].boxes.cls.cpu().numpy().astype(int)
                )

            # Draw bounding boxes and labels on the image
            for detection in detections:
                x1, y1, x2, y2, label, confidence = detection
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(image, f'{label} {confidence:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Return the image with detections
            return image