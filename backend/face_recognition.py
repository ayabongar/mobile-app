import cv2
import numpy as np
import face_recognition

def encode_face(image_path):
    image = cv2.imread(image_path)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(rgb_image)
    if encodings:
        return encodings[0]
    return None

def verify_face(known_encoding, image_path):
    unknown_encoding = encode_face(image_path)
    results = face_recognition.compare_faces([known_encoding], unknown_encoding)
    return results[0]
