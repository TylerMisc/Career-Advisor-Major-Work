import tkinter as tk
from tkinter import ttk

career_app = tk.Tk()
career_app.title("Career Advisor App")
career_app.geometry("400x400")

# Subject categories, to be ammended 
subject_categories = {
    "English": ["English"],
    "Mathematics": ["Mathematics"],
    "Subject 1": ["Physics", "Chemistry", "Biology"],
    "Subject 2": ["History", "Geography"],
    "Subject 3": ["Design and Technology", "Information Technology"],
    "Subject 4": ["French", "Spanish", "German"]
    }

subject_vars = []
subject_menus = []

# Dropdown menu for each subject
for category, subjects in subject_categories.items():
    label = ttk.Label(career_app, text=f"Select {category}:")
    label.pack(pady=5)
    var = tk.StringVar()
    subject_vars.append(var)
    menu = ttk.Combobox(career_app, values=subjects, textvariable=var)
    menu.pack(pady=5)
    subject_menus.append(menu)

career_app.mainloop()