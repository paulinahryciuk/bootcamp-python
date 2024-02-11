import tkinter as tk

def on_click():
    print("przycisk zostl nacisniety")

app = tk.Tk()
app.title("przyklad")
button = tk.Button(app, text = "kliknij mnie", command=on_click)
button.pack()

app.mainloop()