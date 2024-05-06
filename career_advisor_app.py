import tkinter as tk
from tkinter import *
from tkinter import ttk

career_app = tk.Tk()
career_app.title("Career Advisor App")
career_app.geometry("400x400")


def main():

    # Hides main window
    career_app.withdraw()

    # Established window to select level of English completed at school

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

    def maths():
        maths_wind = Toplevel(career_app)
        maths_wind.title("Maths")
        maths_wind.geometry("400x400")

        maths_label = ttk.Label(maths_wind, text= "Select level of Maths completed")
        maths_label.pack(pady=10)

        maths_var = tk.StringVar()

        # Radiobuttons (singular selection) since you can't do more than one kind of English
        # Started with English because all students in NSW must do it

        maths_radio1 = ttk.Radiobutton(maths_wind, text="Maths Standard", variable=maths_var, value="Maths Standard")
        maths_radio1.pack(anchor='w')

        maths_radio2 = ttk.Radiobutton(maths_wind, text="Maths Advanced", variable=maths_var, value="Maths Advanced")
        maths_radio2.pack(anchor='w')

        maths_radio3 = ttk.Radiobutton(maths_wind, text="Maths Ext 1", variable=maths_var, value="Maths Ext 1")
        maths_radio3.pack(anchor='w')

        maths_radio4 = ttk.Radiobutton(maths_wind, text="Maths Ext 2", variable=maths_var, value="Maths Ext 2")
        maths_radio4.pack(anchor='w')

    # "Next" button will close current window and open new window
    def close_window():
        english_wind.destroy()
        maths()



    next_button = ttk.Button(english_wind, text="Next", command=close_window)
    next_button.pack(pady=10)



start_btn = ttk.Button(career_app, text= "Start", command=main)
start_btn.pack(pady=10)

career_app.mainloop()