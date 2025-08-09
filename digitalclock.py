import tkinter as tk
import time

def time_update():
    current_time = time.strftime('%H:%M:%S %p')  
    label.config(text=current_time)
    label.after(1000, time_update)

root = tk.Tk()
root.title("Digital Clock")  
root.geometry("400x200")  
root.configure(bg="black")

label = tk.Label(root, font=("Courier", 40), bg="black", fg="white")
label.pack(expand=True)

time_update()

root.mainloop()
