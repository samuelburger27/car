import gpiozero
import time

servo = gpiozero.AngularServo(
    14,
    0,
)

print("STARting")
time.sleep(2)
servo.angle = 0
time.sleep(2)
servo.angle = 20
print("YAAA")
time.sleep(2)
servo.angle = 0
print("Stoping !!")
