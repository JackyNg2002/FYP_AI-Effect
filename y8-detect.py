from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')  # load an official model


# Predict with the model
results = model(source=0, save=True, show=True)  # predict on an image