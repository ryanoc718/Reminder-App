try:
    import tkinter as tk
    from tkinter import *
except ImportError:
    import Tkinter as tk
    import ttk

import datetime
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
        for i in range(1, 30):
            Application.grid_columnconfigure(self, index=i, minsize=10, weight=1)
            
        # X button
        self.quit = tk.Button(self, text = "X", fg = 'red', padx=1, pady=1, command=self.master.destroy)
        self.quit.grid(row=0, column=29,sticky = E, columnspan=5, rowspan=5)
        
        # create reminder button
        self.create_new = Button(self, text="Create New Reminder: +", fg = bg_color, bg="cyan", padx=5, pady=5, 
                                 command= lambda: Reminder_Pops2.createNewWindow())
        self.create_new['font'] = font.Font(size=15)
        self.create_new.grid(row=1, column=3, rowspan=5, columnspan=10, sticky=W)
        
        # spacing the rows correctly
        for i in range(4, 8):
             Application.grid_rowconfigure(self, index=i, minsize=10, weight=1)
        
        # loghistory label
        self.loghistory_label = tk.Label(self, text="Reminders: ", fg='grey99', bg=bg_color)
        self.loghistory_label['font'] = font.Font(size=15)
        self.loghistory_label.grid(row=8, column=5, columnspan=4, sticky=W)
        
        self.refresh()
      
    def refresh(self):
        self.logButtons = []
        ReminderHistory = open("ReminderHistory.txt", "r")
        linecnt = 0
        for line in ReminderHistory:
            comma = line.index(',')
            if line[0] != 'X': # text file has X's to mark deleted reminder
                self.logButtons.append(Button(self, text=line[1:comma]+' '+line[comma+3:comma+13], height=1, padx=2, pady = 2,
                                          command= lambda l=line: Reminder_Pops2.createNewWindow2(l))) 
                if line[comma+1] == 'A': # because of the textfile layout, A=Active
                    self.logButtons[linecnt]['bg'] = "SeaGreen1"
                else: # Deactivated
                    self.logButtons[linecnt]['bg'] = "grey20"
                    self.logButtons[linecnt]['fg'] = "grey75"
                self.logButtons[linecnt].grid(row=9+linecnt, column=6, sticky=W)
                linecnt += 1
        ReminderHistory.close()
 
        self.after(1000, self.refresh) # refreshes every 1 second
        

        

root = tk.Tk()
#root.geometry("600x300")
#root.resizable(False, False) # make true, true if I want to adjust window size manually
app = Application(master=root)
app.mainloop()

#https://www.youtube.com/watch?v=ELkaEpN29PU -- 54:00 create this as a .exe file


# make window for each reminder when clicked to activate/deativate
# send text to phone
# open pop up at specified time on pc
# need to automatically change reminder color once date passes

