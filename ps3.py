import pygame, sys, time, os
from pygame.locals import *

os.environ['SDL_VIDEODRIVER'] = 'dummy'

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
pygame.display.init()
#screen = pygame.display.set_mode((400,300))
#screen = pygame.display.set_mode((1, 1))

pygame.display.set_caption('Hello World')

interval = 0.01

# get count of joysticks=1, axes=27, buttons=19 for DualShock 3

joystick_count = pygame.joystick.get_count()
print("joystick_count")
print(joystick_count)
print("--------------")

numaxes = joystick.get_numaxes()
print("numaxes")
print(numaxes)
print("--------------")

numbuttons = joystick.get_numbuttons()
print("numbuttons")
print(numbuttons)
print("--------------")

loopQuit = False
while loopQuit == False:
    # test joystick axes
    # outstr = ""

    outstr = ""
    for i in range(0, numbuttons):
        button = joystick.get_button(i)
        outstr = outstr + str(i) + ":" + str(button) + "|"
    print (outstr)

    for event in pygame.event.get():
        if event.type == QUIT:
            loopQuit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loopQuit = True

    time.sleep(interval)

pygame.quit()
sys.exit()
