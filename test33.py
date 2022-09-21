from tkinter import *
from tkinter import ttk
from time import *
from uart import *


dT = 50





ser = Uart()
fConnect = False
fLog = False
fFLog = False


# Root window
root = Tk()
root.title('to MPS2')
root.grid_columnconfigure(0, weight=1, uniform="fred")
root.grid_columnconfigure(1, weight=1, uniform="fred")


# Log
frameLog = LabelFrame(root, text='log')
frameLog.grid(column=0, row=0, sticky='nsew', padx=10, pady=10, columnspan=3)

textLog = Text(frameLog)
textLog.grid(column=0, row=0, sticky='nsew', padx=10, pady=10)

frameLog.grid_rowconfigure(0, weight=1)
frameLog.grid_columnconfigure(0, weight=1)


# serial
frameSerial = LabelFrame(root, text='serial', )
frameSerial.grid(column=0, row=3, sticky='nsew', padx=10, pady=10)
frameSerial.columnconfigure(0, weight=1)
frameSerial.rowconfigure(0, weight=1)
# serial
comboSerial = ttk.Combobox(frameSerial, values=ser.getListPort())
comboSerial.grid(column=0, row=0, sticky='nsew', padx=10, pady=10)
comboSerial.current(0)
cmdConnectSerial = Button(frameSerial, text="Connect", bg="light grey")
cmdConnectSerial.grid(column=1, row=0, padx=10, pady=10, sticky='nsew')

# log filles
frameLogF = LabelFrame(root, text='file', )
frameLogF.grid(column=1, row=3, sticky='nsew', padx=10, pady=10)
frameLogF.columnconfigure(0, weight=1)
frameLogF.rowconfigure(0, weight=1)
cmdFLog = ttk.Button(frameLogF, text='start write')
cmdFLog.grid(column=0, row=0, sticky='w', padx=10, pady=10)
entrPL = Entry(frameLogF, text='', )
entrPL.grid(column=1, row=0, padx=10, pady=10, sticky='nsew')

# send command
frameCommand = LabelFrame(root, text='send CMD', )
frameCommand.grid(column=0, row=1, sticky='nsew', padx=10, pady=10, columnspan=3)
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
frameMain.grid(column=0, row=2, sticky='nsew', padx=10, pady=10)
frameMain.columnconfigure(2, weight=1)
frameMain.rowconfigure(0, weight=1)


cmdClearI = ttk.Button(frameMain, text='set I=0')
cmdClearI.grid(column=0, row=0, sticky='w', padx=10, pady=10)
cmdSetI = ttk.Button(frameMain, text='set I')
cmdSetI.grid(column=1, row=0, sticky='w', padx=10, pady=10)
entrI = Entry(frameMain, text='', )
entrI.grid(column=2, row=0, padx=10, pady=10, sticky='nsew')
cmdUpI = ttk.Button(frameMain, text='+')
cmdUpI.grid(column=3, row=0, sticky='w', padx=10, pady=10)
cmdDownI = ttk.Button(frameMain, text='-')
cmdDownI.grid(column=4, row=0, sticky='w', padx=10, pady=10)

cmdClearU = ttk.Button(frameMain, text='set U=0')
cmdClearU.grid(column=0, row=1, sticky='w', padx=10, pady=10)
cmdSetU = ttk.Button(frameMain, text='set V')
cmdSetU.grid(column=1, row=1, sticky='w', padx=10, pady=10)
entrU = Entry(frameMain, text='', )
entrU.grid(column=2, row=1, padx=10, pady=10, sticky='nsew')
cmdUpU = ttk.Button(frameMain, text='+')
cmdUpU.grid(column=3, row=1, sticky='w', padx=10, pady=10)
cmdDownU = ttk.Button(frameMain, text='-')
cmdDownU.grid(column=4, row=1, sticky='w', padx=10, pady=10)


cmdClearFan = ttk.Button(frameMain, text='set Fan=0')
cmdClearFan.grid(column=0, row=2, sticky='w', padx=10, pady=10)
cmdSetFan = ttk.Button(frameMain, text='fan')
cmdSetFan.grid(column=1, row=2, sticky='w', padx=10, pady=10)
entrFan = Entry(frameMain, text='', )
entrFan.grid(column=2, row=2, padx=10, pady=10, sticky='nsew')
cmdUpFan = ttk.Button(frameMain, text='+')
cmdUpFan.grid(column=3, row=2, sticky='w', padx=10, pady=10)
cmdDownFan = ttk.Button(frameMain, text='-')
cmdDownFan.grid(column=4, row=2, sticky='w', padx=10, pady=10)


# send pch
framePsh = LabelFrame(root, text='psh', )
framePsh.grid(column=1, row=2, sticky='nsew', padx=10, pady=10)
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


# diss
frameDiss = LabelFrame(framePsh, text='dissipation', )
frameDiss.grid(column=1, row=2, sticky='nsew', padx=10, pady=10, columnspan=3)

