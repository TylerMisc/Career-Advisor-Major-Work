from tkinter import *
import tkinter as tk
from tkinter import ttk
import os

# Establishes Tkinter window properties
career_app = tk.Tk()
career_app.geometry(f"{1150}x{900}")
career_app.title("Career Advisor App")
career_app.resizable(False, False)

mainframe = ttk.Frame(career_app, padding = "3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

career_app.mainloop