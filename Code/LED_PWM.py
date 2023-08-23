import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
PWM_PIN = 18
GPIO.setup(PWM_PIN, GPIO.OUT)
pwm = GPIO.PWM(PWM_PIN, 1000)  

pwm.start(0)
try:
    while True:
        for duty_cycle in range(0, 100, 10):  
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.5)
        for duty_cycle in range(100, -1, -10): 
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.5)
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()

