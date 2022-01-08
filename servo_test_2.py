import gpiozero
import time

servo= gpiozero.AngularServo(14)

print("STARting")
time.sleep(2)
servo.angle= 0
time.sleep(2)
servo.angle= 45
time.sleep(2)
servo.angle = -90
print("Stoping !!")
