import serial
import time

baudrate = 115200

com_buffer = b''

currentPort = serial.Serial(
    port='COM20',
    baudrate=int(baudrate),
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    #timeout=0.5, # IMPORTANT, can be lower or higher
    # inter_byte_timeout=0.1 # Alternative
    )

print(currentPort)


def readlnPort():
    t = time.time()
    buffer = b''
    t_wait = 3
    count = 0
    if currentPort == 0:
        job = False
    else:
        job = True
    while job:
        if time.time() < t + t_wait:
            if currentPort.inWaiting():
                c = currentPort.read()  # attempt to read a character from Serial
                #print(c)
                if c == b'\r':
                    pass
                elif c == b'\n':
                    pass  # add the newline to the buffer
                    job = False
                else:
                    buffer += c  # add to the buffer
                    count += 1
        else:
            buffer = b''
            job = False
    return count, buffer

#for i  in range(10):
job = False
while job:
    n, com_buffer = readlnPort()
    if n>0:
        print()
        print(com_buffer)
        if com_buffer == 'Power supply is ready':
            job = False

    else:
        print('.', end='')

cmd = 'log filtered-adcs\r\n'
currentPort.write(cmd.encode('ascii'))
print(currentPort.readline().decode('ascii'))
re = currentPort.readline().decode('ascii')
print(re)

cmd = 'log\r\n'
currentPort.write(cmd.encode('ascii'))
print(currentPort.readline().decode('ascii'))

def send_cmd(command):
    strcmd = str(command) + '\r\n'
    currentPort.write(strcmd.encode('ascii'))
    print(currentPort.readline().decode('ascii'))
    re = currentPort.readline().decode('ascii')
    return re



def get_log(command):
    strcmd = 'log ' + str(command) + '\r\n'
    currentPort.write(strcmd.encode('ascii'))
    print(currentPort.readline().decode('ascii'))
    re = currentPort.readline().decode('ascii')
    cmd = 'log\r\n'
    currentPort.write(cmd.encode('ascii'))
    print(currentPort.readline().decode('ascii'))
    return re


cmd = 'filtered-adcs'
print(get_log(cmd))

cmd = 'fan 0.2'
print(send_cmd(cmd))

time.sleep(2)

cmd = 'filtered-adcs'
print(get_log(cmd))

cmd = 'fan 0'
print(send_cmd(cmd))

cmd = 'mode main-coil'
print (send_cmd(cmd))

currentPort.close()