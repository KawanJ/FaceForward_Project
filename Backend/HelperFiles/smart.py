import cv2
import mtcnn
import pickle
import numpy as np
from scipy.spatial.distance import cosine
from tensorflow.keras.models import load_model
from architecture import InceptionResNetV2

# Load the face recognition model
face_encoder = InceptionResNetV2()
face_encoder.load_weights("facenet_keras_weights.h5")

# Load the MTCNN face detector
face_detector = mtcnn.MTCNN()

# Load the encoding dictionary (user database)
try:
    with open('encodings/encodings.pkl', 'rb') as file:
        encoding_dict = pickle.load(file)
except FileNotFoundError:
    encoding_dict = {}

# Confidence threshold for face recognition
recognition_threshold = 0.5

# Initialize the video capture (camera)
cap = cv2.VideoCapture(0)


while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Camera not opened")
        break

    # Detect faces in the frame
    faces = face_detector.detect_faces(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    for face in faces:
        x, y, width, height = face['box']
        x1, y1 = abs(x), abs(y)
        x2, y2 = x1 + width, y1 + height

        # Crop and preprocess the detected face
        detected_face = frame[y1:y2, x1:x2]
        detected_face = cv2.resize(detected_face, (160, 160))
        detected_face = (detected_face - 127.5) / 128.0  # Normalize

        # Encode the detected face
        detected_encoding = face_encoder.predict(np.expand_dims(detected_face, axis=0))[0]

        # Compare the detected encoding with registered encodings
        for name, registered_encoding in encoding_dict.items():
            distance = cosine(registered_encoding, detected_encoding)

            if distance < recognition_threshold:
                # Match found; allow access
                cv2.putText(frame, f"Access Granted: {name}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                break
        else:
            # No match found; deny access
            cv2.putText(frame, "Access Denied", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv2.imshow('Smart Gate', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# When a new user registers on the admin portal:
# Capture, preprocess, and encode the new user's face data
new_user_name = "NewUser"
new_user_encoding = detected_encoding  # Replace with the actual encoding for the new user

# Add the new user to the encodings dictionary
encoding_dict[new_user_name] = new_user_encoding

# Update the encodings database file
with open('encodings/encodings.pkl', 'wb') as file:
    pickle.dump(encoding_dict, file)
    
