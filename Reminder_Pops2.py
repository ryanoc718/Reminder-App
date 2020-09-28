try:
    import tkinter as tk
    from tkinter import *
except ImportError:
    import Tkinter as tk
    import ttk

import datetime
import calendarDatepicker
#from Reminder_Pops import update


def createNewWindow(): # for creating a reminder
    
    newWindow = tk.Toplevel()
    
    bg_color2 = 'grey1' # sets the background color
    newWindow.configure(bg=bg_color2)
    
    Label(newWindow, text = "Title:", font=font.Font(size=12), bg=bg_color2, fg='grey99').grid(row=0, column=0)
    titleText = Text(newWindow, height=1, width=25, bg= "grey30", fg='medium turquoise')
    titleText.grid(row=1,column=0, sticky=N)
    
    newWindow.grid_columnconfigure(index=1, minsize=10, weight=1)
    newWindow.grid_columnconfigure(index=2, minsize=10, weight=1)
    
    Label(newWindow, text = "Description:", font=font.Font(size=12), bg=bg_color2, fg='grey99').grid(row=0,column=1, columnspan=3)
    descriptionText = Text(newWindow, height=4, width=40, bg= "grey30", fg='medium turquoise')
    descriptionText.grid(row=1,column=1, columnspan=3)
    
    Label(newWindow, text = "Date:", font=font.Font(size=12), bg=bg_color2, fg='grey99').grid(row=2,column=0)
    
    for j in range(3, 18):
        newWindow.grid_rowconfigure(index=j, minsize=10)
    
    # make radio buttons for reoccuring or not *********************
    var = IntVar(0)
    def makeDaily():
        weekly.deselect()
        monthly.deselect()
    def makeWeekly():
        daily.deselect()
        monthly.deselect()
    def makeMonthly():
        daily.deselect()
        weekly.deseelct()
    def recurr():
        daily = Radiobutton(newWindow, text="Daily", variable=1, value=0, command=makeDaily()).grid(row=10, column=3, sticky=E)
        weekly = Radiobutton(newWindow, text="Weekly", variable=2, value=0, command=makeWeekly()).grid(row=11, column=3, sticky=E)
        monthly = Radiobutton(newWindow, text="Monthly", variable=3, value=0, command=makeMonthly()).grid(row=12, column=3, sticky=E)
    reoccuring = Radiobutton(newWindow, text="Reoccuring", variable=var, value=1, command=recurr).grid(row=9, column=3, sticky=E)
    
        
    sendButton = Button(newWindow, text='Send', padx=2, pady=2, width=22, bg='SeaGreen1', 
                        command= lambda: send(titleText, descriptionText, hour, mins, cal))
    
    sendButton.grid(row=17, column=3, sticky=E)
    
    
    # the datepicker widget       
    cal = calendarDatepicker.Datepicker(newWindow)
    cal.grid(row=3,column=0)
    
    # time select
    Label(newWindow, text="Time:", font=font.Font(size=12), bg=bg_color2, fg='grey99').grid(row=2,column=1,sticky=E)
    
    hourstr = tk.StringVar(newWindow,'12')
    hour = tk.Spinbox(newWindow, from_=0, to=23, wrap=True, textvariable=hourstr, width=2, state="readonly", bg= "grey30", fg='medium turquoise')
    hour['font'] = font.Font(size=20)
    hour.grid(row=3, column=1, sticky=E)
    minstr = tk.StringVar(newWindow,'30')
    mins = tk.Spinbox(newWindow, from_=0, to=59, wrap=True, textvariable=minstr, width=2, state="readonly", bg= "grey30", fg='medium turquoise')
    mins['font'] = font.Font(size=20)
    mins.grid(row=3, column=2, sticky=W)
    
    
    newWindow.mainloop()
        
def send(titleText, descriptionText, hour, mins, cal):
    ReminderHistory = open("ReminderHistory.txt", "a")
    ReminderHistory.write("\n")
    ReminderHistory.write('O'+titleText.get('1.0', 'end-1c')+',A,'+cal.get()+','+hour.get()+':'+mins.get()+','+descriptionText.get('1.0', 'end-1c'))
    ReminderHistory.close()
    # still need to see how this can be added to computer reminders
        
