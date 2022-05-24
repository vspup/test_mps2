# convert log to map


import math
import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

dt = 0.5
mainI = []
mainV = []
VV = []
time = []

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
    global mainI, mainV, time, dt, VV
    # file type
    filetypes = (
        ('log files', '*.txt'),
        ('All files', '*.*')
    )
    # show the open file dialog
    f = fd.askopenfile(filetypes=filetypes, initialdir='./')
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
        print(line.strip())
        ls = line.split('|')
        if len(ls) == 3:
            print('['+str(ls[1])+']-['+str(len(ls[1])))
            I = "".join(c for c in ls[1] if not c.isalpha())
            #I = ls[1][:-1]
            vls = ls[2].split()
            V = vls[1][:-1]
            t = dt*i
            Vv = float(V)-float(I)*2.3/740

            mainI.append(float(I))
            mainV.append(float(V))
            VV.append(float(Vv))
            time.append(float(t))
            i=i+1

            text.insert('end', 't = '+str(t)+' I = '+str(I)+' V = '+str(V)+'\n')


    # закрываем файл
    f.close



    write_MAP_button['state'] = tk.NORMAL
    text.insert('end', '--> Can write\n')


# open XML file button
open_Log = ttk.Button(
    root,
    text='Open Log File',
    command=open_log_file
)
open_Log.grid(column=0, row=2, sticky='w', padx=10, pady=10)


def write_map():
    global mainI, mainV, time, dt, Ird, Urd, VV
    text.insert('end', '<<- Start to MAP \n')

    #fig, ax_I = plt.subplots()
    ax_I = plt.subplot(3, 1, 1)
    ax_U = ax_I.twinx()
    ax_I.plot(time, mainI, color='r')
    ax_U.plot(time, mainV, color='b')
    ax_I.set_ylabel('I, A')
    ax_U.set_ylabel('U, V')
    ax_I.grid()

    ax_P = plt.subplot(3, 1, 2)
    P = []
    for i in range(len(mainI)):
        P.append(mainI[i]*mainV[i])
    ax_P.plot(time, P, color='g')
    ax_P.grid()

    ax_CMP = plt.subplot(3, 1, 3)
    ax_CMP.plot(mainI, mainV, '-',  Ird, Urd, '--')
    ax_CMP.grid()


    plt.show()

    text.insert('end', '<<- Finish to MAP \n')


# open file button
write_MAP_button = ttk.Button(
    root,
    text='Write to map',
    command=write_map,
    state=tk.DISABLED
)


write_MAP_button.grid(column=1, row=2, sticky='w', padx=10, pady=10)


root.mainloop()

