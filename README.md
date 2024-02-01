# Facial Recognition Access Control

This project is a facial recognition system designed to identify individuals for secure access control, such as turnstile entry systems. It uses a camera to detect and recognize faces in real-time, allowing for the addition of new individuals to the system and providing immediate access control based on facial recognition.

## Features

- Real-time face detection and recognition using a camera feed.
- Add new individuals' faces to the system for recognition.
- Database support for storing facial data.
- Simple graphical user interface for easy operation.

## Installation

Ensure you have Python 3.6+ installed on your system. Then, clone this repository and install the required dependencies:

git clone https://github.com/veyselsapan/face-recognizer-app.git
cd face-recognizer-app
pip install -r requirements.txt

## Usage

To start the application, run:

python main.py

The GUI will launch, providing options to capture images from the camera, recognize faces, and add new faces to the database.

## Technologies

- Python
- TensorFlow and Keras for facial recognition (using the Keras-FaceNet model).
- SQLite for database management.
- OpenCV for camera operations.
- Tkinter for the graphical user interface.

## Contributing

Contributions to this project are welcome. Please feel free to fork the repository, make changes, and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
