import gpiozero
import time

# 0.45
servo = gpiozero.AngularServo(
    14,
    initial_angle=0,
    min_angle=-5,
    max_angle=5,
)

print("STARting")
time.sleep(4)
servo.angle = 5
print("YAAA")
time.sleep(2)
servo.angle = -5
print("Stoping !!")
time.sleep(2)
print("BABZ girl")
