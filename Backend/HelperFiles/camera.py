import cv2
import time
import tensorflow
import numpy as np
import base64
from io import BytesIO
from PIL import Image
from keras_facenet import FaceNet
from sklearn.metrics.pairwise import cosine_similarity

def detect_matching_face(encoded_photo):
    embedder = FaceNet()
    model = tensorflow.keras.applications.ResNet50(weights='imagenet')
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Load the reference image
    # reference_face = Image.open(reference_face_path).resize((224, 224))
    reference_face = Image.open(BytesIO(base64.b64decode(encoded_photo)))
    reference_array = np.asarray(reference_face).astype('float32')
    # mean, std = reference_array.mean(), reference_array.std()
    # reference_array = (reference_array - mean) / std
    # reference_embedding = model.predict(np.expand_dims(reference_array, axis=0))
    # reference_embedding = reference_embedding.reshape(1, -1)
    reference_embedding = embedder.embeddings([reference_array])

    # Initialize the camera
    cap = cv2.VideoCapture(0)

    # Get the current time
    start_time = time.time()

    while True:
        ret, frame = cap.read()

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Camera Timer
        elapsed_time = time.time() - start_time
        cv2.putText(frame, f'Time Remaining: {10 - int(elapsed_time)} seconds', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        if elapsed_time >= 10:
            cap.release()
            cv2.destroyAllWindows()
            return False

        # Compare detected faces with the reference face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x+10, y), (x + w-10, y + h), (0, 255, 0), 2)
            roi_gray = np.asarray(frame[y:y + h, x:x + w])
            # image = Image.fromarray(roi_gray).resize((224, 224))
            image = Image.fromarray(roi_gray)
            face_array = np.asarray(image).astype('float32')
            # mean, std = face_array.mean(), face_array.std()
            # face_array = (face_array - mean) / std
            # face_embedding = model.predict(np.expand_dims(face_array, axis=0))
            # face_embedding = face_embedding.reshape(1, -1)
            face_embedding = embedder.embeddings([face_array])

            print(cosine_similarity(reference_embedding, face_embedding)[0][0])
            if(cosine_similarity(reference_embedding, face_embedding)[0][0] > 0.8):
                cap.release()
                cv2.destroyAllWindows()
                return True   

        # Display the frame
        cv2.imshow('Face Recognition', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()
    return False