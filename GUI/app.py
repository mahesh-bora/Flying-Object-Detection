# import streamlit as st
# from ultralytics import YOLO
# import cv2
# import tempfile
# from io import BytesIO

# # Load YOLOv8 models
# model1 = YOLO("C:/Users/itsma/Desktop/FlyingObjectDetection/Flying-Object-Detection/GUI/best.pt")
# model2 = YOLO("C:/Users/itsma/Desktop/FlyingObjectDetection/Flying-Object-Detection/GUI/best.pt")
# model3 = YOLO("C:/Users/itsma/Desktop/FlyingObjectDetection/Flying-Object-Detection/GUI/best.pt")
# model4 = YOLO("C:/Users/itsma/Desktop/FlyingObjectDetection/Flying-Object-Detection/GUI/best.pt")
# models = [model1, model2, model3, model4]

# def process_video(video_file, model):
#     # Read the video from the uploaded file
#     cap = cv2.VideoCapture(video_file)

#     # Get the video properties
#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     fps = cap.get(cv2.CAP_PROP_FPS)

#     # Create a buffer to store the output video
#     output_buffer = BytesIO()

#     # Create a video writer for the output video
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     out = cv2.VideoWriter(output_buffer, fourcc, fps, (width, height))

#     # Process the video frame by frame
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Perform object detection on the frame
#         results = model(frame)

#         # Draw the bounding boxes, lines, and coordinates on the frame
#         annotated_frame = results[0].plot()
#         for box in results[0].boxes:
#             # Get the center coordinates of the bounding box
#             center_x = int(box.xywh[0][0] + box.xywh[0][2] / 2)
#             center_y = int(box.xywh[0][1] + box.xywh[0][3] / 2)

#             # Draw a red line from the center of the screen to the center of the object
#             cv2.line(annotated_frame, (width // 2, height // 2), (center_x, center_y), (0, 0, 255), 2)

#             # Draw the coordinates on the frame
#             coords_text = f"({center_x}, {center_y})"
#             cv2.putText(annotated_frame, coords_text, (center_x, center_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36, 255, 12), 2)

#         # Write the annotated frame to the output video
#         out.write(annotated_frame)

#     # Release resources
#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()

#     # Reset the buffer to the beginning
#     output_buffer.seek(0)

#     return output_buffer

# def main():
#     st.title("YOLOv8 Object Detection")
#     video_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

#     if video_file is not None:
#         model_choice = st.selectbox("Select a model", ["Model 1", "Model 2", "Model 3", "Model 4"])
#         selected_model = models[["Model 1", "Model 2", "Model 3", "Model 4"].index(model_choice)]

#         if st.button("Process Video"):
#             output_buffer = process_video(video_file, selected_model)
#             st.success("Video processed successfully!")
#             st.download_button(
#                 label="Download Output Video",
#                 data=output_buffer.getvalue(),
#                 file_name="output.mp4",
#                 mime="video/mp4"
#             )

# if __name__ == "__main__":
#     main()