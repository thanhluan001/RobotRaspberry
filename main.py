import time # Import the Time library
import curses
import os
import camera
from multiprocessing import Process
from motor import Motor

#set up curses
stdscr = curses.initscr()
curses.cbreak()
#curses.noecho()
stdscr.keypad(True)
#stdscr.timeout(100)
curses.halfdelay(1)

#setting camera
p = Process(target=camera.run) 
p.start()

#set up motor
motor = Motor()

# Your code to control the robot goes below this line
#Forwards()
#time.sleep(3) # Pause for 1 second

#stdscr.nodelay(1)
key =''
delay = 0
num_try = 3
while key != ord('q'):
  key = stdscr.getch()
  if key == curses.KEY_UP or key == ord('w'):
    motor.Forwards()
    delay = 0
  elif key == curses.KEY_DOWN:
    motor.Backwards()
    delay = 0
  elif key == curses.KEY_LEFT:
    motor.Left()
    delay = 0
  elif key == curses.KEY_RIGHT:
    motor.Right()
    delay = 0
  elif key == -1:
    if delay >= num_try:
      motor.StopMotors()
    else:
      delay += 1
  #StopMotors()

#clean up
curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()

#shut down camera
p.terminate()

motor.CleanUp()
del motor
