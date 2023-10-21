import cv2
import mtcnn
from PIL import Image
import base64
from io import BytesIO
import numpy as np
from scipy.spatial.distance import cosine
from HelperFiles.architecture import InceptionResNetV2
from HelperFiles.models import User

# Load the face recognition model
face_encoder = InceptionResNetV2()
face_encoder.load_weights("D:\Projects\FaceForwardProject\FaceForward_Project\Backend\HelperFiles\\facenet_keras_weights.h5")

user = User()
user_face = user.get_user_face("0608")
userPhoto = base64.b64encode(user_face[0]['Face']).decode('utf-8')
reference_face = Image.open(BytesIO(base64.b64decode(userPhoto))).resize((160, 160))
reference_array = np.asarray(reference_face).astype('float32')
reference_array = (reference_array - 127.5) / 128.0  # Normalize
registered_encoding = face_encoder.predict(np.expand_dims(reference_array, axis=0))[0]

# Load the MTCNN face detector
face_detector = mtcnn.MTCNN()

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
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Crop and preprocess the detected face
        detected_face = frame[y1:y2, x1:x2]
        detected_face = cv2.resize(detected_face, (160, 160))
        detected_face = (detected_face - 127.5) / 128.0  # Normalize

        # Encode the detected face
        detected_encoding = face_encoder.predict(np.expand_dims(detected_face, axis=0))[0]

        # Compare the detected encoding with registered encodings
        distance = cosine(registered_encoding, detected_encoding)
        print(distance)

        if distance > recognition_threshold:
            print("Yes")
            exit()

    cv2.imshow('Smart Gate', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    
