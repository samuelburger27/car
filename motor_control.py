import time
import gpiozero

wheels = gpiozero.Robot(left=(25, 8), right=(1, 7))

wheels.forward()
time.sleep(3)
wheels.right()
time.sleep(3)
wheels.left()
time.sleep(3)
wheels.stop()