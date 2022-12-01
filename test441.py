# convert log to map


import math
import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

dt = 0.5
mainI = []
mainV = []
VV = [] #????

busV = []
leadV = []
magnetV = []

time = []
nameLog=''

Ird = [625, 650, 675, 700, 720, 730, 744]
Urd = [1.4, 0.8, 0.5, 0.4, 0.3, 0.2, 0.1]



# Root window
root = tk.Tk()
root.title('Convert log files')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)



# Log
text = tk.Text(root, height=12)
text.grid(column=0, row=0, sticky='nsew', columnspan=4)




def open_log_file():
    global mainI, mainV, time, dt, VV, t0, nameLog, busV, leadV, magnetV
    timeR = []
    # file type
    filetypes = (
        ('log files', '*.txt'),
        ('All files', '*.*')
    )
    # show the open file dialog
    f = fd.askopenfile(filetypes=filetypes, initialdir='./log/')
    nameLog = f.name
    text.insert('end', '--> Read : ')
    text.insert('end', f.name)
    text.insert('end', '\n')
    i = 0
    while True:
        # считываем строку
        line = f.readline()
        # прерываем цикл, если строка пустая
        if not line:
            break
        # выводим строку
        print("-> ", end='')
        print(line.strip())
        ls = line.split('|')
        if len(ls) == 3:
            print('I=['+str(ls[1])+']-len=['+str(len(ls[1]))+']')
            I = "".join(c for c in ls[1] if not c.isalpha())
            #I = ls[1][:-1]
            vls = ls[2].split()
            print('vls = ', end='')
            print(vls)
            Vbus= vls[0][:-1]
            V = vls[1][:-1]
            Vl = vls[2][:-1]
            Vm = vls[3][:-1]
            print('Vbus='+str(Vbus)+'\tV='+str(V)+'\tVl='+str(Vl)+'\tVm='+str(Vm))
            ls0 = ls[0].split()
            t =  ls0[0]
            print (ls[0])
            print(ls0[0])
            #t = dt*i
            Vv = float(V)-float(I)*2.3/740

            mainI.append(float(I))
            mainV.append(float(V))
            busV.append(float(Vbus))
            leadV.append(float(Vl))
            magnetV.append(float(Vm))
            VV.append(float(Vv))
            timeR.append(float(t))
            i=i+1

            #text.insert('end', 'tr= '+str(t)+' I = '+str(I)+' V = '+str(V)+'\n')
            #text.yview(tk.END)

    t0 = min(timeR)
    print(t0)
    for tt in timeR:
        ttt = round((tt-t0)/60, 3)
        time.append(ttt)

    # закрываем файл
    f.close



    show_MAP_button['state'] = tk.NORMAL
    text.insert('end', '--> Can write\n')


# open XML file button
open_Log = ttk.Button(
    root,
    text='Open Log File',
    command=open_log_file
)
open_Log.grid(column=0, row=2, sticky='w', padx=10, pady=10)


######
def save_log_file():
    global mainI, mainV, time, dt, VV, busV, magnetV, leadV, t0, nameLog

    # file type
    filetypes = (
        ('log files', '*.map'),
        ('All files', '*.*')
    )
    # show the open file dialog
    name = nameLog.split('/')
    nm=str(name[-1])
    name = nm.replace('.txt', '.map')
    print(nm.replace('.txt', '.map'))

    def_name = str(name)+'.map'
    f = fd.asksaveasfile(mode='w', defaultextension=".map", initialfile=def_name, initialdir='./map/')
    nameMAP = f.name
    text.insert('end', '<<- Start write to : ')
    text.insert('end', f.name)
    text.insert('end', '\n')

    fmap = open(nameMAP, 'w')
    #i = 0
    print('time, s |I main, A | V bus, V | V mps, V | V lead,V | V magnet, V')
    fmap.write('time, s |I main, A | V bus, V | V mps, V | V lead,V | V magnet, V \n')
    for i in range(len(time)):
        fmap.write(str(time[i])+' | '+str(mainI[i])+' | '+str(busV[i]) +' | '+str(mainV[i]) +' | '+str(leadV[i]) +' | '+str(magnetV[i])+' \n ')
        print(str(time[i])+' | '+str(mainI[i])+' | '+str(busV[i]) +' | '+str(mainV[i]) +' | '+str(leadV[i]) +' | '+str(magnetV[i]))
        #text.insert('end', str(time[i])+' | '+str(mainI[i])+' | '+str(mainV[i])+' \n ')
        text.yview(tk.END)

    # закрываем файл
    text.insert('end', '--> write map \n ')
    text.yview(tk.END)
    f.close



    save_Log['state'] = tk.NORMAL



