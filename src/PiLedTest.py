
import time
from hal import hal_led as led
from hal import hal_input_switch as sw



def left_blink(delay):
    led.init()

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)


def right_blink(delay):
    led.init()

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

def main():
    # Initialize LED HAL driver
    led.init()
    sw.init()

    while True:
        if sw.read_slide_switch() == 1:

            
            led.set_output(24, 1)
            left_blink(0.2)


        elif sw.read_slide_switch()== 0:
            led.set_output(24, 0)
            right_blink(0.1)

main()