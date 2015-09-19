#!/usr/bin/env python

import os
from time import sleep
from Tkinter import * 
from functools import partial as pto
from tkMessageBox import showinfo, showwarning, showerror
import string
import tkMessageBox

class DirList(object):
    def __init__(self, initdir=None):
        self.top = Tk()
        self.label = Label(self.top, text='Directory Lister')
        self.label.pack()

        self.cwd = StringVar(self.top)
        self.dir1 = Label(self.top, fg='blue', font=('Helvetica', 12, 'bold'))
        self.dir1.pack()

        self.dirfm = Frame(self.top)
        self.dirsb = Scrollbar(self.dirfm)
        self.dirsb.pack(side=RIGHT, fill=Y)

        self.dirs = Listbox(self.dirfm, height=15, width=50, yscrollcommand=self.dirsb.set)
        self.dirs.bind('<Double-1>', self.setDirAndGo)
        self.dirsb.config(command=self.dirs.yview)
        self.dirs.pack(side=LEFT, fill=BOTH)
        self.dirfm.pack()

        self.dirn = Entry(self.top, width=50, textvariable=self.cwd)
        self.dirn.bind('<Return>', self.doLS)
        self.dirn.pack()

        self.bfm = Frame(self.top)
        self.clr = Button(self.bfm, text='Clear', command=self.clrDir,
                    activeforeground='white',
                    activebackground='blue')

        self.ls = Button(self.bfm, text='ls', command=self.doLS,
                    activeforeground='white',
                    activebackground='green')


        self.quit = Button(self.bfm, text='Quit', command=self.top.quit,
                    activeforeground='white',
                    activebackground='red')

        self.clr.pack(side=LEFT)
        self.ls.pack(side=LEFT)
        self.quit.pack(side=LEFT)
        
        self.bfm.pack()

        if initdir:
            self.cwd.set(os.curdir)
            self.doLS()

    def clrDir(self, ev=None):
        self.cwd.set('')

    def setDirAndGo(self, ev=None):
        self.last = self.cwd.get()
        self.dirs.config(selectbackground='red')
        check = self.dirs.get(self.dirs.curselection())
        if not check:
            check = os.curdir
        self.cwd.set(check)
        self.doLS()

    def doLS(self, ev = None):
        error = ''
        tdir = self.cwd.get()

        if not tdir:
            tdir = os.curdir

        if not os.path.exists(tdir):
            error = tdir + ":no such file"
        elif not os.path.isdir(tdir):
            error = tdir + ": not a dir"

        if error:
            self.cwd.set(error)
            self.top.update()
            sleep(2)
            if not (hasattr(self, 'last') and self.last):
                self.last = os.curdir

            self.cwd.set(self.last)
            self.dirs.config(selectbackground='LightSkyBlue')
            self.top.update()
            return 
        self.cwd.set('Fetching dir contents...')
        self.top.update()
        dirlist = os.listdir(tdir)
        dirlist.sort()
        os.chdir(tdir)
        self.dir1.config(text=os.getcwd())
        self.dirs.delete(0, END)
        self.dirs.insert(END, os.curdir)
        self.dirs.insert(END, os.pardir)
        for eachFile in dirlist:
            self.dirs.insert(END, eachFile)
        self.cwd.set(os.curdir)
        self.dirs.config(selectbackground='LightSkyBlue')

def lsdir():
    d = DirList(os.curdir)
    mainloop()

def roadSigns():
    WARN = 'warn'
    CRIT = 'crit'
    REGU = 'regu'

    SIGNS = {
'do not enter'      : CRIT,
'railroad crossing' : WARN,
'55\nspeed limit'   : REGU,
'wrong way'         : CRIT,
'merging traffic'   : WARN,
'one way'           : REGU,
}
    critCB = lambda: showerror('Error', 'Error Button Pressed!')
    warnCB = lambda: showwarning('Warning', 'Warning Button Pressed!')
    infoCB = lambda: showinfo('Info', 'Info Button Pressed!')

    top = Tk()
    top.title('Road Signs')
    Button(top, text='QUIT', command=top.quit, bg='red', fg='white').pack()

    MyButton = pto(Button, top)
    CritButton = pto(MyButton, command=critCB, bg='white', fg='red')
    WarnButton = pto(MyButton, command=warnCB, bg='goldenrod1')
    ReguButton = pto(MyButton, command=infoCB, bg='white')

    for eachSign in SIGNS:
        signType = SIGNS[eachSign]
        cmd = '%sButton(text=%r%s).pack(fill=X, expand=True)' % (
        signType.title(), eachSign, '.upper()' if signType == CRIT else '.title()')
        eval(cmd)
    top.mainloop()

