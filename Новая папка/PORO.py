from tkinter import *
from tkinter import filedialog
import tkinter as tk
import os

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent        
        self.initUI()

    def initUI(self):
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar,tearoff=0)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu) 
        
        button = tk.Button(self, text="Choose", command=self.onOpen)
        button.place(x=50, y=50)
        
    def onOpen(self):

        ftypes = [('.GRDECL', '*.GRDECL'),('All files', '*')]
        dlg = filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()
        if fl != '':
            df = self.readFile(fl, os.path.dirname(fl))
         

    def readFile(self, fullpath, dirname):
        f = open(fullpath)
        lines = f.readlines()
        my_list = []
        for item in lines:
            for j in list(item.split()):
                my_list.append(j)
        f.close()
        name = fullpath.split("/")[-1].split('.')[0]
        print(name)
        p = open(f"{dirname}/{name}.txt", 'w')
        for i in range(69,len(my_list)):
            if "*" not in set(str(my_list[i])):
                p.write(my_list[i])
                p.write("\n")
            else:
                a, b = map(float, list(my_list[i].split("*")))
                for my_list[i] in range(int(a)):
                    p.write(str(b))
                    p.write("\n")
        p.close()

        
def main():

    root = Tk()
    root.title('Convert Petrel to KMGEsim')
    ex = Example(root)
    root.geometry("150x150") 
    root.mainloop()

if __name__ == '__main__':
    main()  
