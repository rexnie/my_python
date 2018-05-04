# 读取扫描枪上扫到的二维码，写入文本文件
from Tkinter import *
import tkFont
import tkMessageBox
import string
import os

FILE='sn_device.cfg'

class Dialog(object):
    def __init__(self):
        self.root=Tk()
        self.root.title("Read SN")
        self.ft0=tkFont.Font(family='Courier', size=20, weight=tkFont.BOLD)
        self.ft1=tkFont.Font(family='Courier', size=15, weight=tkFont.BOLD)
        Label(self.root, text="Input:", font=self.ft1).pack(side=LEFT)
        self.text=Text(self.root, width=30, height=5, font=self.ft0)
        self.text.insert(1.0, "\n")
        self.text.bind("<Return>", self.returnCb)
        self.text.pack(side=LEFT)
        self.button=Button(self.root, text="OK", font=self.ft1, command=self.cmdOk)
        self.button.pack(side=LEFT)
        self.root.mainloop()
    def returnCb(self, event=None):
        self.cmdOk()
    def cmdOk(self):
        sn = self.text.get(1.0, END)
        self.text.delete(1.0, END)
        self.text.insert(1.0,"\n")
        fout = open(FILE, 'w')

        if not fout:
            print "R/W open file error"
            return
        NEWLINE='\r\n'
        ctx='[device]' + NEWLINE
        ctx+='index=0' + NEWLINE
        ctx+=NEWLINE
        ctx+='[device0]' + NEWLINE
        ctx+='value=' + sn.strip() + NEWLINE
        fout.write(ctx)
        fout.close()

    def cmdOk2(self):
        sn=self.text.get(1.0, END)
        self.text.delete(1.0, END)
        fout=open(FILE,'r+w')
        if not fout:
            print "R/W open file error"
            return
        orgContent=fout.readlines()
        newContent=''
        flag=0
        for line in orgContent:
            #print line
            if flag:
                newLine='value="'+sn.strip()+'"'+'\r\n'
                newContent+=newLine
                flag=0
                continue
            if line.find('[device1]')>=0:
                #print "find it"
                flag=1
            newContent += line
        print 'newContent=\n' + newContent
        fout.close()
        fout=open(FILE,"w")
        #fout.truncate(0)
        fout.write(newContent)
        fout.close()

if __name__ == '__main__':
    dialog = Dialog()

