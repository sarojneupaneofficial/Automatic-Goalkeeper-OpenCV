import cv2
import numpy as np

# HSV color range for orange ball
LOWER_ORANGE = np.array([5, 150, 150])
UPPER_ORANGE = np.array([15, 255, 255])

def detect_ball(frame):
    """
    Detect the ball in the given frame.
    Returns (x, y) coordinates of the ball center or None if not found.
    """
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, LOWER_ORANGE, UPPER_ORANGE)
    mask = cv2.medianBlur(mask, 5)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    ball_center = None

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 300:  # filter small noise
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            ball_center = (int(x), int(y))
            cv2.circle(frame, ball_center, int(radius), (0, 255, 0), 2)
            cv2.putText(frame, "Ball", (ball_center[0]-20, ball_center[1]-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
            break

    return ball_center
