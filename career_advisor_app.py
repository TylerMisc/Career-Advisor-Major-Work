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

    eng_radio1 = ttk.Radiobutton(english_wind, text="English Standard", variable=eng_var, value="English Standard")
    eng_radio1.pack(anchor='w')

    eng_radio2 = ttk.Radiobutton(english_wind, text="English Advanced", variable=eng_var, value="English Advanced")
    eng_radio2.pack(anchor='w')

    eng_radio3 = ttk.Radiobutton(english_wind, text="English Ext 1", variable=eng_var, value="English Ext 1")
    eng_radio3.pack(anchor='w')

    eng_radio4 = ttk.Radiobutton(english_wind, text="English Ext 2", variable=eng_var, value="English Ext 2")
    eng_radio4.pack(anchor='w')

    eng_radio5 = ttk.Radiobutton(english_wind, text="English as an Aditional Language", variable=eng_var, value="EALD")
    eng_radio5.pack(anchor='w')

    eng_radio6 = ttk.Radiobutton(english_wind, text="English Studies", variable=eng_var, value="English Studies")
    eng_radio6.pack(anchor='w')

    def submit():
        english_wind.destroy()

    next_button = ttk.Button(english_wind, text="Submit", command=submit)
    next_button.pack(pady=10)
    
    return eng_var.get()

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

    maths_radio5 = ttk.Radiobutton(maths_wind, text="No Maths", variable=maths_var, value="No Maths")
    maths_radio5.pack(anchor='w')

    def submit():
        maths_wind.destroy()

    next_button = ttk.Button(maths_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

def science():
    sci_wind = Toplevel(career_app)
    sci_wind.title("Science")
    sci_wind.geometry("400x400")

    sci_label = ttk.Label(sci_wind, text= "Select Science(s) completed")
    sci_label.pack(pady=10)

    sci_var = tk.StringVar()

    def empty():
        pass

    # Checkbuttons (multiple selection) since you can do more than one science

    sci_check1 = ttk.Checkbutton(sci_wind, text="Biology", command=empty, variable=sci_var, onvalue="Biology", offvalue="")
    sci_check1.pack(anchor='w')

    sci_check2 = ttk.Checkbutton(sci_wind, text="Chemistry", command=empty, variable=sci_var, onvalue="Chemistry", offvalue="")
    sci_check2.pack(anchor='w')

    sci_check3 = ttk.Checkbutton(sci_wind, text="Physics", command=empty, variable=sci_var, onvalue="Physics", offvalue="")
    sci_check3.pack(anchor='w')

    sci_check4 = ttk.Checkbutton(sci_wind, text="Earth and Environmental", command=empty, variable=sci_var, onvalue="Earth and Environmental", offvalue="")
    sci_check4.pack(anchor='w')

    def submit():
        sci_wind.destroy()

    next_button = ttk.Button(sci_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

def technology():
    tech_wind = Toplevel(career_app)
    tech_wind.title("Technological and Applied Studies")
    tech_wind.geometry("400x400")

    tech_label = ttk.Label(tech_wind, text= "Select Technologies completed")
    tech_label.pack(pady=10)

    tech_var = tk.StringVar()

    def empty():
        pass

    # Checkbuttons (multiple selection) since you can do more than one technology

    tech_check1 = ttk.Checkbutton(tech_wind, text="Design and Technology", command=empty, variable=tech_var, onvalue="Design and Technology", offvalue="")
    tech_check1.pack(anchor='w')

    tech_check2 = ttk.Checkbutton(tech_wind, text="Software Design and Development", command=empty, variable=tech_var, onvalue="Software Design and Development", offvalue="")
    tech_check2.pack(anchor='w')

    tech_check3 = ttk.Checkbutton(tech_wind, text="Industrial Technology - Timber and Furniture", command=empty, variable=tech_var, onvalue="Timber", offvalue="")
    tech_check3.pack(anchor='w')

    tech_check4 = ttk.Checkbutton(tech_wind, text="Engineering Studies", command=empty, variable=tech_var, onvalue="Engineering", offvalue="")
    tech_check4.pack(anchor='w')

    def submit():
        tech_wind.destroy()

    next_button = ttk.Button(tech_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

def language():
    lang_wind = Toplevel(career_app)
    lang_wind.title("Languages")
    lang_wind.geometry("400x400")

    lang_label = ttk.Label(lang_wind, text= "Select Language(s) completed")
    lang_label.pack(pady=10)

    lang_var = tk.StringVar()

    def empty():
        pass

    # Checkbuttons (multiple selection) since you can do more than one technology

    lang_check1 = ttk.Checkbutton(lang_wind, text="Chinese Beginners", command=empty, variable=lang_var, onvalue="Chinese Beginners", offvalue="")
    lang_check1.pack(anchor='w')

    lang_check2 = ttk.Checkbutton(lang_wind, text="Chinese Continuers", command=empty, variable=lang_var, onvalue="Chinese Continuers", offvalue="")
    lang_check2.pack(anchor='w')

    lang_check3 = ttk.Checkbutton(lang_wind, text="Italian Beginners", command=empty, variable=lang_var, onvalue="Italian Beginners", offvalue="")
    lang_check3.pack(anchor='w')

    lang_check4 = ttk.Checkbutton(lang_wind, text="Italian Continuers", command=empty, variable=lang_var, onvalue="Italian Continuers", offvalue="")
    lang_check4.pack(anchor='w')

    lang_check5 = ttk.Checkbutton(lang_wind, text="Japanese Beginners", command=empty, variable=lang_var, onvalue="Japanese Beginners", offvalue="")
    lang_check5.pack(anchor='w')

    lang_check6 = ttk.Checkbutton(lang_wind, text="Japanese Continuers", command=empty, variable=lang_var, onvalue="Japanese Continuers", offvalue="")
    lang_check6.pack(anchor='w')

    def submit():
        lang_wind.destroy()

    next_button = ttk.Button(lang_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

def humanities():
    hum_wind = Toplevel(career_app)
    hum_wind.title("Humanities")
    hum_wind.geometry("400x400")

    hum_label = ttk.Label(hum_wind, text= "Select Humanities completed")
    hum_label.pack(pady=10)

    hum_var = tk.StringVar()

    def empty():
        pass

    # Checkbuttons (multiple selection) since you can do more than one technology

    hum_check1 = ttk.Checkbutton(hum_wind, text="Ancient History", command=empty, variable=hum_var, onvalue="Ancient History", offvalue="")
    hum_check1.pack(anchor='w')

    hum_check2 = ttk.Checkbutton(hum_wind, text="Modern History", command=empty, variable=hum_var, onvalue="Modern History", offvalue="")
    hum_check2.pack(anchor='w')

    hum_check3 = ttk.Checkbutton(hum_wind, text="History Extension", command=empty, variable=hum_var, onvalue="History Extension", offvalue="")
    hum_check3.pack(anchor='w')

    hum_check4 = ttk.Checkbutton(hum_wind, text="Buisness Studies", command=empty, variable=hum_var, onvalue="Buisness", offvalue="")
    hum_check4.pack(anchor='w')

    hum_check5 = ttk.Checkbutton(hum_wind, text="Economics", command=empty, variable=hum_var, onvalue="Economics", offvalue="")
    hum_check5.pack(anchor='w')

    hum_check6 = ttk.Checkbutton(hum_wind, text="Legal Studies", command=empty, variable=hum_var, onvalue="Legal Studies", offvalue="")
    hum_check6.pack(anchor='w')

    hum_check7 = ttk.Checkbutton(hum_wind, text="Geography", command=empty, variable=hum_var, onvalue="Geography", offvalue="")
    hum_check7.pack(anchor='w')

    hum_check8 = ttk.Checkbutton(hum_wind, text="Studies of Religion I", command=empty, variable=hum_var, onvalue="Studies of Religion I", offvalue="")
    hum_check8.pack(anchor='w')

    hum_check9 = ttk.Checkbutton(hum_wind, text="Studies of Religion II", command=empty, variable=hum_var, onvalue="Studies of Religion II", offvalue="")
    hum_check9.pack(anchor='w')

    def submit():
        hum_wind.destroy()

    next_button = ttk.Button(hum_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

def misc():
    misc_wind = Toplevel(career_app)
    misc_wind.title("Miscellaneous Subjects")
    misc_wind.geometry("400x400")

    misc_label = ttk.Label(misc_wind, text= "Select Technologies completed")
    misc_label.pack(pady=10)

    misc_var = tk.StringVar()

    def empty():
        pass

    # Checkbuttons (multiple selection) since you can do more than one technology

    misc_check1 = ttk.Checkbutton(misc_wind, text="PDHPE", command=empty, variable=misc_var, onvalue="PDHPE", offvalue="")
    misc_check1.pack(anchor='w')

    misc_check2 = ttk.Checkbutton(misc_wind, text="Drama", command=empty, variable=misc_var, onvalue="Drama", offvalue="")
    misc_check2.pack(anchor='w')

    misc_check3 = ttk.Checkbutton(misc_wind, text="Music 1", command=empty, variable=misc_var, onvalue="Music `1", offvalue="")
    misc_check3.pack(anchor='w')

    misc_check4 = ttk.Checkbutton(misc_wind, text="Music 2", command=empty, variable=misc_var, onvalue="Music 2", offvalue="")
    misc_check4.pack(anchor='w')

    def submit():
        misc_wind.destroy()

    next_button = ttk.Button(misc_wind, text="Submit", command=submit)
    next_button.pack(pady=10)


english_selection = ttk.Button(career_app, text= "English", command=english)
english_selection.pack(pady=1)

maths_selection = ttk.Button(career_app, text= "Maths", command=maths)
maths_selection.pack(pady=2)

science_selection = ttk.Button(career_app, text= "Science", command=science)
science_selection.pack(pady=3)

tech_selection = ttk.Button(career_app, text= "Technological and Applied Studies", command=technology)
tech_selection.pack(pady=4)

language_selection = ttk.Button(career_app, text= "Language", command=language)
language_selection.pack(pady=5)

humanities_selection = ttk.Button(career_app, text= "Humanities", command=humanities)
humanities_selection.pack(pady=6)

misc_selection = ttk.Button(career_app, text= "Miscellaneous", command=misc)
misc_selection.pack(pady=7)

def main():
    pass


start_btn = ttk.Button(career_app, text= "Start", command=main)
start_btn.pack(pady=10)


career_app.mainloop()