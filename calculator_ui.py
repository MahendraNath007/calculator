# calculator_ui.py

import tkinter as tk
from tkinter import messagebox
from calculator_logic import CalculatorLogic


class CalculatorUI:
    def __init__(self, root):
        self.logic = CalculatorLogic()
        self.root = root
        self.root.title("Structured Calculator")
        self.root.geometry("350x300")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Enter First Number:").pack()
        self.num1_entry = tk.Entry(self.root)
        self.num1_entry.pack()

        tk.Label(self.root, text="Enter Second Number:").pack()
        self.num2_entry = tk.Entry(self.root)
        self.num2_entry.pack()

        self.result_label = tk.Label(self.root, text="Result:", font=("Arial", 12))
        self.result_label.pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack()

        tk.Button(frame, text="Add", width=10, command=self.perform_add).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame, text="Subtract", width=10, command=self.perform_subtract).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(frame, text="Multiply", width=10, command=self.perform_multiply).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(frame, text="Divide", width=10, command=self.perform_divide).grid(row=1, column=1, padx=5, pady=5)

    def get_inputs(self):
        try:
            return float(self.num1_entry.get()), float(self.num2_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers")
            return None, None

    def perform_add(self):
        a, b = self.get_inputs()
        if a is not None:
            self.result_label.config(text=f"Result: {self.logic.add(a, b)}")

    def perform_subtract(self):
        a, b = self.get_inputs()
        if a is not None:
            self.result_label.config(text=f"Result: {self.logic.subtract(a, b)}")

    def perform_multiply(self):
        a, b = self.get_inputs()
        if a is not None:
            self.result_label.config(text=f"Result: {self.logic.multiply(a, b)}")

    def perform_divide(self):
        a, b = self.get_inputs()
        if a is not None:
            try:
                result = self.logic.divide(a, b)
                self.result_label.config(text=f"Result: {result}")
            except ZeroDivisionError as e:
                messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorUI(root)
    root.mainloop()