print('holaviaj')
from ultralytics import YOLO

print('libreria cargada')
# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

print('model cargado')
# Use the model
results = model.train(data="config.yaml", epochs=1)  # train the model