cmdDissPrep = ttk.Button(frameDiss, text='Prep Diss')
cmdDissPrep.grid(column=0, row=0, sticky='w', padx=10, pady=10)
cmdDis0 = ttk.Button(frameDiss, text='Ch Diss 0')
cmdDis0.grid(column=1, row=0, sticky='w', padx=10, pady=10)
cmdDis1 = ttk.Button(frameDiss, text='Ch Diss 1')
cmdDis1.grid(column=2, row=0, sticky='w', padx=10, pady=10)

entrDis = Entry(frameDiss, text='', )
entrDis.grid(column=3, row=0, padx=10, pady=10, sticky='nsew')


# p modules
frameMod = LabelFrame(root, text='pwm-test', )
frameMod.grid(column=2, row=2, sticky='nsew', padx=10, pady=10)

cmdModeMod = ttk.Button(frameMod, text='on pwm-test')
cmdModeMod.grid(column=0, row=0, sticky='w', padx=10, pady=10)

cmdLogMod = ttk.Button(frameMod, text='on log modules')
cmdLogMod.grid(column=1, row=0, sticky='w', padx=10, pady=10)

cmdModCh = ttk.Button(frameMod, text='set ch')
cmdModCh.grid(column=0, row=1, sticky='w', padx=10, pady=10)
entrModCh = Entry(frameMod, text='', )
entrModCh.grid(column=1, row=1, padx=10, pady=10, sticky='nsew')

cmdModDuty = ttk.Button(frameMod, text='set duty')
cmdModDuty.grid(column=0, row=2, sticky='w', padx=10, pady=10)
entrModDuty = Entry(frameMod, text='', )
entrModDuty.grid(column=1, row=2, padx=10, pady=10, sticky='nsew')


def loging(st):
    seconds = time.time()
    #ree = str(round(seconds, 3)) + ' ' + st
    textLog.insert('end', st)
    textLog.yview(END)
    if fFLog:
        ree = str(round(seconds, 3)) + ' ' + st
        fileLog.write(ree)


def connect():
    global fConnect, fFLog, fileLog
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
            if fFLog:
                cmdFLog['text'] = 'start write'
                fileLog.close()
                fFLog = False
    else:
        cmdConnectSerial['text'] = "Connect"
        ser.disconnectPort()
        fConnect = False
        if fFLog:
            cmdFLog['text'] = 'start write'
            fileLog.close()
            fFLog = False


cmdConnectSerial['command'] = connect


###########
def logfile():
    global fConnect, fFLog, fileLog


    if not fFLog:


        ctime = time.localtime()

        nameLogFile = "./log/" + str(entrPL.get()) + '_' + str(ctime.tm_year) + '_' + str(ctime.tm_mon) \
                      + '_' + str(ctime.tm_mday) + '_' + str(ctime.tm_hour) \
                      + '_' + str(ctime.tm_min) + '_' + str(ctime.tm_sec) + ".txt"
        print(nameLogFile)
        fileLog = open(nameLogFile, 'w')
        fFLog = True
        cmdFLog['text'] = "stop files"

    else:
        cmdFLog['text'] = 'start write'
        fileLog.close()
        fFLog = False

cmdFLog['command'] = logfile



###########

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
        entrI.delete(0, END)
        entrI.insert(0, '0')

cmdClearI['command'] = clearI


def upI():
    global fConnect
    #
    if fConnect:
        val = entrI.get()

        newValR = (float(val) + float(0.1))
        newVal = "{:.2f}".format(newValR)
        strcmd = 'mainCurrent ' + newVal + '\r\n'
        print(strcmd, end='')
        ser.write(strcmd)
        loging(strcmd)
        entrI.delete(0, END)
        entrI.insert(0, newVal)


cmdUpI['command'] = upI


def downI():
    global fConnect
    #
    if fConnect:
        val = entrI.get()

        if float(val) >= 0.1:
            newValR = (float(val) - float(0.1))
            newVal = "{:.2f}".format(newValR)
            strcmd = 'mainCurrent ' + newVal + '\r\n'
            print(strcmd, end='')
            ser.write(strcmd)
            loging(strcmd)
            entrI.delete(0, END)
            entrI.insert(0, newVal)


cmdDownI['command'] = downI

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
        entrU.delete(0, END)
        entrU.insert(0, '0')

cmdClearU['command'] = clearU

def upU():
    global fConnect
    #
    if fConnect:
        val = entrU.get()
        print(float(0.05))
        print(int(0.05))
        if float(val) < 10:
            newValR = (float(val) + float(0.01))
            newVal = "{:.2f}".format(newValR)
            strcmd = 'mainVoltage ' + newVal + '\r\n'
            print(strcmd, end='')
            ser.write(strcmd)
            loging(strcmd)
            entrU.delete(0, END)
            entrU.insert(0, newVal)


cmdUpU['command'] = upU

