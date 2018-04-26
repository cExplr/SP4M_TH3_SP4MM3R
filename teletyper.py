from pynput.mouse import Button, Controller

mouse=Controller() ;
mouse.move(514,947);
mouse.click(Button.left,1)

from pynput.keyboard import Key, Controller

keyboard = Controller()
keyboard.type("This is done by a script")

import time

time.sleep(0.5)

mouse.move(-514,-947)
keyboard.press(Key.enter);
