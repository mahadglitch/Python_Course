import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

class DenominationCalculator:
    def __init__(self, root): # constructor
        self.root = root
        self.root.title("Currency Denomination Calculator")
        self.root.geometry("600x700")
        self.root.resizable(True, True)
        self.root.config(bg="#B3C9DF")
        
        # Custom fonts
        self.title_font = tkfont.Font(family="Helvetica", size=20, weight="bold")
        self.label_font = tkfont.Font(family="Helvetica", size=12)
        self.result_font = tkfont.Font(family="Courier", size=11, weight="bold")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Title Frame
        title_frame = tk.Frame(self.root, bg="#73A19C", pady=15) # padding(even space) in the y coordinate
        title_frame.pack(fill="x")
        
        title_label = tk.Label(
            title_frame,
            text="💵 Denomination Calculator 💵",
            font=self.title_font,
            bg="#000000", # background color
            fg="#ECF0F1" # foreground color - color of text
        )
        title_label.pack()
        
        # Main Content Frame
        content_frame = tk.Frame(self.root, bg="#A074BB", pady=30)
        content_frame.pack(expand=True, fill="both", padx=20)
        
        # Amount Input Section
        input_frame = tk.Frame(content_frame, bg="#CE8488")
        input_frame.pack(pady=30)
        
        amount_label = tk.Label(
            input_frame,
            text="Enter Amount (₹):",
            font=self.label_font,
            bg="#CE8488",
            fg="#ECF0F1"
        )
        amount_label.grid(row=0, column=0, padx=10, sticky="w")
        
        self.amount_entry = tk.Entry(
            input_frame,
            font=self.label_font,
            width=50,
            bd=2,
            relief="solid",
            justify="center"
        )
        self.amount_entry.grid(row=0, column=1, padx=10)
        self.amount_entry.focus()
        
        # Bind Enter key to calculate
        self.amount_entry.bind('<Return>', lambda event: self.calculate_denominations())
        
        # Calculate Button
        calc_button = tk.Button(
            content_frame,
            text="Calculate",
            font=self.label_font,
            bg="#27AE60",
            fg="white",
            activebackground="#229954",
            activeforeground="white",
            cursor="hand2",
            bd=0,
            padx=30,
            pady=10,
            command=self.calculate_denominations
        )
        calc_button.pack(pady=20)
        
        # Result Frame
        self.result_frame = tk.Frame(content_frame, bg="#5D5074", bd=6, relief="solid")
        self.result_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        result_title = tk.Label(
            self.result_frame,
            text="Denomination Breakdown",
            font=tkfont.Font(family="Helvetica", size=14, weight="bold"),
            bg="#5D5074",
            fg="#ECF0F1"
        )
        result_title.pack(pady=10)
        
        # Result Text Widget
        self.result_text = tk.Text(
            self.result_frame,
            font=self.result_font,
            bg="#2C3E50",
            fg="#1ABC9C",
            bd=0,
            height=15,
            width=80,
            state="disabled",
            cursor="arrow"
        )
        self.result_text.pack(pady=10, padx=20)
        
        # Buttons Frame
        button_frame = tk.Frame(content_frame, bg="#2C3E50")
        button_frame.pack(pady=10)
        
        clear_button = tk.Button(
            button_frame,
            text="Clear",
            font=self.label_font,
            bg="#E74C3C",
            fg="white",
            activeforeground="white",
            cursor="hand2",
            bd=2,
            padx=20,
            pady=8,
            command=self.clear_fields
        )
        clear_button.pack(side="left", padx=10)
        
        exit_button = tk.Button(
            button_frame,
            text="Exit",
            font=self.label_font,
            bg="#95A5A6",
            fg="white",
            activeforeground="white",
            cursor="hand2",
            bd=2,
            padx=20,
            pady=8,
            command=self.root.quit
        )
        exit_button.pack(side="left", padx=10)
    
    def calculate_denominations(self):
        try:
            # Get amount from entry
            amount = self.amount_entry.get().strip()
            
            # Validate input
            if not amount:
                messagebox.showerror("Error", "Please enter an amount!")
                return
            
            amount = float(amount) # converting to float datatypes and into amount variable
            
            if amount < 0:
                messagebox.showerror("Error", "Amount cannot be negative!")
                return
            
            if amount % 1 != 0:
                messagebox.showwarning("Warning", "Decimals will be ignored. Using whole number only.")
                amount = int(amount)
            else:
                amount = int(amount)
            
            # Calculate denominations
            notes_2000 = amount // 2000
            remaining = amount % 2000
            
            notes_500 = remaining // 500
            remaining = remaining % 500
            
            notes_100 = remaining // 100
            remaining = remaining % 100
            
            # Display results
            self.result_text.config(state="normal")
            self.result_text.delete(1.0, tk.END)
            
            result = f"""
-----------------------------------------------------------------------------
║  Total Amount: ₹{amount:,}
---------------------------------|-------------------------------------------
║  ₹2000 Notes:  {notes_2000:>4} × ₹2000 = ₹{notes_2000*2000:,}
║  ₹500 Notes:   {notes_500:>4} × ₹500  = ₹{notes_500*500:,}
║  ₹100 Notes:   {notes_100:>4} × ₹100  = ₹{notes_100*100:,}
---------------------------------|-------------------------------------------
║  Remaining:    ₹{remaining:,}
-----------------------------------------------------------------------------
"""
            
            self.result_text.insert(1.0, result)
            self.result_text.config(state="disabled")
            
            # Show warning if there's remaining amount
            if remaining > 0:
                messagebox.showinfo(
                    "Information",
                    f"Amount ₹{remaining} cannot be paid with available denominations (₹2000, ₹500, ₹100)."
                )
        
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def clear_fields(self):
        self.amount_entry.delete(0, tk.END)
        self.result_text.config(state="normal")
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state="disabled")
        self.amount_entry.focus()


# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = DenominationCalculator(root)
    root.mainloop()