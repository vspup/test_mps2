from tkinter import *
from tkinter import ttk
from time import *
from uart import *


dT = 50


ctime = time.localtime()

nameLogFile = "./log/log_" + str(ctime.tm_year) + '_' + str(ctime.tm_mon) + '_' + str(ctime.tm_mday) + '_' + str(ctime.tm_hour) \
            + '_' + str(ctime.tm_min) + '_' +  str(ctime.tm_sec) + ".txt"
print(nameLogFile)


ser = Uart()
fConnect = False
fLog = False
fileLog = open(nameLogFile, 'w')


# Root window
root = Tk()
root.title('to MPS2')
root.grid_columnconfigure(0, weight=1, uniform="fred")
root.grid_columnconfigure(1, weight=1, uniform="fred")


# Log
frameLog = LabelFrame(root, text='log')
frameLog.grid(column=0, row=0, sticky='nsew', padx=10, pady=10, columnspan=2)

textLog = Text(frameLog)
textLog.grid(column=0, row=0, sticky='nsew', padx=10, pady=10)

frameLog.grid_rowconfigure(0, weight=1)
frameLog.grid_columnconfigure(0, weight=1)


# serial
frameSerial = LabelFrame(root, text='serial', )
frameSerial.grid(column=0, row=4, sticky='nsew', padx=10, pady=10)
frameSerial.columnconfigure(0, weight=1)
frameSerial.rowconfigure(0, weight=1)
# serial
comboSerial = ttk.Combobox(frameSerial, values=ser.getListPort())
comboSerial.grid(column=0, row=0, sticky='nsew', padx=10, pady=10)
comboSerial.current(0)
cmdConnectSerial = Button(frameSerial, text="Connect", bg="light grey")
cmdConnectSerial.grid(column=1, row=0, padx=10, pady=10, sticky='nsew')



# send command
frameCommand = LabelFrame(root, text='send CMD', )
frameCommand.grid(column=0, row=2, sticky='nsew', padx=10, pady=10, columnspan=2)
frameCommand.columnconfigure(0, weight=1)
frameCommand.rowconfigure(0, weight=1)
cmdSend = ttk.Button(frameCommand, text='send')
cmdSend.grid(column=2, row=0, sticky='w', padx=10, pady=10)
entrCmd = Entry(frameCommand, text='', )
entrCmd.grid(column=0, row=0, padx=10, pady=10, sticky='nsew', columnspan=2)
cmdLog = ttk.Button(frameCommand, text='log ON')
cmdLog.grid(column=3, row=0, sticky='n', padx=10, pady=10)
cmdMain = ttk.Button(frameCommand, text='on Main')
cmdMain.grid(column=4, row=0, sticky='n', padx=10, pady=10)



# send main
frameMain = LabelFrame(root, text='main', )
frameMain.grid(column=0, row=3, sticky='nsew', padx=10, pady=10)
frameMain.columnconfigure(2, weight=1)
frameMain.rowconfigure(0, weight=1)


cmdClearI = ttk.Button(frameMain, text='set I=0')
cmdClearI.grid(column=0, row=0, sticky='w', padx=10, pady=10)
cmdSetI = ttk.Button(frameMain, text='set I')
cmdSetI.grid(column=1, row=0, sticky='w', padx=10, pady=10)
entrI = Entry(frameMain, text='', )
entrI.grid(column=2, row=0, padx=10, pady=10, sticky='nsew')

cmdClearU = ttk.Button(frameMain, text='set U=0')
cmdClearU.grid(column=0, row=1, sticky='w', padx=10, pady=10)
cmdSetU = ttk.Button(frameMain, text='set V')
cmdSetU.grid(column=1, row=1, sticky='w', padx=10, pady=10)
entrU = Entry(frameMain, text='', )
entrU.grid(column=2, row=1, padx=10, pady=10, sticky='nsew')

