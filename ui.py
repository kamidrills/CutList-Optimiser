import tkinter as tk
from tkinter import messagebox
from optimiser import CutListOptimizer

class CutOptimizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cut List Optimizer")

        self.stock_width_label = tk.Label(root, text="Stock Width (mm):")
        self.stock_width_label.grid(row=0, column=0, padx=10, pady=10)
        self.stock_width_entry = tk.Entry(root)
        self.stock_width_entry.grid(row=0, column=1, padx=10, pady=10)

        self.stock_height_label = tk.Label(root, text="Stock Height (mm):")
        self.stock_height_label.grid(row=1, column=0, padx=10, pady=10)
        self.stock_height_entry = tk.Entry(root)
        self.stock_height_entry.grid(row=1, column=1, padx=10, pady=10)

        self.cuts_label = tk.Label(root, text="Cuts (Width x Height in mm):")
        self.cuts_label.grid(row=2, column=0, padx=10, pady=10)
        self.cuts_entry = tk.Entry(root)
        self.cuts_entry.grid(row=2, column=1, padx=10, pady=10)

        self.optimize_button = tk.Button(root, text="Optimize", command=self.optimize_cuts)
        self.optimize_button.grid(row=3, column=0, columnspan=2, pady=10)

    def optimize_cuts(self):
        try:
            stock_width = int(self.stock_width_entry.get())
            stock_height = int(self.stock_height_entry.get())
            cuts_input = self.cuts_entry.get()

            # Parse cuts input (e.g., "1024x1000, 500x400, 300x200")
            cuts = [(int(dim.split('x')[0]), int(dim.split('x')[1])) for dim in cuts_input.split(',')]

            optimiser = CutListOptimizer(stock_width, stock_height, cuts)
            optimiser.optimize()
            optimiser.display_plan()

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for dimensions and cuts.")
