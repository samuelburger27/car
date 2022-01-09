import gpiozero
import time

# 0.45
servo = gpiozero.AngularServo(
    14,
    initial_angle=-15,
    min_angle=-90,
    max_angle=90,
    min_pulse_width=(1 - 0.45) / 1000,
    max_pulse_width=2.45 / 1000,
)

print("STARting")
time.sleep(4)
servo.angle = 15
print("YAAA")
time.sleep(2)
servo.angle = -15
print("Stoping !!")
time.sleep(2)
print("BABZ girl")