cmdClearFan = ttk.Button(frameMain, text='set Fan=0')
cmdClearFan.grid(column=0, row=2, sticky='w', padx=10, pady=10)
cmdSetFan = ttk.Button(frameMain, text='fan')
cmdSetFan.grid(column=1, row=2, sticky='w', padx=10, pady=10)
entrFan = Entry(frameMain, text='', )
entrFan.grid(column=2, row=2, padx=10, pady=10, sticky='nsew')


# send pch
framePsh = LabelFrame(root, text='psh', )
framePsh.grid(column=1, row=3, sticky='nsew', padx=10, pady=10)
#framePsh.columnconfigure(0, weight=1)
#framePsh.columnconfigure(1, weight=1)
framePsh.columnconfigure(2, weight=1)
framePsh.rowconfigure(0, weight=1)
framePsh.rowconfigure(1, weight=1)
framePsh.rowconfigure(2, weight=1)

cmdPshMainClear = ttk.Button(framePsh, text='psh Main I=0')
cmdPshMainClear.grid(column=0, row=0, sticky='w', padx=10, pady=10)
cmdPshMain = ttk.Button(framePsh, text='psh Main I')
cmdPshMain.grid(column=1, row=0, sticky='w', padx=10, pady=10)
entrPshMainI = Entry(framePsh, text='', )
entrPshMainI.grid(column=2, row=0, padx=10, pady=10, sticky='nsew')

cmdPshAxClear = ttk.Button(framePsh, text='psn Ax I=0')
cmdPshAxClear.grid(column=0, row=1, sticky='w', padx=10, pady=10)
cmdPshAx = ttk.Button(framePsh, text='psn Ax I')
cmdPshAx.grid(column=1, row=1, sticky='w', padx=10, pady=10)
entrPshAxI = Entry(framePsh, text='', )
entrPshAxI.grid(column=2, row=1, padx=10, pady=10, sticky='nsew')

cmdPsh = ttk.Button(framePsh, text='psh')
cmdPsh.grid(column=0, row=2, sticky='w', padx=10, pady=10)
cmdDis = ttk.Button(framePsh, text='Ch Diss')
cmdDis.grid(column=1, row=2, sticky='w', padx=10, pady=10)
entrDis = Entry(framePsh, text='', )
entrDis.grid(column=2, row=2, padx=10, pady=10, sticky='nsew')

def loging(st):
    seconds = time.time()
    ree = str(round(seconds, 3)) + ' ' + st
    textLog.insert('end', ree)
    textLog.yview(END)
    fileLog.write(ree)


def connect():
    global fConnect, fLog
    if not fConnect:
        ser.connectPort(comboSerial.get(), int(115200))
        if str(ser.currentPort) != '0':
            print('Connect ' + str(ser.currentPort))
            loging('Connect ' + str(ser.currentPort) + '\n')
            time.sleep(1)
            fConnect = True
            cmdConnectSerial['text'] = "ConnecteD"

        else:
            cmdConnectSerial['text'] = "Connect"
            ser.disconnectPort()
            fConnect = False
    else:
        cmdConnectSerial['text'] = "Connect"
        ser.disconnectPort()
        fConnect = False
        cmdLog['text'] = "log ON"
        fLog = False

cmdConnectSerial['command'] = connect


def send():
    global fConnect
    #
    if fConnect:
        strcmd = str(entrCmd.get()) + '\r\n'
        loging(strcmd)
        print(strcmd, end='')
        ser.write(strcmd)

cmdSend['command'] = send

# set I
def setI():
    global fConnect
    #
    if fConnect:
        strcmd = 'mainCurrent ' + str(entrI.get()) + '\r\n'
        print(strcmd, end='')
        ser.write(strcmd)
        loging(strcmd)

cmdSetI['command'] = setI

def clearI():
    global fConnect
    #
    if fConnect:
        strcmd = 'mainCurrent 0\r\n'
        print(strcmd, end='')
        ser.write(strcmd)
        loging(strcmd)

