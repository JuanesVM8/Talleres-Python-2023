import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    current_text = screen.get()
    
    if text == "=":
        try:
            result = eval(current_text.replace(",", ""))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "AC":
        screen.set("")
    elif text == "CE":
        if current_text:
            new_text = current_text[:-1]
            screen.set(new_text)
    else:
        screen.set(current_text + text)

root = tk.Tk()
root.geometry("400x600")
root.title("Calculadora Fantastica")

# Fondo azul
root.configure(bg="#0078d4")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font=("Helvetica", 40), bg="white")
entry.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

# Botones del mismo tamaño y fondo 
buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'CE', '0', '=', '/',
    'AC',  
]

i = 0
for btn_text in buttons:
    if btn_text == "AC":
        button = tk.Button(button_frame, text=btn_text, font=("Helvetica", 20), padx=40, pady=40, bg="#a8c7e0")
        button.grid(row=4, column=0, columnspan=4, sticky="nsew")
    else:
        button = tk.Button(button_frame, text=btn_text, font=("Helvetica", 20), padx=40, pady=40, bg="#a8c7e0")
        button.grid(row=i // 4, column=i % 4, sticky="nsew")
    button.bind('<Button-1>', click)
    i += 1

# dependiendo de las filas acomodar los botones 
for i in range(5):
    button_frame.columnconfigure(i, weight=1)
for i in range(5):
    button_frame.rowconfigure(i, weight=1)

root.mainloop()
