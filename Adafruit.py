import Adafruit_DHT
import struct

class DHT(object):
    def __init__(self, sensor, gpio):
        self.humidity, self.temperature = Adafruit_DHT.read_retry(sensor, pin)

    def float_to_hex(self,f):
        return hex(struct.unpack('<I', struct.pack('<f', f))[0])[2:]

    def sigfox_msg(self):
        return "{0}{1}".format(self.float_to_hex(self.humidity),self.float_to_hex(self.temperature))
