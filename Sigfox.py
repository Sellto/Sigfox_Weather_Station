#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial


class Sigfox(object):
    SOH = chr(0x01)
    STX = chr(0x02)
    EOT = chr(0x04)
    ACK = chr(0x06)
    NAK = chr(0x15)
    CAN = chr(0x18)
    CRC = chr(0x43)

    def __init__(self, port):
        # permet de choisir le port série – par défaut /dev/ttyAMA0
        portName = port

        print('Serial port : ' + portName)

        self.ser = serial.Serial(
            port=portName,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS
        )

    def getc(self, size, timeout=1):
        return ser.read(size)

    def putc(self, data, timeout=1):
        ser.write(data)
        # temporisation pour permettre au circuit de se préparer
        sleep(0.001)

    #Status de la commande Serie exéxutée.
    def WaitFor(self, success, failure, timeOut):
        return self.receive_until(success, failure, timeOut) != ''

    def receive_until(self, success, failure, timeOut):
        iterCount = timeOut / 0.1
        self.ser.timeout = 0.1
        currentMsg = ''
        while iterCount >= 0 and success not in currentMsg and failure not in currentMsg:
            sleep(0.1)
            while self.ser.inWaiting() > 0:  # bunch of data ready for reading
                c = self.ser.read()
                currentMsg += c
            iterCount -= 1
        if success in currentMsg:
            return currentMsg
        elif failure in currentMsg:
            print('Erreur (' + currentMsg.replace('\r\n', '') + ')')

        else:
            print('Délai de réception dépassé (' + currentMsg.replace('\r\n', '') + ')')
        return ''

    def send_message(self,message):
        print('Sending SigFox Message...')
        if (self.ser.isOpen() == True):  # sur certaines plateformes il faut d'abord fermer le port série
            self.ser.close()
        try:
            self.ser.open()
        except serial.SerialException as e:
            sys.stderr.write("Ouverture du port série impossible {}: {}\n".format(ser.name, e))
            sys.exit(1)

        #Vérification du Port Série
        self.ser.write('AT\r')
        if self.WaitFor('OK', 'ERROR', 3):
            print('SigFox Modem OK')
            self.ser.write("AT$SF={0}\r".format(message))
            print('Envoi des données ...')
            if self.WaitFor('OK', 'ERROR', 15):
                print('OK Message envoyé')
        else:
            print('Erreur Modem SigFox')
        self.ser.close()