class Dialog(Toplevel):
    def __init__(self, parent, title=None):
        Toplevel.__init__(self, parent)
        self.transient(parent)
        if title:
            self.title(title)
        self.parent = parent
        self.result = None

        body = Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)

        self.buttonbox()
        self.grab_set()
        if not self.initial_focus:
            self.initial_focus = self
        #self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.geometry("+%d+%d" % (self.parent.winfo_rootx() + 50,
                                  self.parent.winfo_rooty() + 50))
        self.initial_focus.focus_set()
        self.wait_window(self)

    def body(self, master):
        # create dialog body. return widget that should have
        # initial focus. this method should be overridden
        pass
    def buttonbox(self):
        # add standard button box. override if you don't want the
        # standard buttons
        box = Frame(self)
        w = Button(box, text="OK", width=10, default=ACTIVE, command=self.ok)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)
        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
        box.pack()

    def ok(self, event=None):
        if not self.validate():
            self.initial_focus.focus_set()  # put focus back
            return
        self.withdraw()
        self.update_idletasks()
        self.apply()
        self.cancel()
    def cancel(self, event=None):
        self.parent.focus_set()
        self.destroy()
    def validate(self):
        # command hooks, override
        return 1
    def apply(self):
        pass

class MyDialog(Dialog):
    def body(self, master):
        Label(master, text="First:").grid(row=0, sticky=W)
        Label(master, text="Second:").grid(row=1, sticky=W)
        self.e1 = Entry(master)
        self.e2 = Entry(master)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.cb = Checkbutton(master, text="Hardcopy")
        self.cb.grid(row=2, columnspan=2, sticky=W)
        return self.e1  # initial focus
    def apply(self):
        print self.result
    def validate(self):
        try:
            first = string.atoi(self.e1.get())
            second = string.atoi(self.e2.get())
            self.result=first,second
            return 1
        except ValueError, e:
            tkMessageBox.showwarning("Bad input","Illegal values, please try again")
            return 0

def test_dialog():
    root = Tk()
    d = MyDialog(root, title='dialog')
    root.mainloop()

class MyMenu():
    def __init__(self,master):
        self.master=master
        self.master.protocol("WM_DELETE_WINDOW", self.QuitFunc)

        self.rootMenu=Menu(self.master)
        self.master.config(menu=self.rootMenu)

        self.fileMenu=Menu(self.rootMenu)
        self.editMenu=Menu(self.rootMenu)
        self.helpMenu=Menu(self.rootMenu)
        self.rootMenu.add_cascade(label='File',menu=self.fileMenu)
        self.rootMenu.add_cascade(label='Edit',menu=self.editMenu)
        self.rootMenu.add_cascade(label='Help',menu=self.helpMenu)

        newMenu=Menu(self.fileMenu)
        self.fileMenu.add_cascade(label="New",menu=newMenu)

        newMenu.add_command(label="pydev project",command=self.pyprojectFunc)
        newMenu.add_command(label="project...",command=self.projectFunc)
        newMenu.add_command(label="File",command=self.fileFunc)
        self.fileMenu.add_command(label="Open file...",command=self.fileFunc)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit",command=self.QuitFunc)

        # create toolbar
        toolbar=Frame(self.master)
        Button(toolbar,text='New',width=1,command=self.toolboxFunc).pack(side=LEFT, padx=2, pady=2)
        Button(toolbar,text='Open',width=1,command=self.toolboxFunc).pack(side=LEFT, padx=2, pady=2)
        Button(toolbar,text='Exit',width=1,command=self.QuitFunc).pack(side=LEFT, padx=2, pady=2)
        toolbar.pack(side=TOP, fill=X)

    def fileFunc(self):
        print 'fileFunc'
    def QuitFunc(self):
        print 'QUIT'
        self.master.destroy()
    def pyprojectFunc(self):
        print "pyprojectFunc"
    def projectFunc(self):
        print 'projectFunc'
    def toolboxFunc(self):
        print 'toolboxFunc'
def test_menu():
    root=Tk()
    root.geometry('500x500')
    m=MyMenu(root)
    root.mainloop()

if __name__ == '__main__':
    #lsdir()

    #roadSigns()

    test_dialog()

    #test_menu()