# sawe file button
save_Log = ttk.Button(
    root,
    text='Save Log File',
    command=save_log_file
)
save_Log.grid(column=1, row=2, sticky='w', padx=10, pady=10)
#########



#
def open_map_file():
    global mainI, mainV, time, dt, VV, t0, nameLog

    # file type
    filetypes = (
        ('log files', '*.map'),
        ('All files', '*.*')
    )
    # show the open file dialog
    f = fd.askopenfile(filetypes=filetypes, initialdir='./map/')
    nameLog = f.name
    text.insert('end', '--> Read MAP : ')
    text.insert('end', f.name)
    text.insert('end', '\n')
    i = 0
    time = []
    mainV = []
    mainI = []
    while True:
        # считываем строку
        line = f.readline()
        # прерываем цикл, если строка пустая
        if not line:
            break
        # выводим строку
        print(line.strip('|'))
        ls = line.split('|')
        if len(ls) == 3:
            #I = "".join(c for c in ls[1] if not c.isalpha())
            I = ls[1]
            V = ls[2]
            t = ls[0]
            mainI.append(float(I))
            mainV.append(float(V))
            time.append(float(t))
            i=i+1
            print('t= '+str(t)+' I = '+str(I)+' V = '+str(V))
            #text.insert('end', 'tr= '+str(t)+' I = '+str(I)+' V = '+str(V)+'\n')
            #text.yview(tk.END)



    # закрываем файл
    f.close



    show_MAP_button['state'] = tk.NORMAL
    text.insert('end', '--> Can write\n')


# open XML file button
open_Map = ttk.Button(
    root,
    text='Open MAP File',
    command=open_map_file
)
open_Map.grid(column=2, row=2, sticky='w', padx=10, pady=10)
#

def write_map():
    global mainI, mainV, time, dt, Ird, Urd, VV
    text.insert('end', '<<- Start to MAP \n')

    #fig, ax_I = plt.subplots()
    ax_I = plt.subplot(2, 1, 1)
    ax_U = ax_I.twinx()
    ax_I.plot(time, mainI, color='r')
    ax_U.plot(time, mainV, color='b')
    ax_I.set_ylabel('I, A [red]')
    ax_U.set_ylabel('U, V [blue]')
    #ax_I.set_xlabel('t, min')
    ax_I.grid()

    ax_P = plt.subplot(2, 1, 2)
    P = []
    for i in range(len(mainI)):
        P.append(mainI[i]*mainV[i]/1e3)
    ax_P.plot(time, P, color='g')
    ax_P.set_xlabel('t, min')
    ax_P.set_ylabel('P, kW')
    ax_P.grid()

    #ax_CMP = plt.subplot(3, 1, 3)
    #ax_CMP.plot(mainI, mainV, '-',  Ird, Urd, '--')
    #ax_CMP.grid()


    plt.show()

    text.insert('end', '<<- Finish to MAP \n')


# open file button
show_MAP_button = ttk.Button(
    root,
    text='Show to map',
    command=write_map,
    state=tk.DISABLED
)


show_MAP_button.grid(column=3, row=2, sticky='w', padx=10, pady=10)


root.mainloop()

