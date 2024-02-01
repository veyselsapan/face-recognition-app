# Orchestrates the high-level application flow, initializes the GUI, and links the GUI with the backend functionalities

from ui import Application
from face_recognizer import FaceRecognizer
import tkinter as tk

def main():
    # Initialize the FaceRecognizer
    face_recognizer = FaceRecognizer()
    
    # Create the main application window
    root = tk.Tk()
    app = Application(root, "Facial Recognition System", face_recognizer)
    
    # Start the application
    root.mainloop()

if __name__ == "__main__":
    main()
