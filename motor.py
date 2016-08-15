import RPi.GPIO as GPIO # Import the GPIO Library

class Motor:

    def __init__(self):
        #Set up GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        # Set variables for the GPIO motor pins
        self.pinMotorAForwards = 9 
        self.pinMotorABackwards = 10
        self.pinMotorBForwards = 8
        self.pinMotorBBackwards = 7

        # How many times to turn the pin on and off each second
        self.Frequency = 20
        # How long the pin stays on each cycle, as a percent
        self.DutyCycleA = 41
        self.DutyCycleB = 40
        # Setting the duty cycle to 0 means the motors will not turn
        self.Stop = 0

        # Set the GPIO Pin mode to be Output
        GPIO.setup(self.pinMotorAForwards, GPIO.OUT)
        GPIO.setup(self.pinMotorABackwards, GPIO.OUT)
        GPIO.setup(self.pinMotorBForwards, GPIO.OUT)
        GPIO.setup(self.pinMotorBBackwards, GPIO.OUT)

        # Set the GPIO to software PWM at 'Frequency' Hertz
        self.pwmMotorAForwards = GPIO.PWM(self.pinMotorAForwards, self.Frequency)
        self.pwmMotorABackwards = GPIO.PWM(self.pinMotorABackwards, self.Frequency)
        self.pwmMotorBForwards = GPIO.PWM(self.pinMotorBForwards, self.Frequency)
        self.pwmMotorBBackwards = GPIO.PWM(self.pinMotorBBackwards, self.Frequency)

        # Start the software PWM with a duty cycle of 0 (i.e. not moving)
        self.pwmMotorAForwards.start(self.Stop)
        self.pwmMotorABackwards.start(self.Stop)
        self.pwmMotorBForwards.start(self.Stop)
        self.pwmMotorBBackwards.start(self.Stop)

    # Turn all motors off
    def StopMotors(self):
        self.pwmMotorAForwards.ChangeDutyCycle(self.Stop)
        self.pwmMotorABackwards.ChangeDutyCycle(self.Stop)
        self.pwmMotorBForwards.ChangeDutyCycle(self.Stop)
        self.pwmMotorBBackwards.ChangeDutyCycle(self.Stop)

# Turn both motors forwards
    def Forwards(self):
        self.pwmMotorAForwards.ChangeDutyCycle(self.DutyCycleA)
        self.pwmMotorABackwards.ChangeDutyCycle(self.Stop)
        self.pwmMotorBForwards.ChangeDutyCycle(self.DutyCycleB)
        self.pwmMotorBBackwards.ChangeDutyCycle(self.Stop)

# Turn both motors backwards
    def Backwards(self):
        self.pwmMotorAForwards.ChangeDutyCycle(self.Stop)
        self.pwmMotorABackwards.ChangeDutyCycle(self.DutyCycleA)
        self.pwmMotorBForwards.ChangeDutyCycle(self.Stop)
        self.pwmMotorBBackwards.ChangeDutyCycle(self.DutyCycleB)

# Turn left
    def Right(self):
        self.pwmMotorAForwards.ChangeDutyCycle(self.Stop)
        self.pwmMotorABackwards.ChangeDutyCycle(self.DutyCycleA)
        self.pwmMotorBForwards.ChangeDutyCycle(self.DutyCycleB)
        self.pwmMotorBBackwards.ChangeDutyCycle(self.Stop)

# Turn Right
    def Left(self):
        self.pwmMotorAForwards.ChangeDutyCycle(self.DutyCycleA)
        self.pwmMotorABackwards.ChangeDutyCycle(self.Stop)
        self.pwmMotorBForwards.ChangeDutyCycle(self.Stop)
        self.pwmMotorBBackwards.ChangeDutyCycle(self.DutyCycleB)

    def CleanUp(self):
        GPIO.cleanup()
