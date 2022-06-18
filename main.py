from tkinter import *
from tkinter import ttk
import tkinter.filedialog as fdlg
import os
#import Tkinter as tk # Python 2.x Version

from panels import MsgPanel, BottomPanel
class App(ttk.Frame):

    nameGBA = "null"
    nameSAVE = "null"

    def __init__(self, isapp=True, name='fileseldlgdemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=YES)
        self.master.title('Save injector to Bootleg GBA games')
        self.isapp = isapp
        self._create_widgets()
    
    def _create_widgets(self):
        if self.isapp:
            MsgPanel(self, 
                     ["Select the files to injection",
                      "WARNING: Please remember to backup the files before execute the process"])
            
            BottomPanel(self)
        
        self._create_demo_panel()
        
    def _create_demo_panel(self):
        demoPanel = ttk.Frame(self)
        demoPanel.pack(side=TOP, fill=BOTH, expand=Y)
        
        for item in ('rom', 'sav'):
            frame = ttk.Frame(demoPanel)
            lbl = ttk.Label(frame, width=20,
                            text='Select the {} '.format(item))
            ent = ttk.Entry(frame, width=25)
            btn = ttk.Button(frame, text='Browse...', 
                             command=lambda i=item, e=ent: self._file_dialog(i, e))
            lbl.pack(side=LEFT)
            ent.pack(side=LEFT, expand=Y, fill=X)
            btn.pack(side=LEFT, padx=5)
            frame.pack(fill=X, padx='1c', pady=3)
                
    def _file_dialog(self, type, ent):
        fn = None

        if type == 'rom':
            opts = {'initialfile': ent.get(),
                'filetypes': (('GBA game', '.gba'),)}
            opts['title'] = 'Select the rom...'
            fn = fdlg.askopenfilename(**opts)
            if(fn):
                self.nameGBA = fn
               #print( self.nameGBA)
        else:
            opts = {'initialfile': ent.get(),
                'filetypes': (('save file', '.sav'),)}
            opts['title'] = 'Select the save file...'
            fn = fdlg.askopenfilename(**opts)
            if(fn):
                self.nameSAVE = fn
               # print( self.namgeSAVE)

        if fn:
            ent.delete(0, END)
            ent.insert(END, fn)

    
    def openfile(self):
        return filedialog.askopenfilename()

if __name__ == '__main__':
    App().mainloop()