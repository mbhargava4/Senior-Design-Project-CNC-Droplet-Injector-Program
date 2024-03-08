from pyfirmata import Arduino, util
import time

# Set up the Arduino board
board = Arduino('/dev/ttyUSB0')  # Change '/dev/ttyUSB0' to the port where your Arduino is connected

# Define pins
step_pin = 2  # Step pin
dir_pin = 3   # Direction pin

# Set the pins as OUTPUT
board.digital[step_pin].mode = pyfirmata.OUTPUT
board.digital[dir_pin].mode = pyfirmata.OUTPUT

# Define the delay between steps (adjust for your motor)
step_delay = 0.01

# Define the number of steps per revolution (adjust for your motor)
steps_per_revolution = 200

# Function to move the stepper motor
def move_stepper(steps, direction):
    # Set the direction
    board.digital[dir_pin].write(direction)

    # Step the motor
    for _ in range(steps):
        board.digital[step_pin].write(1)
        time.sleep(step_delay)
        board.digital[step_pin].write(0)
        time.sleep(step_delay)

try:
    # Move the stepper motor 360 degrees clockwise
    move_stepper(steps_per_revolution, 1)  # 1 for clockwise, 0 for counterclockwise

    # Pause for a moment
    time.sleep(1)

    # Move the stepper motor 360 degrees counterclockwise
    move_stepper(steps_per_revolution, 0)

except KeyboardInterrupt:
    # If the user interrupts the program, stop the motor and close the board connection
    board.digital[step_pin].write(0)
    board.exit()
