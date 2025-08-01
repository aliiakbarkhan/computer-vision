# Computer Vision Projects

<img src = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/540afe45-6f30-4279-8198-f4c56bb14f61/dim1zlx-5af23ef9-3ecc-41ec-b3f9-9102280e8289.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzU0MGFmZTQ1LTZmMzAtNDI3OS04MTk4LWY0YzU2YmIxNGY2MVwvZGltMXpseC01YWYyM2VmOS0zZWNjLTQxZWMtYjNmOS05MTAyMjgwZTgyODkuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.RBbAj8CoX5XnzmOIH8sYdTd7Jf24nVRZOUw3wGMTGW8" />

This repository contains a collection of computer vision projects implemented using Python and the OpenCV library. The projects demonstrate various applications of computer vision, from real-time gesture recognition to face detection.

## Projects

### 1\. Face Recognition

This project uses a pre-trained deep learning model to perform real-time face detection and recognition. It can identify individuals from a dataset of images and draw bounding boxes around their faces.

**Key Features:**

  - Real-time face detection.
  - Recognition of known faces.
  - Ability to add new faces to the dataset.


### 2\. Volume Control using Gesture

This project allows you to control your computer's volume by making hand gestures. It uses computer vision to detect hand landmarks and interpret specific gestures to increase or decrease the system volume.

**Key Features:**

  - Gesture-based volume control.
  - Real-time hand tracking.
  - Works with a standard webcam.


### 3\. Mouse Control using Gesture

Control your mouse cursor and perform clicks using hand gestures. This project tracks the tip of your index finger to move the cursor and recognizes a specific gesture (e.g., closing your fist) as a click.

**Key Features:**

  - Hand gesture-based mouse movement.
  - Virtual click functionality.
  - Customizable sensitivity.


### 4\. Auto Selfie Capture using Gesture

Capture selfies automatically by making a specific hand gesture. This project detects the gesture (e.g., a "peace" sign) and, after a short delay, captures a picture, providing a hands-free way to take photos.

**Key Features:**

  - Gesture-triggered selfie capture.
  - Countdown timer for convenience.
  - Saves the captured images to a specified directory.

## Prerequisites

To run these projects, you need to have the following installed:

  - **Python 3.x**
  - **OpenCV**
  - **Mediapipe** (for projects involving hand gestures)
  - **PyAutoGUI** (for mouse control)
  - **Pycaw** (for volume control on Windows)

You can install the required Python libraries using `pip`:

```bash
pip install opencv-python mediapipe pyautogui pycaw
```

## How to Run

1.  Clone this repository:

    ```bash
    git clone https://github.com/aliiakbarkhan/computer-vision.git
    ```

2.  Navigate to the project directory:

    ```bash
    cd computer-vision
    ```

3.  Run the desired project:

    ```bash
    python project_name.py
    ```

    (e.g., `python face_recognition.py`)

## Contributing

Contributions are welcome\! If you have any ideas for new projects or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
