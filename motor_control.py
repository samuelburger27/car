import time
import gpiozero

wheels = gpiozero.Robot(left=(25, 8), right=(1, 7))

wheels.forward()
time.sleep(6)

wheels.stop()
