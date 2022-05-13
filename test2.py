from tkinter import *
from tkinter import ttk
from time import *
from uart import *

dT = 500
ser = Uart()
fConnect = False
fLog = False

# Root window
root = Tk()
root.title('to MPS2')


# Log
frameLog = LabelFrame(root, text='log')
frameLog.grid(column=0, row=0, sticky='nsew', padx=10, pady=10)

textLog = Text(frameLog)
textLog.grid(column=0, row=0, sticky='nsew', padx=10, pady=10)

frameLog.grid_rowconfigure(0, weight=1)
frameLog.grid_columnconfigure(0, weight=1)

# serial
frameSerial = LabelFrame(root, text='J18', )
frameSerial.grid(column=0, row=3, sticky='nsew', padx=10, pady=10)
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
frameCommand.grid(column=0, row=2, sticky='nsew', padx=10, pady=10)
frameCommand.columnconfigure(0, weight=1)
frameCommand.rowconfigure(0, weight=1)
cmdSend = ttk.Button(frameCommand, text='send')
cmdSend.grid(column=2, row=0, sticky='w', padx=10, pady=10)
entrCmd = Entry(frameCommand, text='', )
entrCmd.grid(column=0, row=0, padx=10, pady=10, sticky='nsew', columnspan=2)
cmdLog = ttk.Button(frameCommand, text='log ON')
cmdLog.grid(column=3, row=0, sticky='n', padx=10, pady=10)


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


def update():
    global fConnect
    if fConnect:
        re = ser.readLN()
        textLog.insert('end', re)
        textLog.yview(END)

    root.after(dT, update)

root.after(dT, update())

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)





root.mainloop()

