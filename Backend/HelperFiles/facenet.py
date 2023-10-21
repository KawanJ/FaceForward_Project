import tensorflow
import numpy as np
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity

model = tensorflow.keras.applications.ResNet50(weights='imagenet')

image1 = Image.open('D:\Projects\FaceForwardProject\FaceForward_Project\Backend\HelperFiles\KJ.jpg').resize((224, 224))
face_array1 = np.asarray(image1).astype('float32')
mean, std = face_array1.mean(), face_array1.std()
face_array1 = (face_array1 - mean) / std

embedding1 = model.predict(np.expand_dims(face_array1, axis=0))

image2 = Image.open('D:\Projects\FaceForwardProject\FaceForward_Project\Backend\HelperFiles\SOD.jpg').resize((224, 224))
face_array2 = np.asarray(image2).astype('float32')
mean, std = face_array2.mean(), face_array2.std()
face_array2 = (face_array2 - mean) / std

embedding2 = model.predict(np.expand_dims(face_array2, axis=0))

embedding1 = embedding1.reshape(1, -1)  # Reshape to a 2D array
embedding2 = embedding2.reshape(1, -1)  # Reshape to a 2D array

# Calculate cosine similarity between the embeddings
similarity_score = cosine_similarity(embedding1, embedding2)[0][0]

# Print the similarity score
print("Cosine Similarity Score:", similarity_score)