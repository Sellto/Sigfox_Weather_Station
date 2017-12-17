RPI with Raspian Jessie Stretch

sudo raspi-config
  > Interfacing options 
  > P6 Serial
  > Would you like a login shell to be accessible over serial? No
  > Would you like the serial port hardware to be enabled? Yes
  
ls -l /dev
  > Vérifier que serial 0 pointe vers ttyAMA0.
  

Install Adafruit Python Library
  > git clone https://github.com/adafruit/Adafruit_Python_DHT.git
  > cd Adafruit_Python_DHT
  > sudo apt-get update
  > sudo apt-get install build-essential python-dev python-openssl
  > sudo python setup.py install

Install Python serial library
  > pip install pyserial
