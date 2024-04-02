import streamlit as st
from ultralytics import YOLO
import cv2
import tempfile

# Load YOLOv8 models
model1 = YOLO("C:/Users/itsma/Desktop/CD/Prac4/best (2).pt")
model2 = YOLO("C:/Users/itsma/Desktop/CD/Prac4/best (2).pt")
model3 = YOLO("C:/Users/itsma/Desktop/CD/Prac4/best (2).pt")
model4 = YOLO("C:/Users/itsma/Desktop/CD/Prac4/best (2).pt")


models = [model1, model2, model3, model4]

def process_video(video, model):
          # Set the video source (0 for webcam, or provide a video file path)
      cap = cv2.VideoCapture("Prac4/demo.mp4")

      # Get the video properties
      width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
      height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
      fps = cap.get(cv2.CAP_PROP_FPS)

      # Create a temporary file for the output video
      with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
            output_video_path = temp_file.name

      # Create a video writer for the output video
      fourcc = cv2.VideoWriter_fourcc(*'mp4v')
      out = cv2.VideoWriter('/Prac4/output-video-latest.mp4', fourcc, fps, (width, height))

      # Process the video frame by frame
      while True:
          ret, frame = cap.read()
          if not ret:
              break

          # Perform object detection on the frame
          results = model(frame)

          # Draw the bounding boxes, lines, and coordinates on the frame
          annotated_frame = results[0].plot()
          for box in results[0].boxes:
              # Get the center coordinates of the bounding box
              center_x = int(box.xywh[0][0] + box.xywh[0][2] / 2)
              center_y = int(box.xywh[0][1] + box.xywh[0][3] / 2)

              # Draw a red line from the center of the screen to the center of the object
              cv2.line(annotated_frame, (width // 2, height // 2), (center_x, center_y), (0, 0, 255), 2)

              # Draw the coordinates on the frame
              coords_text = f"({center_x}, {center_y})"
              cv2.putText(annotated_frame, coords_text, (center_x, center_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36, 255, 12), 2)

          # Write the annotated frame to the output video
          out.write(annotated_frame)

          # Display the frame in Colab
        #   cv2.imshow(annotated_frame)
        #   if cv2.waitKey(1) == ord('q'):
        #       break

      # Release resources
      cap.release()
      out.release()
      cv2.destroyAllWindows()
      return output_video_path

  

def main():
    st.title("YOLOv8 Object Detection")

    video_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

    if video_file is not None:
        model_choice = st.selectbox("Select a model", ["Model 1", "Model 2", "Model 3", "Model 4"])
        selected_model = models[["Model 1", "Model 2", "Model 3", "Model 4"].index(model_choice)]

        if st.button("Process Video"):
            output_file=process_video(video_file, selected_model)
            st.success("Video processed successfully!")
            st.download_button("Download Output Video", "output.mp4", "output.mp4")
            with open(output_file, "rb") as output_video:
                st.download_button("Download Output Video", output_file.split("/")[-1], output_video.read(),
                                   mime="video/mp4")
            # Display accuracy of the selected model
            # accuracy = selected_model.metrics.metrics["mAP_0.5:0.95"]
            # st.write(f"Model Accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    main()