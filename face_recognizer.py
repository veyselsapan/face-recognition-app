# Implements the facial recognition logic. 
# This involve loading the pre-trained model FaceNet, 
# extracting embeddings from detected faces, and comparing these embeddings with those stored in the database.

from keras_facenet import FaceNet
import numpy as np

class FaceRecognizer:
    def __init__(self):
        self.embedder = FaceNet()

    def get_embedding(self, image):
        """
        Generate a face embedding for the given image.
        """
        detections = self.embedder.extract(image, threshold=0.95)
        if detections:
            return detections[0]['embedding']  # Assuming one face per image
        return None

    def compare_faces(self, emb1, emb2):
        """
        Compare two face embeddings.
        """
        return np.linalg.norm(emb1 - emb2)
