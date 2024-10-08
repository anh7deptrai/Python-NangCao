import tkinter as tk
from tkinter import messagebox

class CasinoCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Casino Calculator")
        
        self.expression = ""
        
        # Entry để hiển thị kết quả
        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(root, textvariable=self.result_var, font=("Arial", 20), justify='right')
        self.result_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Nút số và phép toán
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(root, text=button, command=lambda b=button: self.on_button_click(b), font=("Arial", 15)).grid(row=row_val, column=col_val, sticky='nsew', padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        
        # Tăng kích thước cột và hàng
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.result_var.set("")
        elif char == '=':
            try:
                # Tính toán biểu thức
                result = str(eval(self.expression))
                self.result_var.set(result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
                self.result_var.set("")
        else:
            self.expression += str(char)
            self.result_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CasinoCalculator(root)
    root.mainloop()
