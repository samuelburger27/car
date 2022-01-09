from gpiozero.pins.pigpio import PiGPIOFactory
import gpiozero
import time

# 0.45
factory = PiGPIOFactory(host="192.168.1.43")
servo = gpiozero.AngularServo(
    pin_factory=factory,
    pin=14,
    initial_angle=0,
    min_angle=-90,
    max_angle=90,
    min_pulse_width=(1 - 0.45) / 1000,
    max_pulse_width=2.45 / 1000,
)

print("STARting")
time.sleep(4)
servo.angle = 25
print("YAAA")
time.sleep(2)
servo.angle = -25
print("Stoping !!")
time.sleep(2)
print("BABZ girl")
