# function uart
# vpupkov@digitsi.com

import serial
import serial.tools.list_ports
import time


class Uart:
    def __init__(self):
        # get list of uart available
        self.ports = serial.tools.list_ports.comports()
        self.listUart = []
        for port, desc, hwid in sorted(self.ports):
            print("{}: {} [{}]".format(port, desc, hwid))
            self.listUart.append(port)
        print(self.listUart)
        self.currentPort = 0
        self.buffer = b''

    def getListPort(self):
        return self.listUart

    def connectPort(self, name, baudrate):
        self.currentPort = serial.Serial(
            port=name,
            baudrate=int(baudrate),
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0.002,  # IMPORTANT, can be lower or higher
            # inter_byte_timeout=0.1 # Alternative
        )

    def getCurrentPort(self):
        return self.currentPort

    def disconnectPort(self):
        self.currentPort.close()
        self.currentPort = 0

    def readlnPort(self):
        t = time.time()
        self.buffer = b''
        t_wait = 0.8
        count = 0
        if self.currentPort == 0:
            job = False
        else:
            job = True
        while job:
            if time.time() < t + t_wait:
                if self.currentPort.inWaiting():
                    c = self.currentPort.read()  # attempt to read a character from Serial
                    print(c)
                    if c == b'\r':
                        pass
                    elif c == b'\n':
                        pass  # add the newline to the buffer
                        job = False
                    else:
                        self.buffer += c  # add to the buffer
                        count += 1
            else:
                self.buffer = b''
                job = False
        return count

    def transmit(self, command, jmax):
        # massiv on re
        replya = []
        reply = ''
        # send command
        # print(command.encode('ascii'))

        self.currentPort.write(command.encode('ascii'))

        j = 0
        while j < jmax:
            # print (j)
            c = self.currentPort.read()
            # print('.', end="")
            # print(c)
            if c != b'':
                # print("[{}]".format(hex(ord(c))), end='')
                if c == b'\n':
                    break
                if (c == b'\r'):
                    pass
                else:
                    replya.append(c.decode('ascii'))
            # time.sleep(0.01)
            j = j + 1

        # print('\n')
        print('re = {}'.format(replya))
        for ch in replya:
            reply = reply + ch
        return reply

    def send(self, command):
        cmd = str(command) + '\r\n'
        self.currentPort.write(cmd.encode('ascii'))

    def read(self):
        t = time.time()
        self.buffer = b''
        t_wait = 1.5
        count = 0
        if self.currentPort == 0:
            job = False
        else:
            job = True
        while job:
            if time.time() < t + t_wait:
                if self.currentPort.inWaiting():
                    c = self.currentPort.read()  # attempt to read a character from Serial
                    # print (c)
                    self.buffer += c  # add to the buffer
                    count += 1
                    # print (self.buffer)
            else:
                job = False

        return count

    def getBuffer(self):
        return self.buffer


    def write(self, command):

        self.currentPort.write(command.encode('ascii'))

    def readLN(self):
        # need re = self.currentPort.readline().decode('ascii')
        # UnicodeDecodeError: 'ascii' codec can't decode byte 0xfe in position 5: ordinal not in range(128)
        rend = self.currentPort.readline()
        print(rend)
        ree = b''
        for ch in rend:
            #print(ch)
            if int(ch) <= 128:
                num_bytes = int(ch).to_bytes(1, byteorder='big')
                ree = ree + num_bytes
        #re = self.currentPort.readline().decode('ascii')
        re = ree
        return re