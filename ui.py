# Builds the user interface with Tkinter. Includes elements like buttons, labels, and a video display panel.

import tkinter as tk
from tkinter import messagebox, simpledialog
from camera_manager import CameraManager
from face_detector import FaceDetector
from face_recognizer import FaceRecognizer
from database_manager import DatabaseManager
from PIL import Image, ImageTk
import cv2
import numpy as np

class Application:
    def __init__(self, window, window_title, face_recognizer):
        self.window = window
        self.window.title(window_title)
        
        self.face_recognizer = face_recognizer
        self.camera = CameraManager()
        self.face_detector = FaceDetector()
        self.database = DatabaseManager('faces.db')

        # The canvas size
        self.canvas = tk.Canvas(window, width=600, height=500)
        self.canvas.pack()

        self.btn_capture = tk.Button(window, text="Capture Image", command=self.capture_image)
        self.btn_capture.pack(anchor=tk.CENTER, expand=True)

        self.btn_recognize = tk.Button(window, text="Recognize Face", command=self.recognize_face)
        self.btn_recognize.pack(anchor=tk.CENTER, expand=True)

        # Button to add a new face
        self.btn_add_face = tk.Button(window, text="Add Face to Database", command=self.add_face_to_database)
        self.btn_add_face.pack(anchor=tk.CENTER, expand=True)

        # Button to clear the canvas
        self.btn_clear_canvas = tk.Button(window, text="Clear Canvas", command=self.clear_canvas)
        self.btn_clear_canvas.pack(anchor=tk.CENTER, expand=True)
        self.start_camera()
        self.window.mainloop()

    def start_camera(self):
        """Ensure the camera is ready for capturing images."""
        self.camera.start_camera()

    def capture_image(self):
        """Capture an image, display it, and stop the camera."""
        self.image = self.camera.capture_image()
        if self.image is not None:
            self.display_image(self.image)
            self.camera.stop_camera()
            
    def display_image(self, image):
        self.current_image = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)))
        # Keep a reference to the image object
        self.canvas.image = self.current_image
        self.canvas.create_image(0, 0, image=self.current_image, anchor=tk.NW)

    def clear_canvas(self):
        # Clear the canvas
        self.canvas.delete("all")
        
    def recognize_face(self):
        if self.image is not None:
            embedding = self.face_recognizer.get_embedding(self.image)
            if embedding is not None:
                min_distance = float('inf')
                recognized_label = None
                for label, known_embedding in self.database.get_all_faces():
                    # Convert embedding string back to numpy array
                    known_embedding_np = np.frombuffer(known_embedding, dtype=np.float32)
                    distance = self.face_recognizer.compare_faces(embedding, known_embedding_np)
                    if distance < min_distance:
                        min_distance = distance
                        recognized_label = label
                if recognized_label is not None:
                    messagebox.showinfo("Result", f"Recognized as {recognized_label}")
                else:
                    messagebox.showinfo("Result", "Face not recognized")
            else:
                messagebox.showinfo("Result", "No face detected")

    def add_face_to_database(self):
        if self.image is not None:
            # Get label for the new face
            label = simpledialog.askstring("Input", "Who is this?")
            if label:
                embedding = self.face_recognizer.get_embedding(self.image)
                if embedding is not None:
                    # Convert numpy array to bytes for storage
                    embedding_bytes = embedding.tobytes()
                    self.database.add_face(label, embedding_bytes)
                    messagebox.showinfo("Result", "Face added to database")
                else:
                    messagebox.showinfo("Result", "No face detected")
