import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("400x300")

label1 = tk.Label(window, text = "First Number:")
label1.pack(pady = 5)
entry1 = tk.Entry(window)
entry1.pack(pady = 5)

label2 = tk.Label(window, text = "Second Number:")
label2.pack(pady = 5)
entry2 = tk.Entry(window)
entry2.pack(pady = 5)

result_label = tk.Label(window, text = "Result is here!", font = ("Arial", 14))
result_label.pack(pady = 10)

def add():
    a = float(entry1.get())
    b = float(entry2.get())
    result_label.config(text = f"Result: {a + b}")

def subtract():
    a = float(entry1.get())
    b = float(entry2.get())
    result_label.config(text = f"Result: {a - b}")

def multiply():
    a = float(entry1.get())   
    b = float(entry2.get()) 
    result_label.config(text = f"Result: {a * b}")

def divide():
    a = float(entry1.get())
    b = float(entry2.get())
    if b == 0:
        result_label.config(text = "Error: can't divide by zero")
    else:
        result_label.config(text = f"Result: {a / b}")


btn_add = tk.Button(window, text = "Add", width = 10, command = add)
btn_add.pack(pady = 3)

btn_sub = tk.Button(window, text = "Subtract", width = 10, command = subtract)
btn_sub.pack(pady = 3)

btn_mult = tk.Button(window, text = "Multiply", width = 10, command = multiply)
btn_mult.pack(pady = 3) 

btn_divide = tk.Button(window, text = "Divide", width = 10, command = divide)
btn_divide.pack(pady = 3) 

window.mainloop()