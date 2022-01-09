import gpiozero
import time

servo = gpiozero.AngularServo(
    14,
    initial_angle=0,
    min_pulse_width=(1 - 0.45) / 1000,
    max_pulse_width=2.45 / 1000,
)

print("STARting")
time.sleep(2)
servo.angle = 25
print("YAAA")
time.sleep(2)
servo.angle = -25
print("Stoping !!")
time.sleep(2)
print("BABZ girl")
