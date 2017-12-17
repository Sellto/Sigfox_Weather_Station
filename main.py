from Sigfox import Sigfox
from Adafruit import DHT
import sys
from time import sleep

if __name__ == '__main__':
    wtr = DHT(11, 4)
    sgfx = Sigfox('/dev/ttyAMA0')
    sgfx.send_message(wtr.sigfox_msg())
    # time.sleep(600) #mise en sommeil pendant 10 mn
