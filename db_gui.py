import tkinter as tk
from tkinter import ttk


def main_window():
    root = tk.Tk()
    root.title("Blood Donor Database")
    root.geometry("600x300")

    tk.Label(root, text="Blood Donor Database").grid(column=0, row=0, columnspan=2)
    tk.Label(root, text="Name").grid(column=0, row=1)
    tk.Entry(root, width=50).grid(column=1, row=1)
    tk.Label(root, text="ID").grid(column=0, row=2)
    tk.Entry(root, width=50).grid(column=1, row=2)

    root.mainloop()


if __name__ == "__main__":
    main_window()