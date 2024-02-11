import tkinter

class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()


        self.label = tkinter.Label(self.main_window, text = 'witaj swiecie')
        self.label.pack(side = 'left')
        self.label2 = tkinter.Label(self.main_window, text='witaj swiecie2')
        self.label2.pack(side = 'top')
        self.label3 = tkinter.Label(self.main_window, text='witaj swiecie3')
        self.label3.pack(side='right')
        self.label4 = tkinter.Label(self.main_window, text='witaj swiecie4')
        self.label4.pack(side='bottom')

        tkinter.mainloop()




my_gui = MyGui()
