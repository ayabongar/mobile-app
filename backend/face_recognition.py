import cv2
import numpy as np
import face_recognition
import numpy as np

def encode_face(image):
    # Load the uploaded image file
    image = face_recognition.load_image_file(image)
    # Encode the face in the image
    encodings = face_recognition.face_encodings(image)
    if not encodings:
        return None
    return encodings[0]

def verify_face(known_encoding, image):
    # Load the uploaded image file
    image = face_recognition.load_image_file(image)
    # Encode the face in the image
    unknown_encodings = face_recognition.face_encodings(image)
    if not unknown_encodings:
        return False
    # Compare the known encoding with the unknown encoding
    results = face_recognition.compare_faces([known_encoding], unknown_encodings[0])
    return results[0]

