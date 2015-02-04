from Tkinter import *
import tkFileDialog
from ttk import *

import main as mn



class GUI(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   

        inputDir = ""
        outputDir = ""
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
                  
      
        self.parent.title("Stacking V0.1b")
        self.style = Style()
        self.style.theme_use("default")
        
        iFrame = Frame(self, relief=RAISED, borderwidth=1)
        iFrame.pack(fill=BOTH, expand=1)
        oFrame = Frame(self, relief=RAISED, borderwidth=1)
        oFrame.pack(fill=BOTH, expand=1)
        
        self.pack(fill=BOTH, expand=1)

        inputLabel = Label(iFrame, text="Input Directory:")
        inputLabel.pack(side=LEFT, padx=10)
        inputEntry = Entry(iFrame, width=50)
        inputEntry.pack(side=LEFT, padx=5)
        inputButton = Button(iFrame, text="Choose", command=lambda:self.chooseDir(inputEntry,0))
        inputButton.pack(side=LEFT, padx=5)

        outputLabel = Label(oFrame, text="Output Directory:")
        outputLabel.pack(side=LEFT, padx=5)
        outputEntry = Entry(oFrame, width=50)
        outputEntry.pack(side=LEFT, padx=5)
        outputButton = Button(oFrame, text="Choose", command=lambda:self.chooseDir(outputEntry,1))
        outputButton.pack(side=LEFT, padx=5)
        warningLabel = Label(self, text="Warning: The output directory's content will be deleted!")
        warningLabel.pack(side=LEFT, padx=5)

        closeButton = Button(self, text="Exit", command=self.close)
        closeButton.pack(side=RIGHT, padx=5)
        okButton = Button(self, text="Stack!", command=lambda:mn.stack(self.inputDir, self.outputDir))
        okButton.pack(side=RIGHT)

    def chooseDir(self,entry,inout):
        dirname = tkFileDialog.askdirectory(parent=self,initialdir="/",title='Please select a directory')
        if len(dirname ) > 0:
            print "You chose %s" % dirname 
            entry.delete(0,END)
            entry.insert(0,dirname)
            if inout == 0:
                self.inputDir = dirname
            else:
                self.outputDir = dirname
            return

    def close(self):
        self.parent.destroy()

def main():
    root = Tk()
    root.geometry("600x200+300+300")
    app = GUI(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
