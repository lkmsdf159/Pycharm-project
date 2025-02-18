import tkinter  as tk
from tkinter  import messagebox

class Calculator:
    def __init__(self):
        self.operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else 'Error: Division by zero',
            '%': lambda x, y: x % y if y != 0 else 'Error: Division by zero'
        }

    def calculate(self, operator, num1, num2):
        return self.operations[operator](num1, num2)

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")
        self.calculator = Calculator()

        self.entry1 = tk.Entry(self.master)
        self.entry1.grid(row=0, column=0)

        self.entry2 = tk.Entry(self.master)
        self.entry2.grid(row=0, column=2)

        self.button_add = tk.Button(self.master, text="+", command=lambda: self.calculate('+'))
        self.button_add.grid(row=1, column=0)

        self.button_subtract = tk.Button(self.master, text="-", command=lambda: self.calculate('-'))
        self.button_subtract.grid(row=1, column=1)

        self.button_multiply = tk.Button(self.master, text="*", command=lambda: self.calculate('*'))
        self.button_multiply.grid(row=1, column=2)

        self.button_divide = tk.Button(self.master, text="/", command=lambda: self.calculate('/'))
        self.button_divide.grid(row=2, column=0)

        self.button_modulo = tk.Button(self.master, text="%", command=lambda: self.calculate('%'))
        self.button_modulo.grid(row=2, column=1)

        self.result_label = tk.Label(self.master, text="Result: ")
        self.result_label.grid(row=3, column=0, columnspan=3)

    def calculate(self, operator):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            result = self.calculator.calculate(operator, num1, num2)
            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except KeyError:
            messagebox.showerror("Error", "Invalid operator")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()