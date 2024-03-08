import math
from pyfirmata import Arduino, util
import time

# Arduino board setup
board = Arduino('/dev/ttyUSB0')  # Change this to your serial port

# Define Arduino pins for stepper motor control
step_pin = 2
dir_pin = 3

# Constants
steps_per_revolution = 200  # Change this according to your stepper motor specifications

def move_stepper_motor(pitch, lead, distance):
    # Calculate the number of steps required
    num_steps = int(distance * steps_per_revolution * pitch / (math.pi * lead))

    # Determine the direction based on the sign of distance
    direction = 1 if distance >= 0 else 0

    # Set the direction pin
    board.digital[dir_pin].write(direction)

    # Pulse the step pin to move the motor
    for _ in range(num_steps):
        board.digital[step_pin].write(1)
        time.sleep(0.001)  # Adjust delay as needed for your motor
        board.digital[step_pin].write(0)
        time.sleep(0.001)  # Adjust delay as needed for your motor

# Example usage
if __name__ == "__main__":
    pitch = float(input("Enter the pitch of the screw (in meters): "))
    lead = float(input("Enter the lead of the screw (in meters): "))
    distance = float(input("Enter the linear distance to move (in meters): "))

    move_stepper_motor(pitch, lead, distance)

# Cleanup
board.exit()
