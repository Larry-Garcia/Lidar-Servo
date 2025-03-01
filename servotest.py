from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

# Assign servo channels
PAN_CHANNEL = 14   # Bottom servo (pan - horizontal)
TILT_CHANNEL = 15  # Top servo (tilt - vertical)

# Function to move a servo to a given angle with delay
def move_servo(channel, angle, delay=0.5):
    kit.servo[channel].angle = angle
    print(f"Servo on channel {channel} moved to {angle}°")
    time.sleep(delay)

# Initial pan-tilt positioning
def initialize_position(pan_angle=90, tilt_angle=90):
    print("Initializing Pan-Tilt Servos...")
    move_servo(PAN_CHANNEL, pan_angle, delay=1)
    move_servo(TILT_CHANNEL, tilt_angle, delay=1)

if __name__ == "__main__":
    try:
        # Initialize servos at center positions
        initialize_position()

        while True:
            # Pan motion (left → center → right → center)
            for pan_angle in [0, 90, 180, 90]:
                move_servo(PAN_CHANNEL, pan_angle, delay=1)

            # Tilt motion (down → center → up → center)
            for tilt_angle in [45, 90, 135, 90]:
                move_servo(TILT_CHANNEL, tilt_angle, delay=1)

    except KeyboardInterrupt:
        print("\nPan-Tilt control stopped by user.")