cmdClearI['command'] = clearI

# set U
def setU():
    global fConnect
    #
    if fConnect:
        strcmd = 'mainVoltage ' + str(entrU.get()) + '\r\n'
        print(strcmd, end='')
        ser.write(strcmd)
        loging(strcmd)

cmdSetU['command'] = setU


def clearU():
    global fConnect
    #
    if fConnect:
        strcmd = 'mainVoltage 0\r\n'
        print(strcmd, end='')
        ser.write(strcmd)
        loging(strcmd)

cmdClearU['command'] = clearU

# fan
def setFan():
    global fConnect
    #
    if fConnect:
        strcmd = 'fan ' + str(entrFan.get()) + '\r\n'
        print(strcmd, end='')
        ser.write(strcmd)
        loging(strcmd)

cmdSetFan['command'] = setFan

def clearFan():
    global fConnect
    #
    if fConnect:
        strcmd = 'fan 0\r\n'
        print(strcmd, end='')
        ser.write(strcmd)
        loging(strcmd)

cmdClearFan['command'] = clearFan

# psh main
def setPshMain():
    global fConnect
    #
    if fConnect:
        strcmd = 'psh 0 ' + str(entrPshMainI.get()) + '\r\n'
        print(strcmd, end='')
        ser.write(strcmd)
        loging(strcmd)

cmdPshMain['command'] = setPshMain


def setPshMainClear():
    global fConnect
    #
    if fConnect:
        strcmd = 'psh 0 0\r\n'
        print(strcmd, end='')
        ser.write(strcmd)
        loging(strcmd)

cmdPshMainClear['command'] = setPshMainClear


# psh Ax
def setPshAx():
    global fConnect
    #
    if fConnect:
        strcmd = 'psh 3 ' + str(entrPshAxI.get()) + '\r\n'
        print(strcmd, end='')
        ser.write(strcmd)
        loging(strcmd)

cmdPshAx['command'] = setPshAx

def setPshAxClear():
    global fConnect
    #
    if fConnect:
        strcmd = 'psh 3 0\r\n'
        print(strcmd, end='')
        ser.write(strcmd)
        loging(strcmd)

cmdPshAxClear['command'] = setPshAxClear

# diss ch
def setDis():
    global fConnect
    #
    if fConnect:
        strcmd = 'dissipationTest ' + str(entrDis.get()) + '\r\n'
        print(strcmd, end='')
        ser.write(strcmd)
        loging(strcmd)

cmdDis['command'] = setDis


# psh
def setPsh():
    global fConnect
    #
    if fConnect:
        strcmd = 'psh \r\n'
        print(strcmd, end='')
        ser.write(strcmd)
        loging(strcmd)

cmdPsh['command'] = setPsh



def log():
    global fConnect
    global fLog
    if fConnect:
        if not fLog:
            cmdLog['text'] = "log OFF"
            cmd = 'log filtered-adcs\r\n'
            ser.write(cmd)
            loging(cmd)
            fLog = True

        else:
            cmdLog['text'] = "log ON"
            cmd = 'log\r\n'
            ser.write(cmd)
            loging(cmd)
            fLog = False

cmdLog['command'] = log


fMain = False
def modeMain():
    global fConnect
    global fMain
    if fConnect:
        if not fMain:
            cmdMain['text'] = "Disable"
            cmd = 'mode main-coil\r\n'
            ser.write(cmd)
            loging(cmd)
            fMain = True

        else:
            cmdMain['text'] = "on Main"
            cmd = 'disable\r\n'
            ser.write(cmd)
            loging(cmd)
            fMain = False

cmdMain['command'] = modeMain

def update():
    global fConnect
    if fConnect:
        re = ser.readLN()
        if re != '':
            loging(re)

    root.after(dT, update)

root.after(dT, update())

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)





root.mainloop()

