import tkinter as tk

def show_text():
    text = entry.get()
    print(f"wprowadzamy tekst {text}")

app = tk.Tk()
app.title("pole wprowadzenia")

entry = tk.Entry(app)
entry.pack()

button = tk.Button(app, text = "pokaz tekst", command = show_text)

button.pack(side=tk.BOTTOM)

app.mainloop()