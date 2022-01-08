from gpiozero import Servo
from time import sleep

servo = Servo(14)

while True:
    servo.min()
    print("min")
    sleep(2)
    servo.mid()
    print("mid")
    sleep(2)
    servo.max()
    print("max")
    sleep(2)
