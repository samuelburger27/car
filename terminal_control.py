import gpiozero
import time
import curses

wheels = gpiozero.Robot(left=(25, 21), right=(1, 7))

servo = gpiozero.AngularServo(
    pin=14,
    initial_angle=0,
    min_angle=-90,
    max_angle=90,
    min_pulse_width=(1 - 0.45) / 1000,
    max_pulse_width=2.45 / 1000,
)

speed = 1

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
screen.nodelay(True)

try:
    while True:
        char = screen.getch()
        if char == ord('q'):  # quit
            break
        if char == ord('w'):  # forward
            wheels.forward(speed)

        elif char == ord('s'):  # bacward
            wheels.backward(speed)

        if char == ord('b'):  # stop
            wheels.stop()

        if char == ord('a'):  # turn left
            servo.angle = 30
            time.sleep(0.5)
            servo.angle = 0.0
        elif char == ord('d'):  # turn righ
            servo.angle = -30
            time.sleep(0.5)
            servo.angle = 0.0
        else:
            servo.angle = 0.0
            time.sleep(0.5)
except KeyboardInterrupt:
    pass
curses.nocbreak()
screen.keypad(0)
curses.echo()
curses.endwin()
print("DONE")


#####################################################################
