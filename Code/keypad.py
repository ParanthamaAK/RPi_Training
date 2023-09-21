import RPi.GPIO as GPIO
import time

# Define the row and column pins of the keypad
ROW_PINS = [25, 12, 13, 19]
COL_PINS = [17, 18, 27, 22]

# Initialize the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(ROW_PINS, GPIO.OUT)
GPIO.setup(COL_PINS, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Create a dictionary to map the keypad buttons to characters
KEYPAD_MAP = {
    (1, 0): "1",
    (1, 1): "2",
    (1, 2): "3",
    (1, 3): "A",
    (2, 0): "4",
    (2, 1): "5",
    (2, 2): "6",
    (2, 3): "B",
    (3, 0): "7",
    (3, 1): "8",
    (3, 2): "9",
    (3, 3): "C",
    (4, 0): "*",
    (4, 1): "0",
    (4, 2): "#",
    (4, 3): "D",
}

def read_keypad():
  """Reads the keypad and returns the pressed button, or None if no button is pressed."""
  for row in range(4):
    GPIO.output(ROW_PINS[row], GPIO.LOW)
    for col in range(4):
      if not GPIO.input(COL_PINS[col]):
        return (row, col)
    GPIO.output(ROW_PINS[row], GPIO.HIGH)

def main():
  """The main loop that reads the keypad and prints the pressed button."""
  while True:
    button = read_keypad()
    if button:
      print(KEYPAD_MAP[button])

if __name__ == "__main__":
  main()

