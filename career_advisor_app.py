import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas # API used to filter tables (from excel)

career_app = tk.Tk()
career_app.title("Career Advisor App")
career_app.geometry("700x400")

user_selections = []

def update_selection_label():
    # Filter out empty strings from the list
    filtered_selections = [selection for selection in user_selections if selection]
    
    # Join the filtered selections with a comma and space
    selections_text = ", ".join(filtered_selections)
    selection_label.config(text=f"You've Selected: {selections_text}")

def english():
    english_wind = Toplevel(career_app)
    english_wind.title("English")
    english_wind.geometry("400x400")

    english_label = ttk.Label(english_wind, text= "Select level of English completed")
    english_label.pack(pady=10)

    eng_var = tk.StringVar()

    # Radiobuttons (singular selection) since you can't do more than one kind of English

    eng_radio1 = ttk.Radiobutton(english_wind, text="English Standard", variable=eng_var, value="English Std")
    eng_radio1.pack(anchor='w')

    eng_radio2 = ttk.Radiobutton(english_wind, text="English Advanced", variable=eng_var, value="English Adv")
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
        user_selections.append(eng_var.get())
        english_wind.destroy()
        update_selection_label()

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

    maths_radio1 = ttk.Radiobutton(maths_wind, text="Maths Standard", variable=maths_var, value="Maths Std")
    maths_radio1.pack(anchor='w')

    maths_radio2 = ttk.Radiobutton(maths_wind, text="Maths Advanced", variable=maths_var, value="Maths Adv")
    maths_radio2.pack(anchor='w')

    maths_radio3 = ttk.Radiobutton(maths_wind, text="Maths Ext 1", variable=maths_var, value="Maths Ext 1")
    maths_radio3.pack(anchor='w')

    maths_radio4 = ttk.Radiobutton(maths_wind, text="Maths Ext 2", variable=maths_var, value="Maths Ext 2")
    maths_radio4.pack(anchor='w')

    # maths_radio5 = ttk.Radiobutton(maths_wind, text="No Maths", variable=maths_var, value="No Maths")
    # maths_radio5.pack(anchor='w')

    def submit():
        user_selections.append(maths_var.get())
        maths_wind.destroy()
        update_selection_label()

    next_button = ttk.Button(maths_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

def science():
    sci_wind = Toplevel(career_app)
    sci_wind.title("Science")
    sci_wind.geometry("400x400")

    sci_label = ttk.Label(sci_wind, text= "Select Science(s) completed")
    sci_label.pack(pady=10)

    sci1_var = tk.StringVar()
    sci2_var = tk.StringVar()
    sci3_var = tk.StringVar()
    sci4_var = tk.StringVar()
    sci5_var = tk.StringVar()


    def empty():
        pass

    # Checkbuttons (multiple selection) since you can do more than one science

    sci_check1 = ttk.Checkbutton(sci_wind, text="Biology", command=empty, variable=sci1_var, onvalue="Biology", offvalue="")
    sci_check1.pack(anchor='w')

    sci_check2 = ttk.Checkbutton(sci_wind, text="Chemistry", command=empty, variable=sci2_var, onvalue="Chemistry", offvalue="")
    sci_check2.pack(anchor='w')

    sci_check3 = ttk.Checkbutton(sci_wind, text="Physics", command=empty, variable=sci3_var, onvalue="Physics", offvalue="")
    sci_check3.pack(anchor='w')

    sci_check4 = ttk.Checkbutton(sci_wind, text="Earth and Environmental", command=empty, variable=sci4_var, onvalue="Earth and Environmental", offvalue="")
    sci_check4.pack(anchor='w')

    sci_check5 = ttk.Checkbutton(sci_wind, text="Investigating Science", command=empty, variable=sci5_var, onvalue="Investigating Science", offvalue="")
    sci_check5.pack(anchor='w')

    def submit():
        # .extend() is used. It's an alternative to .append() and allows us to add multiple things to an array at once
        user_selections.extend([
            sci1_var.get() if sci1_var.get() else "",
            sci2_var.get() if sci2_var.get() else "",
            sci3_var.get() if sci3_var.get() else "",
            sci4_var.get() if sci4_var.get() else "",
            sci5_var.get() if sci5_var.get() else ""
        ])
        sci_wind.destroy()
        update_selection_label()


    next_button = ttk.Button(sci_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

def technology():
    tech_wind = Toplevel(career_app)
    tech_wind.title("Technological and Applied Studies")
    tech_wind.geometry("400x400")

    tech_label = ttk.Label(tech_wind, text= "Select Technologies completed")
    tech_label.pack(pady=10)

    tech1_var = tk.StringVar()
    tech2_var = tk.StringVar()
    tech3_var = tk.StringVar()
    tech4_var = tk.StringVar()

    def empty():
        pass

    # Checkbuttons (multiple selection) since you can do more than one technology

    tech_check1 = ttk.Checkbutton(tech_wind, text="Design and Technology", command=empty, variable=tech1_var, onvalue="Design and Tech", offvalue="")
    tech_check1.pack(anchor='w')

    tech_check2 = ttk.Checkbutton(tech_wind, text="Software Design and Development", command=empty, variable=tech2_var, onvalue="Software", offvalue="")
    tech_check2.pack(anchor='w')

    tech_check3 = ttk.Checkbutton(tech_wind, text="Industrial Technology - Timber and Furniture", command=empty, variable=tech3_var, onvalue="Timber", offvalue="")
    tech_check3.pack(anchor='w')

    tech_check4 = ttk.Checkbutton(tech_wind, text="Engineering Studies", command=empty, variable=tech4_var, onvalue="Engineering", offvalue="")
    tech_check4.pack(anchor='w')

    def submit():
        user_selections.extend([
            tech1_var.get() if tech1_var.get() else "",
            tech2_var.get() if tech2_var.get() else "",
            tech3_var.get() if tech3_var.get() else "",
            tech4_var.get() if tech4_var.get() else ""
        ])
        tech_wind.destroy()
        update_selection_label()

    next_button = ttk.Button(tech_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

def language():
    lang_wind = Toplevel(career_app)
    lang_wind.title("Languages")
    lang_wind.geometry("400x400")

    lang_label = ttk.Label(lang_wind, text= "Select Language(s) completed")
    lang_label.pack(pady=10)

    lang1_var = tk.StringVar()
    lang2_var = tk.StringVar()
    lang3_var = tk.StringVar()
    lang4_var = tk.StringVar()
    lang5_var = tk.StringVar()
    lang6_var = tk.StringVar()

    def empty():
        pass

    # Checkbuttons (multiple selection) since you can do more than one technology

    lang_check1 = ttk.Checkbutton(lang_wind, text="Chinese Beginners", command=empty, variable=lang1_var, onvalue="Chinese Beg", offvalue="")
    lang_check1.pack(anchor='w')

    lang_check2 = ttk.Checkbutton(lang_wind, text="Chinese Continuers", command=empty, variable=lang2_var, onvalue="Chinese Cont", offvalue="")
    lang_check2.pack(anchor='w')

    lang_check3 = ttk.Checkbutton(lang_wind, text="Italian Beginners", command=empty, variable=lang3_var, onvalue="Italian Beg", offvalue="")
    lang_check3.pack(anchor='w')

    lang_check4 = ttk.Checkbutton(lang_wind, text="Italian Continuers", command=empty, variable=lang4_var, onvalue="Italian Cont", offvalue="")
    lang_check4.pack(anchor='w')

    lang_check5 = ttk.Checkbutton(lang_wind, text="Japanese Beginners", command=empty, variable=lang5_var, onvalue="Japanese Beg", offvalue="")
    lang_check5.pack(anchor='w')

    lang_check6 = ttk.Checkbutton(lang_wind, text="Japanese Continuers", command=empty, variable=lang6_var, onvalue="Japanese Cont", offvalue="")
    lang_check6.pack(anchor='w')

    def submit():
        user_selections.extend([
            lang1_var.get() if lang1_var.get() else "",
            lang2_var.get() if lang2_var.get() else "",
            lang3_var.get() if lang3_var.get() else "",
            lang4_var.get() if lang4_var.get() else "",
            lang5_var.get() if lang5_var.get() else "",
            lang6_var.get() if lang6_var.get() else ""
        ])
        lang_wind.destroy()
        update_selection_label()


    next_button = ttk.Button(lang_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

def humanities():
    hum_wind = Toplevel(career_app)
    hum_wind.title("Humanities")
    hum_wind.geometry("400x400")

    hum_label = ttk.Label(hum_wind, text= "Select Humanities completed")
    hum_label.pack(pady=10)

    hum1_var = tk.StringVar()
    hum2_var = tk.StringVar()
    hum3_var = tk.StringVar()
    hum4_var = tk.StringVar()
    hum5_var = tk.StringVar()
    hum6_var = tk.StringVar()
    hum7_var = tk.StringVar()
    hum8_var = tk.StringVar()
    hum9_var = tk.StringVar()

    def empty():
        pass

    # Checkbuttons (multiple selection) since you can do more than one technology

    hum_check1 = ttk.Checkbutton(hum_wind, text="Ancient History", command=empty, variable=hum1_var, onvalue="Ancient Hist", offvalue="")
    hum_check1.pack(anchor='w')

    hum_check2 = ttk.Checkbutton(hum_wind, text="Modern History", command=empty, variable=hum2_var, onvalue="Modern Hist", offvalue="")
    hum_check2.pack(anchor='w')

    hum_check3 = ttk.Checkbutton(hum_wind, text="History Extension", command=empty, variable=hum3_var, onvalue="History Ext", offvalue="")
    hum_check3.pack(anchor='w')

    hum_check4 = ttk.Checkbutton(hum_wind, text="Buisness Studies", command=empty, variable=hum4_var, onvalue="Buisness", offvalue="")
    hum_check4.pack(anchor='w')

    hum_check5 = ttk.Checkbutton(hum_wind, text="Economics", command=empty, variable=hum5_var, onvalue="Economics", offvalue="")
    hum_check5.pack(anchor='w')

    hum_check6 = ttk.Checkbutton(hum_wind, text="Legal Studies", command=empty, variable=hum6_var, onvalue="Legal", offvalue="")
    hum_check6.pack(anchor='w')

    hum_check7 = ttk.Checkbutton(hum_wind, text="Geography", command=empty, variable=hum7_var, onvalue="Geography", offvalue="")
    hum_check7.pack(anchor='w')

    hum_check8 = ttk.Checkbutton(hum_wind, text="Studies of Religion I", command=empty, variable=hum8_var, onvalue="SOR I", offvalue="")
    hum_check8.pack(anchor='w')

    hum_check9 = ttk.Checkbutton(hum_wind, text="Studies of Religion II", command=empty, variable=hum9_var, onvalue="SOR II", offvalue="")
    hum_check9.pack(anchor='w')

    def submit():
        user_selections.extend([
            hum1_var.get() if hum1_var.get() else "",
            hum2_var.get() if hum2_var.get() else "",
            hum3_var.get() if hum3_var.get() else "",
            hum4_var.get() if hum4_var.get() else "",
            hum5_var.get() if hum5_var.get() else "",
            hum6_var.get() if hum6_var.get() else "",
            hum7_var.get() if hum7_var.get() else "",
            hum8_var.get() if hum8_var.get() else "",
            hum9_var.get() if hum9_var.get() else ""
        ])
        hum_wind.destroy()
        update_selection_label()


    next_button = ttk.Button(hum_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

def misc():
    misc_wind = Toplevel(career_app)
    misc_wind.title("Miscellaneous Subjects")
    misc_wind.geometry("400x400")

    misc_label = ttk.Label(misc_wind, text= "Select Technologies completed")
    misc_label.pack(pady=10)

    misc1_var = tk.StringVar()
    misc2_var = tk.StringVar()
    misc3_var = tk.StringVar()
    misc4_var = tk.StringVar()

    def empty():
        pass

    # Checkbuttons (multiple selection) since you can do more than one technology

    misc_check1 = ttk.Checkbutton(misc_wind, text="PDHPE", command=empty, variable=misc1_var, onvalue="PDHPE", offvalue="")
    misc_check1.pack(anchor='w')

    misc_check2 = ttk.Checkbutton(misc_wind, text="Drama", command=empty, variable=misc2_var, onvalue="Drama", offvalue="")
    misc_check2.pack(anchor='w')

    misc_check3 = ttk.Checkbutton(misc_wind, text="Music 1", command=empty, variable=misc3_var, onvalue="Music `1", offvalue="")
    misc_check3.pack(anchor='w')

    misc_check4 = ttk.Checkbutton(misc_wind, text="Music 2", command=empty, variable=misc4_var, onvalue="Music 2", offvalue="")
    misc_check4.pack(anchor='w')

    def submit():
        user_selections.extend([
            misc1_var.get() if misc1_var.get() else "",
            misc2_var.get() if misc1_var.get() else "",
            misc3_var.get() if misc1_var.get() else "",
            misc4_var.get() if misc1_var.get() else ""
        ])
        misc_wind.destroy()
        update_selection_label()

    next_button = ttk.Button(misc_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

# canvas = Canvas()

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

selection_label = ttk.Label(career_app, text="You've Selected: ")
selection_label.pack(pady= 8)

def ranking():
    career_app.withdraw()
    
    rank_win = Toplevel(career_app)
    rank_win.title = "Favourite Subject"
    rank_win.geometry("400x400")

    rank_main_label = ttk.Label(rank_win, text= "Please rank your subjects based off enjoyment")
    rank_main_label.pack(pady=1)

    # Filter out empty strings
    filtered_selections = []
    for selection in user_selections:
        if selection:
            filtered_selections.append(selection)

    # Dropdown lists for each subject, user to select favourite to least fav
    rank_vars = []
    rank_combos = []
    # Enumerate allows you to access each item in an array, alongside a count value (important for ranking, stored in subject if I've applied this correctly)
    for i, subject in enumerate(filtered_selections, start=1): 
        subject_label = ttk.Label(rank_win, text=f"Rank {i} Subject:")
        subject_label.pack(pady=1)        
        
        rank_var = StringVar()
        rank_vars.append(rank_var)
        rank_combo = ttk.Combobox(rank_win, textvariable=rank_var, values=filtered_selections)
        rank_combo.pack(pady=2)
        rank_combos.append(rank_combo)
        rank_combo.state(['readonly']) # prevents people typing their own responses into dropdowns



    def submit_ranking():
        rankings = [rank_var.get() for rank_var in rank_vars]
        print(rankings)
        # print(subject)

    submit_button = ttk.Button(rank_win, text="Submit Rankings", command=submit_ranking)
    submit_button.pack(pady=10)


    # To Be Finished




start_btn = ttk.Button(career_app, text= "Start", command=ranking)
start_btn.pack(pady=10)

career_app.mainloop()


# TO DO

# After subjects are selected, user needs to order their subjects in order of enjoyment ✅
# (MAYBE) List of hobbies, co-cirriculars, sports, etc. to further differentiate choices
# Collate possible degrees into a table, with university and reccomended courses listed next to it

    # EG.        Bachelor of Science |  USYD  |  Biology, Chemistry, Physics, Earth and Env, Inv Science

# Take prioritised subject and the student type they fit into (eg. Science student) and eliminate degrees which don't fit user
# Produce degree that most fits user, alongside which University(ies) that offers that degree
# Underneath produce alternative degrees possibly based off their second and third highest subject