def createNewWindow2(string): 
    
    newWindow = tk.Toplevel()
    
    comma = string.index(',') # to parse the text file data of the reminder
    tit = string[1:comma] # title
    active = string[comma+1] # activation status
    dat = string[comma+3:comma+13] # date
    ho = string[comma+14:comma+16] # hour
    mn = string[comma+17:comma+19] # min
    des = string[comma+20:] # description
    
    bg_color2 = 'grey1' # sets the background color
    newWindow.configure(bg=bg_color2)
    
    Label(newWindow, text = "Title:", font=font.Font(size=12), bg=bg_color2, fg='grey99').grid(row=0, column=0)
    titleText = Text(newWindow, height=1, width=25, bg= "grey30", fg='medium turquoise')
    titleText.grid(row=1,column=0, sticky=N)
    titleText.insert('1.0', tit)
    
    newWindow.grid_columnconfigure(index=1, minsize=10, weight=1)
    newWindow.grid_columnconfigure(index=2, minsize=10, weight=1)
    
    Label(newWindow, text = "Description:", font=font.Font(size=12), bg=bg_color2, fg='grey99').grid(row=0,column=1, columnspan=3)
    descriptionText = Text(newWindow, height=4, width=40, bg= "grey30", fg='medium turquoise')
    descriptionText.grid(row=1,column=1, columnspan=3)
    descriptionText.insert('1.0', des)
    
    Label(newWindow, text = "Date:", font=font.Font(size=12), bg=bg_color2, fg='grey99').grid(row=2,column=0)
    
    for j in range(3, 18):
        newWindow.grid_rowconfigure(index=j, minsize=10)
    
    # make radio buttons for reoccuring or not *********************
    # var = IntVar(0)
    # def makeDaily():
    #     weekly.deselect()
    #     monthly.deselect()
    # def makeWeekly():
    #     daily.deselect()
    #     monthly.deselect()
    # def makeMonthly():
    #     daily.deselect()
    #     weekly.deseelct()
    # def recurr():
    #     daily = Radiobutton(newWindow, text="Daily", variable=1, value=1, command=makeDaily).grid(row=10, column=3, sticky=E)
    #     weekly = Radiobutton(newWindow, text="Weekly", variable=2, value=1, command=makeWeekly).grid(row=11, column=3, sticky=E)
    #     monthly = Radiobutton(newWindow, text="Monthly", variable=3, value=1, command=makeMonthly).grid(row=12, column=3, sticky=E)
    # reoccuring = Radiobutton(newWindow, text="Reoccuring", variable=var, value=1, command=recurr).grid(row=9, column=3, sticky=E)
    
        
    updateButton = Button(newWindow, text='update', padx=2, pady=2, width=22, bg='SeaGreen1', 
                        command= lambda: update1(tit, titleText, descriptionText, hour, mins, cal))
    # updateButton = Button(newWindow, text='update', padx=2, pady=2, width=22, bg='SeaGreen1', 
    #                      command= lambda: update2())
    
    updateButton.grid(row=17, column=3, sticky=E)
    
    # the datepicker widget       
    cal = calendarDatepicker.Datepicker(newWindow)
    cal.insert(0,dat)
    cal.grid(row=3,column=0)
    
    # time select
    Label(newWindow, text="Time:", font=font.Font(size=12), bg=bg_color2, fg='grey99').grid(row=2,column=1,sticky=E)
    
    hourstr = tk.StringVar(value=ho)
    hour = tk.Spinbox(newWindow, from_=0, to=23, wrap=True, textvariable=hourstr, width=2, state="readonly", bg= "grey30", fg='medium turquoise')
    hour['font'] = font.Font(size=20)
    hour.grid(row=3, column=1, sticky=E)
    minstr = tk.StringVar(value=mn)
    mins = tk.Spinbox(newWindow, from_=0, to=59, wrap=True, textvariable=minstr, width=2, state="readonly", bg= "grey30", fg='medium turquoise')
    mins['font'] = font.Font(size=20)
    mins.grid(row=3, column=2, sticky=W)
    
    # activate/deactivate
    # if active == 'A':
    #     v = IntVar(1)
    # else:             # this doesn't work
    #     v= IntVar(0)
    activate = Radiobutton(newWindow, text="Activate/Deactivate", variable=0, value=1,
                           command= lambda: activate_deativate(active, tit)).grid(row=7, column=3, sticky=E)
    
    deleteButton = Button(newWindow, text='Delete', padx=2, pady=2, width=22, bg='SeaGreen1', 
                        command= lambda: delete(tit))
    deleteButton.grid(row=17, column=0, sticky=E)
    
    newWindow.mainloop()

def delete(t):
    ReminderHistory = open("ReminderHistory.txt", "r") # update can be seen next time app is loaded
    lines = ReminderHistory.readlines()
    cnt = 0
    for line in lines:
        comma = line.index(',')
        if line[1:comma] == t:
            lines[cnt] = 'X'+line[1:]
        cnt += 1
    ReminderHistory = open("ReminderHistory.txt", "w")
    ReminderHistory.writelines(lines)
    ReminderHistory.close()
    

def activate_deativate(act, t): # when user toggles activity of reminder it changes the activity in the text file
    ReminderHistory = open("ReminderHistory.txt", "r") # update can be seen next time app is loaded
    lines = ReminderHistory.readlines()
    cnt = 0
    for line in lines:
        comma = line.index(',')
        if line[1:comma] == t:
            if act == 'A':
                lines[cnt] = 'O'+line[1:comma+1]+'X'+line[comma+2:]
            else:
                lines[cnt] = 'O'+line[1:comma+1]+'A'+line[comma+2:]
        cnt += 1
    ReminderHistory = open("ReminderHistory.txt", "w")
    ReminderHistory.writelines(lines)
    ReminderHistory.close()
    

def update1(tit, tt, dt, ho, mn, cal):
    ReminderHistory = open("ReminderHistory.txt", "r") 
    lines = ReminderHistory.readlines()
    cnt = 0
    for line in lines:
        comma = line.index(',')
        if line[1:comma] == tit:
            lines[cnt] = 'O'+tt.get('1.0', 'end-1c')+',A,'+cal.get()+','+ho.get()+':'+mn.get()+','+dt.get('1.0', 'end-1c')
        cnt += 1
    ReminderHistory = open("ReminderHistory.txt", "w")
    ReminderHistory.writelines(lines)
    ReminderHistory.close()

        

