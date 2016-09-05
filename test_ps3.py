from triangula.input import SixAxis, SixAxisResource
import time

def handler(button):
    print 'Button {} pressed'.format(button)


interval = 0.01

with SixAxisResource(bind_defaults=True) as joystick:
    joystick.register_button_handler(handler, SixAxis.BUTTON_SQUARE)
    while 1:

        x = joystick.axes[0].corrected_value()
        y = joystick.axes[1].corrected_value()

        print(x,y)

        time.sleep(interval)
