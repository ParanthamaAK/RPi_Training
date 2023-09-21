import serial
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
led = 18
GPIO.setup(led, GPIO.OUT)


pwm = GPIO.PWM(led, 100)

ser = serial.Serial('/dev/ttyS0', 115200, timeout=1)

try:
    while True:
        data = ser.readline().decode().strip()
        if data:
            try:
                rec = int(data)
                print("Received:", rec)
                if 0 <= rec <= 100:
                    pwm.start(rec)
            except ValueError:
                print("Received non-integer data:", data)
        ser.reset_input_buffer()
except KeyboardInterrupt:
    pass
finally:
    pwm.stop() 
    GPIO.cleanup()
    ser.close()
