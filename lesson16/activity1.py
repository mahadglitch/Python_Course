import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont


class DenominationCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Denomination Calculator")
        self.root.geometry("550x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#F4F6F7")

        # Fonts
        self.title_font = tkfont.Font(
            family="Segoe UI", size=20, weight="bold")
        self.label_font = tkfont.Font(family="Segoe UI", size=12)
        self.result_font = tkfont.Font(family="Consolas", size=11)

        self.create_widgets()

    def create_widgets(self):
        # Header
        header = tk.Frame(self.root, bg="#2C3E50", pady=15)
        header.pack(fill="x")

        tk.Label(
            header,
            text="💵 Denomination Calculator (৳)",
            font=self.title_font,
            bg="#2C3E50",
            fg="white"
        ).pack()

        # Main Frame
        main = tk.Frame(self.root, bg="#F4F6F7", pady=30)
        main.pack(fill="both", expand=True)

        # Input Section
        input_frame = tk.Frame(main, bg="#F4F6F7")
        input_frame.pack(pady=20)

        tk.Label(
            input_frame,
            text="Enter Amount (৳)",
            font=self.label_font,
            bg="#F4F6F7"
        ).grid(row=0, column=0, padx=10)

        self.amount_entry = tk.Entry(
            input_frame,
            font=self.label_font,
            width=25,
            justify="center",
            bd=2
        )
        self.amount_entry.grid(row=0, column=1, padx=10)
        self.amount_entry.focus()

        self.amount_entry.bind(
            "<Return>", lambda e: self.calculate_denominations())

        # Calculate Button
        tk.Button(
            main,
            text="Calculate",
            font=self.label_font,
            bg="#27AE60",
            fg="white",
            padx=25,
            pady=8,
            command=self.calculate_denominations
        ).pack(pady=15)

        # Result Box
        result_frame = tk.Frame(main, bg="#D6DBDF", bd=2, relief="groove")
        result_frame.pack(padx=20, pady=10, fill="both", expand=True)

        tk.Label(
            result_frame,
            text="Denomination Breakdown",
            font=self.label_font,
            bg="#D6DBDF"
        ).pack(pady=8)

        self.result_text = tk.Text(
            result_frame,
            font=self.result_font,
            height=14,
            bg="#1C2833",
            fg="#58D68D",
            bd=0,
            state="disabled"
        )
        self.result_text.pack(padx=10, pady=10, fill="both", expand=True)

        # Bottom Buttons
        bottom = tk.Frame(main, bg="#F4F6F7")
        bottom.pack(pady=15)

        tk.Button(
            bottom,
            text="Clear",
            font=self.label_font,
            bg="#E74C3C",
            fg="white",
            width=10,
            command=self.clear_fields
        ).pack(side="left", padx=10)

        tk.Button(
            bottom,
            text="Exit",
            font=self.label_font,
            bg="#7F8C8D",
            fg="white",
            width=10,
            command=self.root.quit
        ).pack(side="left", padx=10)

    def calculate_denominations(self):
        try:
            amount = self.amount_entry.get().strip()

            if not amount:
                messagebox.showerror("Error", "Please enter an amount.")
                return

            amount = int(float(amount))

            if amount < 0:
                messagebox.showerror("Error", "Amount cannot be negative.")
                return

            notes_2000 = amount // 2000
            remaining = amount % 2000

            notes_500 = remaining // 500
            remaining %= 500

            notes_100 = remaining // 100
            remaining %= 100

            result = f"""
Total Amount : ৳{amount:,}

৳2000 x {notes_2000:<3} = ৳{notes_2000 * 2000:,}
৳500  x {notes_500:<3} = ৳{notes_500 * 500:,}
৳100  x {notes_100:<3} = ৳{notes_100 * 100:,}

Remaining : ৳{remaining}
"""

            self.result_text.config(state="normal")
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, result)
            self.result_text.config(state="disabled")

            if remaining:
                messagebox.showinfo(
                    "Note",
                    f"৳{remaining} cannot be divided using available denominations."
                )

        except ValueError:
            messagebox.showerror("Error", "Enter a valid numeric amount.")

    def clear_fields(self):
        self.amount_entry.delete(0, tk.END)
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", tk.END)
        self.result_text.config(state="disabled")
        self.amount_entry.focus()


# Main
if __name__ == "__main__":
    root = tk.Tk()
    DenominationCalculator(root)
    root.mainloop()
