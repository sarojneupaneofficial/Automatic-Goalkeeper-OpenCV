 ## Automatic Goalkeeper using Raspberry Pi and OpenCV

An embedded computer vision system that detects a moving football in real time and automatically positions a servo-driven goalkeeper to block incoming shots.
This project demonstrates the integration of edge computing, robotics control, and real-time image processing using Raspberry Pi and OpenCV.
Developed as part of a final-semester Technical Project course, the system simulates an intelligent defensive mechanism using low-cost hardware and vision-based tracking.

## Hardware Used

- Raspberry Pi
- Servo Motor
- Camera Module
- Breadboard
- Jumper wires
- Ball

## Software Used

- Python
- OpenCV
- NumPy

## How it Works

1. The camera captures live video.
2. OpenCV detects the moving ball.
3. The system calculates the ball position.
4. The servo motor moves the goalkeeper accordingly.
5. LED will flash after the save is being made

## Installation

Clone the repository:

git clone https://github.com/sarojneupaneofficial/automatic-goalkeeper-opencv.git

Install dependencies:

pip install -r requirements.txt

Run the program:

python main.py

## Future Improvements

- Improve ball tracking accuracy
- Add machine learning prediction
- Increase servo response speed
- Increasing Impact Ratio

  ##Author
  
  - Saroj Neupane
  - sarojneupane114@gmail.com
  - Computer Engineering Technician
  - Data Engineer
  - AI Enthusiast
