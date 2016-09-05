from triangula.input import SixAxis, SixAxisResource
import time # Import the Time library
import os
import camera
from multiprocessing import Process
from motor import Motor

#setting camera
#p = Process(target=camera.run) 
#p.start()

#set up motor
motor = Motor()

# Your code to control the robot goes below this line
#Forwards()
#time.sleep(3) # Pause for 1 second

with SixAxisResource(bind_defaults=True) as joystick:
  
  while 1:
    x = joystick.axes[0].corrected_value()
    y = joystick.axes[1].corrected_value()

    if y == 1: 
      motor.Forwards()
      print(x, y, 'FORWARD')
    elif y == -1:
      motor.Backwards()
      print(x, y, 'BACKWARD')
    else: 
      motor.StopMotors()
      print(x, y, 'STOP')
    
    time.sleep(0.01)

#clean up

#shut down camera
#p.terminate()

motor.CleanUp()
del motor
