import cv2
import time
import numpy as np
import base64
from io import BytesIO
from PIL import Image
from HelperFiles import embedder
from sklearn.metrics.pairwise import cosine_similarity

def detect_matching_face(encoded_photo):
    #Can Cache this into Database
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    reference_face = Image.open(BytesIO(base64.b64decode(encoded_photo)))
    reference_array = np.asarray(reference_face).astype('float32')
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
        cv2.putText(frame, f'Time Remaining: {10 - int(elapsed_time)} seconds', (100, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (205, 105, 15), 2)
        if elapsed_time >= 10:
            cap.release()
            cv2.destroyAllWindows()
            return False

        # Compare detected faces with the reference face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x+10, y), (x + w-10, y + h), (0, 255, 0), 2)
            face_array = np.asarray(frame[y:y + h, x:x + w]).astype('float32')
            face_embedding = embedder.embeddings([face_array])

            #print(cosine_similarity(reference_embedding, face_embedding)[0][0])
            if(cosine_similarity(reference_embedding, face_embedding)[0][0] > 0.8):
                cap.release()
                cv2.destroyAllWindows()
                return True   

        # Display the frame
        cv2.imshow('Face Recognition', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()
    return False