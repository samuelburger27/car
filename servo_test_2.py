import gpiozero
import time

# 0.45
servo = gpiozero.AngularServo(
    14,
    initial_angle=0,
    min_angle=-10,
    max_angle=10,
)

print("STARting")
time.sleep(4)
servo.angle = 10
print("YAAA")
time.sleep(2)
servo.angle = -10
print("Stoping !!")
time.sleep(2)
print("BABZ girl")
