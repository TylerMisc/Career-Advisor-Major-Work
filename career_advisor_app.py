import tkinter as tk
from tkinter import *
from tkinter import ttk

career_app = tk.Tk()
career_app.title("Career Advisor App")
career_app.geometry("400x400")

def english():
    english_wind = Toplevel(career_app)
    english_wind.title("English")
    english_wind.geometry("400x400")

    english_label = ttk.Label(english_wind, text= "Select level of English completed")
    english_label.pack(pady=10)

    eng_var = tk.StringVar()

    # Radiobuttons (singular selection) since you can't do more than one kind of English
    # Started with English because all students in NSW must do it

    eng_radio1 = ttk.Radiobutton(english_wind, text="English Standard", variable=eng_var, value="English Standard")
    eng_radio1.pack(anchor='w')

    eng_radio2 = ttk.Radiobutton(english_wind, text="English Advanced", variable=eng_var, value="English Advanced")
    eng_radio2.pack(anchor='w')

    eng_radio3 = ttk.Radiobutton(english_wind, text="English Ext 1", variable=eng_var, value="English Ext 1")
    eng_radio3.pack(anchor='w')

    eng_radio4 = ttk.Radiobutton(english_wind, text="English Ext 2", variable=eng_var, value="English Ext 2")
    eng_radio4.pack(anchor='w')

    def submit():
        english_wind.destroy()

    next_button = ttk.Button(english_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

    return english_wind

def maths():
    maths_wind = Toplevel(career_app)
    maths_wind.title("Maths")
    maths_wind.geometry("400x400")

    maths_label = ttk.Label(maths_wind, text= "Select level of Maths completed")
    maths_label.pack(pady=10)

    maths_var = tk.StringVar()

    # Radiobuttons (singular selection) since you can't do more than one kind of English

    maths_radio1 = ttk.Radiobutton(maths_wind, text="Maths Standard", variable=maths_var, value="Maths Standard")
    maths_radio1.pack(anchor='w')

    maths_radio2 = ttk.Radiobutton(maths_wind, text="Maths Advanced", variable=maths_var, value="Maths Advanced")
    maths_radio2.pack(anchor='w')

    maths_radio3 = ttk.Radiobutton(maths_wind, text="Maths Ext 1", variable=maths_var, value="Maths Ext 1")
    maths_radio3.pack(anchor='w')

    maths_radio4 = ttk.Radiobutton(maths_wind, text="Maths Ext 2", variable=maths_var, value="Maths Ext 2")
    maths_radio4.pack(anchor='w')

    def submit():
        maths_wind.destroy()

    next_button = ttk.Button(maths_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

def science():
    sci_wind = Toplevel(career_app)
    sci_wind.title("Science")
    sci_wind.geometry("400x400")

    sci_label = ttk.Label(sci_wind, text= "Select level of Science completed")
    sci_label.pack(pady=10)

    sci_var = tk.StringVar()

    def empty():
        pass

    # Checkbuttons (multiple selection) since you can do more than one science

    sci_radio1 = ttk.Checkbutton(sci_wind, text="Biology", command=empty, variable=sci_var, onvalue="Biology", offvalue="")
    sci_radio1.pack(anchor='w')

    sci_radio2 = ttk.Checkbutton(sci_wind, text="Chemistry", command=empty, variable=sci_var, onvalue="Chemistry", offvalue="")
    sci_radio2.pack(anchor='w')

    sci_radio3 = ttk.Checkbutton(sci_wind, text="Physics", command=empty, variable=sci_var, onvalue="Physics", offvalue="")
    sci_radio3.pack(anchor='w')

    sci_radio4 = ttk.Checkbutton(sci_wind, text="Earth and Environmental", command=empty, variable=sci_var, onvalue="Earth and Environmental", offvalue="")
    sci_radio4.pack(anchor='w')

    def submit():
        sci_wind.destroy()

    next_button = ttk.Button(sci_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

def test():
    print("hello")


english_selection = ttk.Button(career_app, text= "English", command=english)
english_selection.pack(pady=1)

maths_selection = ttk.Button(career_app, text= "Maths", command=maths)
maths_selection.pack(pady=2)

science_selection = ttk.Button(career_app, text= "Science", command=science)
science_selection.pack(pady=3)

tech_selection = ttk.Button(career_app, text= "Technology", command=test)
tech_selection.pack(pady=4)

language_selection = ttk.Button(career_app, text= "Language", command=test)
language_selection.pack(pady=5)

humanities_selection = ttk.Button(career_app, text= "Humanities", command=test)
humanities_selection.pack(pady=6)

misc_selection = ttk.Button(career_app, text= "Miscellaneous", command=test)
misc_selection.pack(pady=7)

def main():
    pass


start_btn = ttk.Button(career_app, text= "Start", command=main)
start_btn.pack(pady=10)


career_app.mainloop()