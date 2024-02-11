import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_310=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_310["font"] = ft
        GLabel_310["fg"] = "#333333"
        GLabel_310["justify"] = "center"
        GLabel_310["text"] = "label"
        GLabel_310.place(x=220,y=90,width=70,height=25)

        GButton_902=tk.Button(root)
        GButton_902["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_902["font"] = ft
        GButton_902["fg"] = "#000000"
        GButton_902["justify"] = "center"
        GButton_902["text"] = "przycisk"
        GButton_902.place(x=240,y=310,width=70,height=25)
        GButton_902["command"] = self.GButton_902_command

        GCheckBox_382=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_382["font"] = ft
        GCheckBox_382["fg"] = "#333333"
        GCheckBox_382["justify"] = "center"
        GCheckBox_382["text"] = "CheckBox"
        GCheckBox_382.place(x=400,y=170,width=70,height=25)
        GCheckBox_382["offvalue"] = "0"
        GCheckBox_382["onvalue"] = "1"
        GCheckBox_382["command"] = self.GCheckBox_382_command

        GLineEdit_783=tk.Entry(root)
        GLineEdit_783["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_783["font"] = ft
        GLineEdit_783["fg"] = "#333333"
        GLineEdit_783["justify"] = "center"
        GLineEdit_783["text"] = "Entry"
        GLineEdit_783.place(x=60,y=170,width=70,height=25)

    def GButton_902_command(self):
        print("command")


    def GCheckBox_382_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
