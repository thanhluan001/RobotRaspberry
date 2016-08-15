import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO pins to use on the Pi
pinTrigger = 17
pinEcho = 18

print("Ultrasonic Measurement")

# Set pins as output and input
GPIO.setup(pinTrigger, GPIO.OUT) # Trigger
GPIO.setup(pinEcho, GPIO.IN) # Echo

try:
    while True:
        #set trigger to False
        GPIO.output(pinTrigger, False)

        #Allow module to settle
        time.sleep(0.5)

        #Send 10us pulse to trigger
        GPIO.output(pinTrigger, True)
        time.sleep(0.00001)
        GPIO.output(pinTrigger, False)

        StartTime = time.time()

        #The start time is reset until the Echo Pin is taken high (==1)
        while GPIO.input(pinEcho)==0:
            StartTime = time.time()

        #Stop when the Echo pin in no longer high - the end time
        while GPIO.input(pinEcho)==1:
            StopTime = time.time()

        #If too close
        if StopTime - StartTime >= 0.04:
            print("Hold on there! You're too close")
            StopTime = StartTime
            break

        #Calculate pulse length
        ElapsedTime = StopTime - StartTime

        #Distance pulse travelled 
        Distance = ElapsedTime * 34326

        # The distance is there and back
        Distance = Distance / 2

        print("Distance: %.1f cm" % Distance)

        time.sleep(0.5)
    
#IF Ctrl-C, clean up
except KeyboardInterrupt:
    # Reset GPIO
    GPIO.cleanup()



