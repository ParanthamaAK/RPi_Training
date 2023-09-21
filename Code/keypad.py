import RPi.GPIO as GPIO
import time

row = [25, 12, 13, 19]
col = [17, 18, 27, 22]

GPIO.setmode(GPIO.BCM)
GPIO.setup(row, GPIO.OUT)
GPIO.setup(col, GPIO.IN, pull_up_down=GPIO.PUD_UP)

keypad = {
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
  for rows in range(4):
    GPIO.output(row[rows], GPIO.LOW)
    for cols in range(4):
      if not GPIO.input(col[cols]):
        return (rows, cols)
    GPIO.output(row[rows], GPIO.HIGH)

def main():
  while True:
    button = read_keypad()
    if button:
      print(keypad[button])

if __name__ == "__main__":
  main()