def downU():
    global fConnect
    #
    if fConnect:
        val = entrU.get()

        if float(val) >= 0.01:
            newValR = (float(val) - float(0.01))
            newVal = "{:.2f}".format(newValR)
            strcmd = 'mainVoltage ' + newVal + '\r\n'
            print(strcmd, end='')
            ser.write(strcmd)
            loging(strcmd)
            entrU.delete(0, END)
            entrU.insert(0, newVal)

cmdDownU['command'] = downU

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
        entrFan.delete(0, END)
        entrFan.insert(0, '0')

cmdClearFan['command'] = clearFan


def upFan():
    global fConnect
    #
    if fConnect:
        val = entrFan.get()
        print(float(0.05))
        print(int(0.05))
        if float(val) < 0.9:
            newFanR = (float(val) + float(0.05))
            newFan = "{:.2f}".format(newFanR)
            strcmd = 'fan ' + newFan + '\r\n'
            print(strcmd, end='')
            ser.write(strcmd)
            loging(strcmd)
            entrFan.delete(0, END)
            entrFan.insert(0, newFan)

cmdUpFan['command'] = upFan

def downFan():
    global fConnect
    #
    if fConnect:
        val = entrFan.get()

        if float(val) > 0.1:
            newFanR = (float(val)-float(0.05))
            newFan = "{:.2f}".format(newFanR)
            strcmd = 'fan ' + newFan + '\r\n'

            print(strcmd, end='')
            ser.write(strcmd)
            loging(strcmd)
            entrFan.delete(0, END)
            entrFan.insert(0, newFan)

cmdDownFan['command'] = downFan

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
        entrPshMainI.delete(0, END)
        entrPshMainI.insert(0, '0')

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
        entrPshAxI.delete(0, END)
        entrPshAxI.insert(0, '0')

cmdPshAxClear['command'] = setPshAxClear


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

# diss ch

def setPrep():
    global fConnect
    #
    if fConnect:
        strcmd = 'mainVoltage 0\r\n'
        print(strcmd, end='')
        ser.write(strcmd)
        loging(strcmd)
        entrU.delete(0, END)
        entrU.insert(0, '0')
        sleep(2)

        strcmd = 'mainCurrent 0\r\n'
        print(strcmd, end='')
        ser.write(strcmd)
        loging(strcmd)
        entrI.delete(0, END)
        entrI.insert(0, '0')
        sleep(2)

        strcmd = 'fan 0.6\r\n'
        print(strcmd, end='')
        ser.write(strcmd)
        loging(strcmd)
        entrFan.delete(0, END)
        entrFan.insert(0, '0.6')

cmdDissPrep['command'] = setPrep

def setDis1():
    global fConnect
    #
    if fConnect:
        strcmd = 'dissipationTest 1\r\n'
        print(strcmd, end='')
        ser.write(strcmd)
        loging(strcmd)

cmdDis1['command'] = setDis1

def setDis0():
    global fConnect
    #
    if fConnect:
        strcmd = 'dissipationTest 0\r\n'
        print(strcmd, end='')
        ser.write(strcmd)
        loging(strcmd)

cmdDis0['command'] = setDis0





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

## pwm-test
fMod = False
def modeMod():
    global fConnect
    global fMod
    if fConnect:
        if not fMod:
            cmdModeMod['text'] = "Disable"
            cmd = 'mode pwm-test\r\n'
            ser.write(cmd)
            loging(cmd)
            fMod = True

        else:
            cmdModeMod['text'] = "on pwm-test"
            cmd = 'disable\r\n'
            ser.write(cmd)
            loging(cmd)
            fMod = False

cmdModeMod['command'] = modeMod

fModLog = False
def logMod():
    global fConnect
    global fModLog
    if fConnect:
        if not fModLog:
            cmdLogMod['text'] = "log OFF"
            cmd = 'log modules\r\n'
            ser.write(cmd)
            loging(cmd)
            fModLog = True

        else:
            cmdLogMod['text'] = "log ON"
            cmd = 'log\r\n'
            ser.write(cmd)
            loging(cmd)
            fModLog = False

cmdLogMod['command'] = logMod

# select ch
fCh = False
def setCh():
    global fConnect, fCh
    #
    if fConnect:
        if not fCh:
            cmdModCh['text'] = "dis Ch"
            strcmd = 'module ' + str(entrModCh.get()) + ' enable \r\n'
            print(strcmd, end='')
            ser.write(strcmd)
            loging(strcmd)
            fCh = True
        else:
            cmdModCh['text'] = "en Ch"
            strcmd = 'module ' + str(entrModCh.get()) + ' disable \r\n'
            print(strcmd, end='')
            ser.write(strcmd)
            loging(strcmd)
            fCh = False


cmdModCh['command'] = setCh

# duty


def setDuty():
    global fConnect, fCh

    if fConnect:
        if fCh:

            strcmd = 'duty ' + str(entrModCh.get()) + ' 0 ' + str(entrModDuty.get()) + ' \r\n'
            #strcmd = 'duty 0 0 0.02 \r\n'
            print(strcmd, end='')
            ser.write(strcmd)
            loging(strcmd)



cmdModDuty['command'] = setDuty

###

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

