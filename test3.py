from tkinter import *
from tkinter import ttk
from time import *
from uart import *


dT = 50


ctime = time.localtime()

nameLogFile = "log_" + str(ctime.tm_year) + '_' + str(ctime.tm_mon) + '_' + str(ctime.tm_mday) + '_' + str(ctime.tm_hour) \
            + '_' + str(ctime.tm_min) + '_' +  str(ctime.tm_sec) + ".txt"
print(nameLogFile)


ser = Uart()
fConnect = False
fLog = False
fileLog = open(nameLogFile, 'w')


# Root window
root = Tk()
root.title('to MPS2')


# Log
frameLog = LabelFrame(root, text='log')
frameLog.grid(column=0, row=0, sticky='nsew', padx=10, pady=10, columnspan=2)

textLog = Text(frameLog)
textLog.grid(column=0, row=0, sticky='nsew', padx=10, pady=10)

frameLog.grid_rowconfigure(0, weight=1)
frameLog.grid_columnconfigure(0, weight=1)


# serial
frameSerial = LabelFrame(root, text='J18', )
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
frameMain.columnconfigure(0, weight=1)
#frameMain.columnconfigure(1, weight=1)
frameMain.rowconfigure(0, weight=1)
#frameMain.rowconfigure(1, weight=1)
cmdSetI = ttk.Button(frameMain, text='set I')
cmdSetI.grid(column=1, row=0, sticky='w', padx=10, pady=10)
entrI = Entry(frameMain, text='', )
entrI.grid(column=0, row=0, padx=10, pady=10, sticky='nsew')
cmdSetU = ttk.Button(frameMain, text='set V')
cmdSetU.grid(column=1, row=1, sticky='w', padx=10, pady=10)
entrU = Entry(frameMain, text='', )
entrU.grid(column=0, row=1, padx=10, pady=10, sticky='nsew')
cmdSetFan = ttk.Button(frameMain, text='fan')
cmdSetFan.grid(column=1, row=2, sticky='w', padx=10, pady=10)
entrFan = Entry(frameMain, text='', )
entrFan.grid(column=0, row=2, padx=10, pady=10, sticky='nsew')


# send pch
framePsh = LabelFrame(root, text='psh', )
framePsh.grid(column=1, row=3, sticky='nsew', padx=10, pady=10)
framePsh.columnconfigure(0, weight=1)
framePsh.columnconfigure(1, weight=1)
framePsh.rowconfigure(0, weight=1)
framePsh.rowconfigure(1, weight=1)
cmdPshMain = ttk.Button(framePsh, text='psh Main I')
cmdPshMain.grid(column=1, row=0, sticky='w', padx=10, pady=10)
entrPshMainI = Entry(framePsh, text='', )
entrPshMainI.grid(column=0, row=0, padx=10, pady=10, sticky='nsew')
cmdPshAx = ttk.Button(framePsh, text='psn Ax I')
cmdPshAx.grid(column=1, row=1, sticky='w', padx=10, pady=10)
entrPshAxI = Entry(framePsh, text='', )
entrPshAxI.grid(column=0, row=1, padx=10, pady=10, sticky='nsew')
cmdDis = ttk.Button(framePsh, text='Ch Diss')
cmdDis.grid(column=1, row=2, sticky='w', padx=10, pady=10)
entrDis = Entry(framePsh, text='', )
entrDis.grid(column=0, row=2, padx=10, pady=10, sticky='nsew')




def connect():
    global fConnect, fLog
    if not fConnect:
        ser.connectPort(comboSerial.get(), int(115200))
        if str(ser.currentPort) != '0':
            print('Connect ' + str(ser.currentPort))
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

cmdSetI['command'] = setI


# set U
def setU():
    global fConnect
    #
    if fConnect:
        strcmd = 'mainVoltage ' + str(entrU.get()) + '\r\n'
        print(strcmd, end='')
        ser.write(strcmd)

cmdSetU['command'] = setU


# fan
def setFan():
    global fConnect
    #
    if fConnect:
        strcmd = 'fan ' + str(entrFan.get()) + '\r\n'
        print(strcmd, end='')
        ser.write(strcmd)

cmdSetFan['command'] = setFan


# psh main
def setPshMain():
    global fConnect
    #
    if fConnect:
        strcmd = 'psh 0 ' + str(entrPshMainI.get()) + '\r\n'
        print(strcmd, end='')
        ser.write(strcmd)

cmdPshMain['command'] = setPshMain


# psh Ax
def setPshAx():
    global fConnect
    #
    if fConnect:
        strcmd = 'psh 3 ' + str(entrPshAxI.get()) + '\r\n'
        print(strcmd, end='')
        ser.write(strcmd)

cmdPshAx['command'] = setPshAx


# diss ch
def setDis():
    global fConnect
    #
    if fConnect:
        strcmd = 'dissipationTest ' + str(entrDis.get()) + '\r\n'
        print(strcmd, end='')
        ser.write(strcmd)

cmdDis['command'] = setDis

def log():
    global fConnect
    global fLog
    if fConnect:
        if not fLog:
            cmdLog['text'] = "log OFF"
            cmd = 'log filtered-adcs\r\n'
            ser.write(cmd)
            fLog = True

        else:
            cmdLog['text'] = "log ON"
            cmd = 'log\r\n'
            ser.write(cmd)
            fLog = False

cmdLog['command'] = log


fMain = False
def modeMain():
    global fConnect
    global fMain
    if fConnect:
        if not fMain:
            cmdLog['text'] = "Disable"
            cmd = 'mode main-coil\r\n'
            ser.write(cmd)
            fLog = True

        else:
            cmdLog['text'] = "on Main"
            cmd = 'disable\r\n'
            ser.write(cmd)
            fLog = False

cmdMain['command'] = modeMain

def update():
    global fConnect
    if fConnect:
        re = ser.readLN()
        textLog.insert('end', re)
        textLog.yview(END)
        fileLog.write(re)

    root.after(dT, update)

root.after(dT, update())

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)





root.mainloop()

