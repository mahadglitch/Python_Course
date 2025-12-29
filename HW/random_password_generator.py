import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_var.get()

    if length > 12:
        messagebox.showerror("Error", "Password length cannot exceed 12!")
        return

    chars = ""
    if lower_var.get():
        chars += string.ascii_lowercase
    if upper_var.get():
        chars += string.ascii_uppercase
    if number_var.get():
        chars += string.digits
    if special_var.get():
        chars += string.punctuation

    if not chars:
        messagebox.showerror("Error", "Select at least one option!")
        return

    password = "".join(random.choice(chars) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# ---------------- UI ----------------
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x360")
root.resizable(False, False)

tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

lower_var = tk.BooleanVar(value=True)
upper_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Lowercase Letters (a-z)", variable=lower_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Uppercase Letters (A-Z)", variable=upper_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Numbers (0-9)", variable=number_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Special Characters (!@#$)", variable=special_var).pack(anchor="w", padx=20)

# Length selector (LIMITED)
tk.Label(root, text="Password Length (Max 12)").pack(pady=5)
length_var = tk.IntVar(value=12)
tk.Spinbox(
    root,
    from_=6,
    to=12,
    textvariable=length_var,
    width=5
).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

result_entry = tk.Entry(root, width=30, font=("Arial", 12))
result_entry.pack(pady=5)

tk.Button(root, text="Copy", command=copy_password).pack()

root.mainloop()
