import time

try:
    import RPi.GPIO as GPIO
    SERVO_AVAILABLE = True
except ImportError:
    print("RPi.GPIO not available, servo simulation only.")
    SERVO_AVAILABLE = False

if SERVO_AVAILABLE:
    GPIO.setmode(GPIO.BCM)
    SERVO_PIN = 18
    GPIO.setup(SERVO_PIN, GPIO.OUT)
    PWM = GPIO.PWM(SERVO_PIN, 50)
    PWM.start(7.5)

def move_servo(angle):
    """
    Move servo to the given angle (0-180)
    """
    if SERVO_AVAILABLE:
        duty = 2.5 + (angle / 18)
        PWM.ChangeDutyCycle(duty)
        time.sleep(0.1)
    else:
        print(f"[Servo Simulation] Move to angle: {angle}")

def cleanup():
    if SERVO_AVAILABLE:
        PWM.stop()
        GPIO.cleanup()
