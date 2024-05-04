import tkinter as tk
from tkinter import messagebox
import math

# COCOMO constants
KLOC = 0.001  # Kilo lines of code
TABLE = {
    "Organic": [2.4, 1.05, 2.5, 0.38],
    "Semi-Detached": [3.0, 1.12, 2.5, 0.35],
    "Embedded": [3.6, 1.20, 2.5, 0.32]
}

def calculate_cocomo():
    size = int(size_entry.get())
    mode = mode_var.get()

    if size <= 0:
        messagebox.showerror("Error", "Size should be a positive number.")
        return

    if mode not in TABLE:
        messagebox.showerror("Error", "Invalid mode selected.")
        return

    table = TABLE[mode]
    effort = table[0] * math.pow(size, table[1])
    time = table[2] * math.pow(effort, table[3])
    staff = effort / time

    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"Effort: {effort:.2f} Person-Months\n")
    result_text.insert(tk.END, f"Time: {time:.2f} Months\n")
    result_text.insert(tk.END, f"Staff: {staff:.2f} Persons\n")

root = tk.Tk()
root.title("COCOMO Model")

tk.Label(root, text="Size (KLOC):").pack()
size_entry = tk.Entry(root)
size_entry.pack()

tk.Label(root, text="Mode:").pack()
mode_var = tk.StringVar(root)
mode_var.set("SELECT")
mode_options = ["Organic", "Semi-Detached", "Embedded"]
tk.OptionMenu(root, mode_var, *mode_options).pack()

tk.Button(root, text="Calculate", command=calculate_cocomo).pack()

result_text = tk.Text(root, height=10, width=50)
result_text.pack()

root.mainloop()