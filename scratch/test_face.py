import face_recognition
import numpy as np
import cv2

print("Libraries imported.")

# Create a blank image
img = np.zeros((100, 100, 3), dtype=np.uint8)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print("Starting face_encodings...")
enc = face_recognition.face_encodings(rgb)
print(f"Done. Found {len(enc)} faces.")
