# Detects faces from the camera feed with pre-trained model MTCNN.

from mtcnn import MTCNN
import cv2

class FaceDetector:
    def __init__(self):
        self.detector = MTCNN()

    def detect_faces(self, image):
        """
        Detect faces in an image using MTCNN.
        :param image: Image as a numpy array
        :return: List of detected faces with their bounding box coordinates
        """
        faces = self.detector.detect_faces(image)
        return [face['box'] for face in faces]
