import gpiozero
import time

servo = gpiozero.AngularServo(
    14,
    min_pulse_width=(1 - 0.45) / 1000,
    max_pulse_width=2.45 / 1000,
)

print("STARting")
time.sleep(2)
servo.angle = 0
time.sleep(2)
servo.angle = 45
print("YAAA")
time.sleep(2)
servo.angle = -45
print("Stoping !!")
time.sleep(2)
servo.angle = 0
