#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from uart import *
from pyparsing import *
import re

mySerial = Uart()
fConnect = False
fUart = False


class Gui1Widget(tk.Frame):
    def __init__(self, master=None, **kw):
        super(Gui1Widget, self).__init__(master, **kw)
        self.textReadVoltageEntry = tk.StringVar()
        self.textReadCurrentEntry = tk.StringVar()
        self.textBCMoutEntry = tk.StringVar()
        self.textVoltageOutTerEntry = tk.StringVar()
        self.textEndOfLeadsTextEntry = tk.StringVar()

        self.textPsh0Entry = tk.StringVar()
        self.textPsh3Entry = tk.StringVar()

        self.cb = tk.BooleanVar()
        vcmd = (master.register(self.validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.mainMenu1 = tk.LabelFrame(self)
        self.mainLeftMenu1 = tk.Frame(self.mainMenu1)
        self.mainCoin = tk.LabelFrame(self.mainLeftMenu1)
        self.mainCoinText = tk.Message(self.mainCoin)
        self.mainCoinText.configure(
            font="TkHeadingFont", padx="10", text="Main coil:", width="200"
        )
        self.mainCoinText.pack(fill="x", padx="10", side="left")
        self.mainCoinBut = tk.Checkbutton(self.mainCoin)
        self.mainCoinBut.configure(text=" ", variable=self.cb, state="disable")
        self.mainCoinBut.pack(padx="10", side="left")
        self.mainCoinBut.configure(command=self.mainCoinDef)
        self.mainCoinLable = tk.Label(self.mainCoin)
        self.mainCoinLable.configure(
            font="{Arial} 10 {bold}", foreground="#ff0000", text="not ready"
        )
        self.mainCoinLable.pack(padx="10", side="right")
        self.mainCoin.configure(height="50", width="250")
        self.mainCoin.pack(padx="0", pady="5", side="top")
        self.mainCoin.pack_propagate(0)
        self.voltageSet = tk.LabelFrame(self.mainLeftMenu1)
        self.voltageSetText = tk.Label(self.voltageSet)
        self.voltageSetText.configure(text="V")
        self.voltageSetText.pack(padx="5", side="left")
        self.voltageSetEntry = tk.Entry(self.voltageSet, validate="key")

        self.voltageSetEntry['validatecommand'] = vcmd
        self.voltageSetEntry.pack(ipadx="15", padx="5", side="left")
        self.voltageSetBut = tk.Button(self.voltageSet)
        self.voltageSetBut.configure(text="Set")
        self.voltageSetBut['command'] = self.setVoltage
        self.voltageSetBut.pack(padx="10", side="left")
        self.voltageSet.configure(height="50", width="250")
        self.voltageSet.pack(padx="0", pady="5", side="top")
        self.voltageSet.pack_propagate(0)
        self.currentSet = tk.LabelFrame(self.mainLeftMenu1)
        self.currentSetText = tk.Label(self.currentSet)
        self.currentSetText.configure(text="A")
        self.currentSetText.pack(padx="5", side="left")
        self.currentSetEntry = tk.Entry(self.currentSet, validate="key")

        self.currentSetEntry['validatecommand'] = vcmd
        self.currentSetEntry.pack(ipadx="15", padx="5", side="left")
        self.currentSetBut = tk.Button(self.currentSet)
        self.currentSetBut.configure(text="Set")
        self.currentSetBut['command']=self.setCurrent
        self.currentSetBut.pack(padx="10", side="left")
        self.currentSet.configure(height="50", width="250")
        self.currentSet.pack(padx="0", pady="5", side="top")
        self.currentSet.pack_propagate(0)

        self.psk = tk.LabelFrame(self.mainLeftMenu1)
        self.psh0 = tk.LabelFrame(self.psk)
        self.psh0Label = tk.Label(self.psh0)
        self.psh0Label.configure(text="main")
        self.psh0Label.pack(padx="1", side="left")
        self.psh0Entry = tk.Entry(self.psh0, validate="key")
        self.psh0Entry['validatecommand'] = vcmd
        self.psh0Entry['textvariable'] = self.textPsh0Entry
        self.psh0Entry.pack(ipadx="15", side="left")
        self.psh0Button = tk.Button(self.psh0)
        self.psh0Button.configure(text="Set", command=self.setPsh0)
        self.psh0Button.pack(padx="10", side="left")
        self.psh0.configure(height="50", width="250",)
        self.psh0.pack(pady="10", side="top")
        self.psh0.pack_propagate(0)
        self.psh3 = tk.LabelFrame(self.psk)
        self.psh3Label = tk.Label(self.psh3)
        self.psh3Label.configure(text="axual")
        self.psh3Label.pack(padx="1", side="left")
        self.psh3Entry = tk.Entry(self.psh3, validate="key")
        self.psh3Entry['textvariable'] = self.textPsh3Entry
        self.psh0Entry['validatecommand'] = vcmd
        self.psh3Entry.pack(ipadx="15", side="left")
        self.psh3Button = tk.Button(self.psh3)
        self.psh3Button.configure(text="Set", command=self.setPsh3)
        self.psh3Button.pack(padx="10", side="left")
        self.psh3.configure(height="50", width="250")
        self.psh3.pack(pady="10", side="top")
        self.psh3.pack_propagate(0)
        self.psk.configure(height="180", width="250")
        self.psk.pack(padx="0", pady="15", side="top")
        self.psk.pack_propagate(0)

        self.mainLeftMenu1.configure(height="350", width="250")
        self.mainLeftMenu1.pack(padx="0", pady="5", side="left")
        self.mainLeftMenu1.pack_propagate(0)
        self.mainRightMenu1 = tk.Frame(self.mainMenu1)
        self.rightMenuTop = tk.LabelFrame(self.mainRightMenu1)
        self.rightMenuTopText = tk.Frame(self.rightMenuTop)
        self.readVoltageText = tk.Label(self.rightMenuTopText)
        self.readVoltageText.configure(
            font="{Arial} 12 {}", text="Voltage on circular connector:"
        )
        self.readVoltageText.pack(padx="15", side="left")
        self.readCurrentText = tk.Label(self.rightMenuTopText)
        self.readCurrentText.configure(
            font="{Arial} 12 {}", text="Total Output Current:"
        )
        self.readCurrentText.pack(padx="40", side="left")
        self.rightMenuTopText.configure(height="50", width="700")
        self.rightMenuTopText.pack(side="top")
        self.rightMenuTopText.pack_propagate(0)
        self.rightMenuTopEntry = tk.Frame(self.rightMenuTop)
        self.readVoltageEntry = tk.Entry(self.rightMenuTopEntry)
        self.readVoltageEntry.configure(font="{Arial} 12 {}", textvariable=self.textReadVoltageEntry,
                                        state="disable", disabledbackground="#f5f5f5", disabledforeground="black")
        self.readVoltageEntry.pack(ipadx="30", ipady="15", padx="10", side="left")
        self.readCurrentEntry = tk.Entry(self.rightMenuTopEntry, textvariable=self.textReadCurrentEntry,
                                        state = "disable", disabledbackground="#f5f5f5", disabledforeground="black")
        self.readCurrentEntry.configure(font="{Arial} 12 {}")
        self.readCurrentEntry.pack(ipadx="30", ipady="15", padx="5", side="left")
        self.rightMenuTopEntry.configure(height="50", width="700")
        self.rightMenuTopEntry.pack(padx="5", pady="5", side="top")
        self.rightMenuTopEntry.pack_propagate(0)
        self.rightMenuTopTextBox = tk.Frame(self.rightMenuTop)
        self.rightMenuTopTextBox1 = tk.Label(self.rightMenuTopTextBox)
        self.rightMenuTopTextBox1.configure(
            font="{Arial} 20 {bold italic}", text="Main"
        )
        self.rightMenuTopTextBox1.pack(padx="100", side="left")
        self.rightMenuTopTextBox.configure(height="50", width="700")
        self.rightMenuTopTextBox.pack(padx="5", pady="5", side="top")
        self.rightMenuTopTextBox.pack_propagate(0)
        self.rightMenuTop.configure(height="171", width="700")
        self.rightMenuTop.pack(padx="5", pady="5", side="top")
        self.rightMenuTop.pack_propagate(0)
        self.rightMenuBottom = tk.LabelFrame(self.mainRightMenu1)
        self.rightMenuBottomText = tk.Frame(self.rightMenuBottom)
        self.BCMoutText = tk.Label(self.rightMenuBottomText)
        self.BCMoutText.configure(
            font="{Arial} 10 {}", justify="left", text="Intermediate bus voltage:"
        )
        self.BCMoutText.pack(padx="15", side="left")
        self.voltageOutTerText = tk.Label(self.rightMenuBottomText)
        self.voltageOutTerText.configure(
            font="{Arial} 10 {}", relief="flat", text="Voltage at output terminals:"
        )
        self.voltageOutTerText.pack(padx="55", side="left")
        self.endOfLeadsText = tk.Label(self.rightMenuBottomText)
        self.endOfLeadsText.configure(
            font="{Arial} 10 {}", text="Voltage on circular connector: "
        )
        self.endOfLeadsText.pack(side="left")
        self.rightMenuBottomText.configure(height="40", width="700")
        self.rightMenuBottomText.pack(pady="10", side="top")
        self.rightMenuBottomText.pack_propagate(0)
        self.rightMenuBottomEntry = tk.Frame(self.rightMenuBottom)
        self.BCMoutEntry = tk.Entry(self.rightMenuBottomEntry)
        self.BCMoutEntry.configure(font="{Arial} 12 {}", textvariable=self.textBCMoutEntry,
                                          state="disable", disabledbackground="#f5f5f5", disabledforeground="black")
        self.BCMoutEntry.pack(ipadx="8", ipady="15", padx="10", side="left")
        self.voltageOutTerEntry = tk.Entry(self.rightMenuBottomEntry)
        self.voltageOutTerEntry.configure(font="{Arial} 12 {}", textvariable=self.textVoltageOutTerEntry,
                                          state="disable", disabledbackground="#f5f5f5", disabledforeground="black")
        self.voltageOutTerEntry.pack(ipadx="8", ipady="15", padx="10", side="left")
        self.endOfLeadsTextEntry = tk.Entry(self.rightMenuBottomEntry)
        self.endOfLeadsTextEntry.configure(font="{Arial} 12 {}", textvariable=self.textEndOfLeadsTextEntry,
                                           state="disable", disabledbackground="#f5f5f5", disabledforeground="black")
        self.endOfLeadsTextEntry.pack(ipadx="8", ipady="15", padx="10", side="left")
        self.rightMenuBottomEntry.configure(height="50", width="700")
        self.rightMenuBottomEntry.pack(side="top")
        self.rightMenuBottomEntry.pack_propagate(0)
        self.rightMenuBottom.configure(height="180", width="700")
        self.rightMenuBottom.pack(padx="5", pady="15", side="top")
        self.rightMenuBottom.pack_propagate(0)
        self.mainRightMenu1.configure(height="350", width="700")
        self.mainRightMenu1.pack(padx="0", pady="5", side="right")
        self.mainRightMenu1.pack_propagate(0)
        self.mainMenu1.configure(height="360", width="950")
        self.mainMenu1.pack(padx="5", pady="5", side="top")
        self.mainMenu1.pack_propagate(0)
        self.comMenu1 = ttk.Frame(self)
        self.statusCOM = ttk.Label(self.comMenu1)
        self.statusCOM.pack(padx="10", side="right")
        self.listCom = ttk.Combobox(self.comMenu1)
        self.listCom.configure(values=mySerial.getListPort())
        self.listCom.pack(padx="10", side="left")
        self.Connect = tk.Button(self.comMenu1)
        self.Connect.configure(text="Open COM port")
        self.Connect.pack(padx="10", side="left")
        self.Connect.configure(command=self.connectCOM)
        self.comMenu1.configure(height="50", width="950")
        self.comMenu1.pack(padx="5", pady="5", side="top")
        self.comMenu1.pack_propagate(0)
        self.configure(height="440", width="960")
        self.pack(side="top")

        ###
        self.LogFA = tk.Button(self.comMenu1)
        self.LogFA.configure(text="Start log")
        self.LogFA.pack(padx="10", side="left")
        self.LogFA.configure(command=self.log_fa)

        ####

        self.pack_propagate(0)


    def validate(self, action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):
        if text in '0123456789.-+':
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

    ####
    def log_fa(self):
        global fConnect
        global fUart
        global cb



    ####


    def mainCoinDef(self):
        global fConnect
        global fUart
        global cb
        if fConnect:
            if self.cb.get() == True:
                cmd_MCU = 'mode main-coil\r\n'
                reStatus = mySerial.transmit(cmd_MCU, 0)
                time.sleep(1)
                #print(reStatus)
                cmd_MCU = 'mode\r\n'
                reStatus = mySerial.transmit(cmd_MCU, 50)
                print('mode:'+reStatus)
                if reStatus == 'Current operating mode is: disabled (0)':
                    self.mainCoinLable['text'] = "ready"
                    self.mainCoinLable['foreground'] = "#00ff00"
                    fUart = True
                else:
                    self.Connect['text'] = "Open COM port"
                    cmd_MCU = 'mode disable\r\n'
                    mySerial.transmit(cmd_MCU, 0)
                    mySerial.disconnectPort()
                    #self.statusCOM['text'] = "Wrong COM"
                    self.mainCoinLable['text'] = "not ready"
                    self.mainCoinLable['foreground'] = "#ff0000"
                    self.cb.set(False)
                    fConnect = False
                    fUart = False
            else:
                cmd_MCU = 'mode disable\r\n'
                mySerial.transmit(cmd_MCU, 0)
                self.mainCoinLable['text'] = "not ready"
                self.mainCoinLable['foreground'] = "#ff0000"
                fUart = False
        else:
            self.mainCoinLable['text'] = "not ready"
            self.mainCoinLable['foreground'] = "#ff0000"
            self.cb.set(False)
            fUart = False

    def connectCOM(self):
        global fConnect
        global fUart

        if not fConnect:
            self.statusCOM["text"] = ""
            mySerial.connectPort(self.listCom.get(), int(115200))
            if str(mySerial.currentPort) != '0':
                print('Connect ' + str(mySerial.currentPort))
                time.sleep(1)
                self.Connect["state"] = "normal"
                self.Connect["text"] = "Close COM port"
                self.mainCoinBut.config(state="normal")
                fConnect = True
        else:
            self.Connect['text'] = "Open COM port"
            cmd_MCU = 'mode disable\r\n'
            mySerial.transmit(cmd_MCU, 0)
            mySerial.disconnectPort()
            print('Disconnect ' + str(mySerial.currentPort))
            self.mainCoinLable['text'] = "not ready"
            self.mainCoinLable['foreground'] = "#ff0000"
            self.mainCoinBut.config(state="disable")
            self.cb.set(False)
            fUart = False
            fConnect = False
            fUart = False

    def readMySerial(self):
        global fConnect

        if fConnect == True:
            cmd_MCU = 'log filtered-adcs\r\n'
            reStatus = mySerial.transmit(cmd_MCU, 150)
            print(reStatus)
            if len(reStatus) > 10:
                nums = re.findall(r'\d*\.\d+|\d+', reStatus)
                nums = [float(i) for i in nums]

                if len(nums) == 13:
                    self.textReadVoltageEntry.set(nums[12])
                    self.textReadCurrentEntry.set(nums[8])
                    self.textBCMoutEntry.set(nums[9])
                    self.textVoltageOutTerEntry.set(nums[10])
                    self.textEndOfLeadsTextEntry.set(nums[11])
                else:
                    self.textReadVoltageEntry.set('')
                    self.textReadCurrentEntry.set('')
                    self.textBCMoutEntry.set('')
                    self.textVoltageOutTerEntry.set('')
                    self.textEndOfLeadsTextEntry.set('')

                cmd_MCU = 'log\r\n'
                mySerial.transmit(cmd_MCU, 0)
                print('logs stoped')
            else:
                self.textReadVoltageEntry.set('')
                self.textReadCurrentEntry.set('')
                self.textBCMoutEntry.set('')
                self.textVoltageOutTerEntry.set('')
                self.textEndOfLeadsTextEntry.set('')
                cmd_MCU = 'log\r\n'
                mySerial.transmit(cmd_MCU, 0)
                print('logs stoped')
        else:
            self.textReadVoltageEntry.set('')
            self.textReadCurrentEntry.set('')
            self.textBCMoutEntry.set('')
            self.textVoltageOutTerEntry.set('')
            self.textEndOfLeadsTextEntry.set('')
        root.after(500, self.readMySerial)

    def setVoltage(self):
        global fConnect
        if fConnect == True:
            cmd_MCU = 'mainVoltage ' + self.voltageSetEntry.get() + '\r\n'
            print(cmd_MCU)
            mySerial.transmit(cmd_MCU, 0)

    def setCurrent(self):
        global fConnect
        if fConnect == True:
            cmd_MCU = 'mainCurrent ' + self.currentSetEntry.get() + '\r\n'
            print(cmd_MCU)
            mySerial.transmit(cmd_MCU, 0)

    def setPsh0(self):
        global fConnect
        if fConnect == True:
            cmd_MCU = 'psh 0 I ' + self.psh0Entry.get() + '\r\n'
            print(cmd_MCU)
            mySerial.transmit(cmd_MCU, 0)

    def setPsh3(self):
        global fConnect
        if fConnect == True:
            cmd_MCU = 'psh 3 I ' + self.psh3Entry.get() + '\r\n'
            print(cmd_MCU)
            mySerial.transmit(cmd_MCU, 0)

if __name__ == "__main__":
    root = tk.Tk()
    tab_control = ttk.Notebook(root)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Tab 1')
    tab_control.add(tab2, text='Tab 2')
    widget = Gui1Widget(tab1)
    tab_control.pack(expand=1, fill='both')
    root.after(500, widget.readMySerial())
    root.mainloop()

