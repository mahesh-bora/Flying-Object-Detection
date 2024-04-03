import streamlit as st
from ultralytics import YOLO
import cv2
import tempfile
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Load YOLOv8 models
model1 = YOLO("C:/Users/itsma/Desktop/FlyingObjectDetection/Flying-Object-Detection/GUI/best.pt")
model2 = YOLO("C:/Users/itsma/Desktop/FlyingObjectDetection/Flying-Object-Detection/GUI/best.pt")
model3 = YOLO("C:/Users/itsma/Desktop/FlyingObjectDetection/Flying-Object-Detection/GUI/best.pt")
model4 = YOLO("C:/Users/itsma/Desktop/FlyingObjectDetection/Flying-Object-Detection/GUI/best.pt")
models = [model1, model2, model3, model4]

# Function to draw bounding box on image
def draw_bbox(ax, box_coords, class_id, conf):
    # Create a Rectangle patch
    rect = patches.Rectangle((box_coords[0], box_coords[1]), box_coords[2], box_coords[3],
                             linewidth=2, edgecolor='r', facecolor='none')

    # Add the patch to the Axes
    ax.add_patch(rect)

    # Add label (class ID, confidence, and coordinates) along with the box, making the text bold
    label = f"Class: {class_id}, Confidence: {conf:.2f}, Coordinates: {box_coords}"
    ax.text(box_coords[0], box_coords[1], label, fontsize=10, color='r',
            verticalalignment='bottom', fontweight='bold')

# Function to perform inference and get bounding box predictions
def predict(image_path, model):
    # Perform inference using model.predict() (replace with actual inference method)
    results = model.predict(image_path)

    # Extract bounding box predictions from the inference results
    bounding_boxes = []
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])  # Convert class ID to integer
            class_name = result.names[class_id]  # Access class name using class ID
            box_coords = [round(coord) for coord in box.xyxy[0].tolist()]
            conf = round(float(box.conf[0]), 2)  # Convert tensor to float before rounding
            bounding_boxes.append((class_name, conf, box_coords))

    return bounding_boxes

def process_video(video, model):
    # Create a temporary directory for frames
    temp_dir = tempfile.mkdtemp()
    
    # Get the video properties
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)
    
    # Process the video frame by frame
    frame_count = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break
        
        # Save the frame as an image
        frame_path = os.path.join(temp_dir, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)
        
        # Perform object detection on the frame
        bounding_boxes = predict(frame_path, model)
        
        # Draw bounding boxes on the frame
        fig, ax = plt.subplots()
        ax.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for display
        for class_id, conf, box_coords in bounding_boxes:
            draw_bbox(ax, box_coords, class_id, conf)
        plt.axis('off')
        
        # Save the modified frame
        annotated_frame_path = os.path.join(temp_dir, f"annotated_frame_{frame_count}.jpg")
        plt.savefig(annotated_frame_path, bbox_inches='tight', pad_inches=0)
        plt.close(fig)
        
        frame_count += 1
    
    # Create a video from the processed frames
    output_video_path = os.path.join(temp_dir, "output_video.mp4")
    output_video = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
    for i in range(frame_count):
        annotated_frame_path = os.path.join(temp_dir, f"annotated_frame_{i}.jpg")
        frame = cv2.imread(annotated_frame_path)
        output_video.write(frame)
    output_video.release()
    
    return output_video_path

def main():
    st.title("YOLOv8 Object Detection")
    video_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

    if video_file is not None:
        model_choice = st.selectbox("Select a model", ["Model 1", "Model 2", "Model 3", "Model 4"])
        selected_model = models[["Model 1", "Model 2", "Model 3", "Model 4"].index(model_choice)]

        if st.button("Process Video"):
            # Save the uploaded file to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
                temp_file.write(video_file.read())
                temp_file_path = temp_file.name

            # Open the temporary video file
            video = cv2.VideoCapture(temp_file_path)
            output_file_path = process_video(video, selected_model)
            st.success("Video processed successfully!")
            video.release()  # Release the video capture resource


            # Display download button for the output video
            with open(output_file_path, "rb") as output_video:
                st.download_button(
                    label="Download Output Video",
                    data=output_video.read(),
                    file_name="output_video.mp4",
                    mime="video/mp4"
                )

            # Remove the temporary file
            os.remove(temp_file_path)

if __name__ == "__main__":
    main()
