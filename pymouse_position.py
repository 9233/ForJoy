from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
m = PyMouse()
k = PyKeyboard()
while True:
    print m.position()
    time.sleep(3)
