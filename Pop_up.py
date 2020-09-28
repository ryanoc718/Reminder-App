try:
    import tkinter as tk
    from tkinter import *
except ImportError:
    import Tkinter as tk
    import ttk

from datetime import date
import Reminder_Pops2

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()

        bg_color = 'grey1' # sets the background color
        Application.configure(self, bg=bg_color)
        Application.grid_rowconfigure(self, index=0, minsize=10, weight=1)
        Application.grid_columnconfigure(self, index=0, minsize=10, weight=1)
        # setting the row and column sizing
        for i in range(1, 20):
            Application.grid_columnconfigure(self, index=i, minsize=10, weight=1)
            
        # X button
        self.quit = tk.Button(self, text = "X", fg = 'red', padx=1, pady=1, command=self.master.destroy)
        self.quit.grid(row=0, column=19,sticky = E, columnspan=5, rowspan=5)
        
        today = date.today()
        
        Application.grid_rowconfigure(self, index=9, minsize=10, weight=1)
        Application.grid_rowconfigure(self, index=14, minsize=20, weight=1)
        
        ReminderHistory = open("ReminderHistory.txt", "r")
        linecnt = 0
        colcnt = 0
        for line in ReminderHistory:
            comma = line.index(',')
            if line[comma+3:comma+13] == str(today):

                # labels for all of the info:
                alertTitle = tk.Label(self, text=line[1:comma], fg='red', bg='white')
                alertTitle['font'] = font.Font(size=20)
                alertTitle.grid(row=8, column=5, columnspan=4, sticky=W)
                
                alertDesc = tk.Label(self, text=line[comma+20:], fg='red', bg='white')
                alertDesc['font'] = font.Font(size=12)
                alertDesc.grid(row=10, column=5, columnspan=4, rowspan=3, sticky=W)
                
                alertTime = tk.Label(self, text=line[comma+14:comma+19], fg='red', bg='white')
                alertTime['font'] = font.Font(size=20)
                alertTime.grid(row=8, column=10, columnspan=2, sticky=W)
                
                alertDate = tk.Label(self, text=str(today), fg='red', bg='white')
                alertDate['font'] = font.Font(size=12)
                alertDate.grid(row=10, column=10, columnspan=2, sticky=W)
                
        ReminderHistory.close() 

        

root = tk.Tk()
#root.geometry("600x300")
#root.resizable(False, False) # make true, true if I want to adjust window size manually
app = Application(master=root)
app.mainloop()