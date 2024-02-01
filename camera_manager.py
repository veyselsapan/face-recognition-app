# Handles camera operations using OpenCV, captures the video stream, and supplies images to the face detector and recognizer.

import cv2

class CameraManager:
    def __init__(self):
        self.cap = None
        self.start_camera()

    def start_camera(self):
        """Start or restart the camera."""
        if self.cap is not None:
            self.cap.release()
        self.cap = cv2.VideoCapture(0)

    def capture_image(self):
        """Capture a single image from the camera."""
        if self.cap is None or not self.cap.isOpened():
            self.start_camera()
        ret, frame = self.cap.read()
        if ret:
            return frame
        return None

    def stop_camera(self):
        """Stop the camera."""
        if self.cap is not None:
            self.cap.release()
            self.cap = None

    def release(self):
        """Release the camera resource."""
        self.stop_camera()
