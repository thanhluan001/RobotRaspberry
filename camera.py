from SimpleCV import Camera, Display
import time

def run():
    cam = Camera()
    display = Display()

    img = cam.getImage()
    img.save(display)

    while not display.isDone():
        img = cam.getImage()  
        img.save(display)

        time.sleep(0.1)

    print('Done') 
