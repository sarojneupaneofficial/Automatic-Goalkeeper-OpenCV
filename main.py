# main.py

import cv2
from ball_detection import detect_ball
from servo_control import move_servo, cleanup   # <-- updated module name
from data_logger import log_ball_position
import time

# --- Video capture ---
cap = cv2.VideoCapture(0)  # 0 = default camera
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# --- Goal area (visualization) ---
goal_top = int(frame_height * 0.7)
goal_bottom = frame_height
goal_left = int(frame_width * 0.3)
goal_right = int(frame_width * 0.7)

# --- Servo angle mapping ---
def map_x_to_servo(x, frame_width):
    """
    Map x-coordinate of ball to servo angle (0-180)
    """
    angle = int((x / frame_width) * 180)
    return angle

print("Automatic Goalkeeper started. Press ESC to quit.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Flip frame for mirror effect
        frame = cv2.flip(frame, 1)

        # Detect ball
        ball = detect_ball(frame)
        if ball:
            x, y = ball
            # Move servo
            servo_angle = map_x_to_servo(x, frame_width)
            move_servo(servo_angle)
            # Log position
            log_ball_position(x, y)

        # Draw goal area
        cv2.rectangle(frame, (goal_left, goal_top), (goal_right, goal_bottom), (255, 0, 0), 2)

        # Display frame
        cv2.imshow("Automatic Goalkeeper", frame)

        # Exit on ESC
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break

finally:
    # Cleanup
    cap.release()
    cv2.destroyAllWindows()
    cleanup()
    print("Program exited safely.")
