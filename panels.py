from tkinter import *
from tkinter import ttk,messagebox
from tkinter.font import ROMAN
from tkinter.simpledialog import Dialog
from injection import InjectionProcess
import os

class MsgPanel(ttk.Frame):
    def __init__(self, master, msgtxt):
        ttk.Frame.__init__(self, master)
        self.pack(side=TOP, fill=X)
        
        msg = Label(self, wraplength='4i', justify=LEFT)
        msg['text'] = msgtxt[0]+'\n'+msgtxt[1]
        msg.pack(fill=X, padx=5, pady=5)
        
class BottomPanel(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master) 
        self.pack(side=BOTTOM, fill=X)          # resize with parent
        
        # separator widget
        sep = ttk.Separator(orient=HORIZONTAL)

        # Dismiss button
        injectBtn = ttk.Button(text='Inject!', default=ACTIVE, command=lambda: self.process(master))
        injectBtn['compound'] = LEFT           # display image to left of label text
             
        # position and register widgets as children of this frame
        sep.grid(in_=self, row=0, columnspan=4, sticky=EW, pady=5)
        injectBtn.grid(in_=self, row=1, column=1, sticky=E)
        
        # set resize constraints
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def process(self,master):
        rom = master.nameGBA
        savefile = str(master.nameSAVE)
        baseName = os.path.basename(savefile)
        print('process.rom -> '+rom)
        print('process.savefile -> '+savefile)
        print('process.basename -> ' + baseName)
        if(not rom ):
            messagebox.showerror("Erro!", "Insert a valid rom (.gba)")
        elif(not savefile):
            messagebox.showerror("Erro!", "Insert a valid save file (.sav)")
        elif(InjectionProcess.hexAddress(baseName) is None):
            messagebox.showerror("Erro!", "The file name is not valid.")
        else:
            hex = InjectionProcess.hexAddress(os.path.basename(savefile))
            print('process.hex -> '+hex)
            InjectionProcess.writeBytes(rom,savefile,hex)
            messagebox.showinfo("Sucess!", "File export: output-"+os.path.basename(rom))
        
         
    