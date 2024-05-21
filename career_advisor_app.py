import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd # API used to filter tables (from excel)
from tkinter import messagebox

career_app = tk.Tk()
career_app.title("Career Advisor App")
career_app.geometry("700x400")

user_selections = []

# Updates the label which reads "You've Selected: "
def update_selection_label():
    # Filter out empty strings from the list
    filtered_selections = [selection for selection in user_selections if selection]
    
    # Join the filtered selections with a comma and space
    selections_text = ", ".join(filtered_selections)
    selection_label.config(text=f"You've Selected: {selections_text}")

# Opens the window for the user to choose their level of English completed
def english():
    career_app.withdraw()
    
    english_wind = Toplevel(career_app)
    english_wind.title("English")
    english_wind.geometry("400x400")

    english_label = ttk.Label(english_wind, text= "Select level of English completed.")
    english_label.pack(pady=10)

    english_info = ttk.Label(english_wind, text="If you do Extension, you don't need to select Advanced.")
    english_info.pack(pady=10)

    eng_var = tk.StringVar()

    # Radiobuttons (singular selection) since you can't do more than one kind of English

    english_subjects = ["English Standard", 
                        "English Advanced", 
                        "English Extension 1", 
                        "English Extension 2", 
                        "English as an Aditional Language", 
                        "English Studies"]
    length = len(english_subjects)


    for i in range(length):
        radio_btn = ttk.Radiobutton(english_wind, 
                                    text=english_subjects[i], 
                                    variable=eng_var, 
                                    value=english_subjects[i])
        radio_btn.pack(anchor='w')

    def submit():
        if any(subject in user_selections for subject in english_subjects):

            if messagebox.askyesno(message="You have already selected an English subject. Are you sure you want to change it?", icon="warning", title="Warning"):
                user_selections.remove([subject for subject in user_selections if subject in english_subjects][0])
                user_selections.append(eng_var.get())
                english_wind.destroy()
                update_selection_label()
        else:
            user_selections.append(eng_var.get())
            english_wind.destroy()
            update_selection_label()

    next_button = ttk.Button(english_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

    def back():
        career_app.deiconify()
        english_wind.destroy()

    back_button = ttk.Button(english_wind, text="Back", command=back)
    back_button.pack(pady=10)

# If the user has completed maths, they can choose their level of maths
def maths():
    career_app.withdraw()
    
    maths_wind = Toplevel(career_app)
    maths_wind.title("Maths")
    maths_wind.geometry("400x400")

    maths_label = ttk.Label(maths_wind, text= "Select level of Maths completed")
    maths_label.pack(pady=10)

    maths_info = ttk.Label(maths_wind, text="If you do Extension, you don't need to select Advanced.")
    maths_info.pack(pady=10)

    maths_var = tk.StringVar()

    # Radiobuttons (singular selection) since you can't do more than one kind of Maths*

    math_subjects = ["Mathematics Standard",
                     "Mathematics Advanced",
                     "Mathematics Extension 1",
                     "Mathematics Extension 2"]
    
    length = len(math_subjects)

    for i in range(length):
        radio_btn = ttk.Radiobutton(maths_wind, text=math_subjects[i], variable=maths_var, value=math_subjects[i])
        radio_btn.pack(anchor='w')

    def submit():
        user_selections.append(maths_var.get())
        maths_wind.destroy()
        update_selection_label()

    next_button = ttk.Button(maths_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

    def back():
        career_app.deiconify()
        maths_wind.destroy()

    back_button = ttk.Button(maths_wind, text="Back", command=back)
    back_button.pack(pady=10)

# If the user is doing a science, this opens the window to choose the science(s)
def science():
    career_app.withdraw()
    
    sci_wind = Toplevel(career_app)
    sci_wind.title("Science")
    sci_wind.geometry("400x400")

    sci_label = ttk.Label(sci_wind, text= "Select Science(s) completed")
    sci_label.pack(pady=10)

    sci_info = ttk.Label(sci_wind, text="You can select at most three science subjects.")
    sci_info.pack(pady=10)

    # Checkbuttons don't need to do anything, so an empty function is created
    def empty():
        pass
    
    sci1_var = tk.StringVar()
    sci2_var = tk.StringVar()
    sci3_var = tk.StringVar()
    sci4_var = tk.StringVar()
    sci5_var = tk.StringVar()

    # Checkbuttons (multiple selection) since you can do more than one science

    sci_check1 = ttk.Checkbutton(sci_wind, text="Biology", command=empty, variable=sci1_var, onvalue="Biology", offvalue="")
    sci_check1.pack(anchor='w')

    sci_check2 = ttk.Checkbutton(sci_wind, text="Chemistry", command=empty, variable=sci2_var, onvalue="Chemistry", offvalue="")
    sci_check2.pack(anchor='w')

    sci_check3 = ttk.Checkbutton(sci_wind, text="Physics", command=empty, variable=sci3_var, onvalue="Physics", offvalue="")
    sci_check3.pack(anchor='w')

    sci_check4 = ttk.Checkbutton(sci_wind, text="Earth & Environmental", command=empty, variable=sci4_var, onvalue="Earth and Environmental", offvalue="")
    sci_check4.pack(anchor='w')

    sci_check5 = ttk.Checkbutton(sci_wind, text="Investigating Science", command=empty, variable=sci5_var, onvalue="Investigating Science", offvalue="")
    sci_check5.pack(anchor='w')

    def submit():
        sciences_selected = [sci_var.get() for sci_var in [sci1_var, sci2_var, sci3_var, sci4_var, sci5_var] if sci_var.get()]
        num_of_sciences = len(sciences_selected)
        
        # Check if more than three checkboxes are selected (NESA prevents students from doing more than three sciences)
        if num_of_sciences > 3:
            messagebox.showerror("Error", "Please select at most three science subjects.")
        else:
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

    def back():
        career_app.deiconify()
        sci_wind.destroy()

    back_button = ttk.Button(sci_wind, text="Back", command=back)
    back_button.pack(pady=10)

# If the user does a technology subject, this opens the window to choose the technology
def technology():
    career_app.withdraw()
    
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

    tech_check1 = ttk.Checkbutton(tech_wind, text="Design and Technology", command=empty, variable=tech1_var, onvalue="Design and Technology", offvalue="")
    tech_check1.pack(anchor='w')

    tech_check2 = ttk.Checkbutton(tech_wind, text="Software Design and Development", command=empty, variable=tech2_var, onvalue="Software Design", offvalue="")
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

    def back():
        career_app.deiconify()
        tech_wind.destroy()

    back_button = ttk.Button(tech_wind, text="Back", command=back)
    back_button.pack(pady=10)

# If the user does a language, this opens the window to choose the language(s)
def language():
    career_app.withdraw()
    
    lang_wind = Toplevel(career_app)
    lang_wind.title("Languages")
    lang_wind.geometry("400x400")

    lang_label = ttk.Label(lang_wind, text= "Select Language(s) completed")
    lang_label.pack(pady=10)

    lang_info = ttk.Label(lang_wind, text="You cannot select both beginners and continuers for the same language.")
    lang_info.pack(pady=10)
    
    lang_info2 = ttk.Label(lang_wind, text="You can remove a language by selecting it again.")
    lang_info2.pack(pady=10)

    china_beg_var = tk.StringVar()
    china_con_var = tk.StringVar()
    italy_beg_var = tk.StringVar()
    italy_cont_var = tk.StringVar()
    japan_beg_var = tk.StringVar()
    japan_cont_var = tk.StringVar()

    def empty():
        pass

    # Checkbuttons (multiple selection) since you can do more than one technology

    lang_check1 = ttk.Checkbutton(lang_wind, text="Chinese Beginners", command=empty, variable=china_beg_var, onvalue="Chinese Beg", offvalue="")
    lang_check1.pack(anchor='w')

    lang_check2 = ttk.Checkbutton(lang_wind, text="Chinese Continuers", command=empty, variable=china_con_var, onvalue="Chinese Cont", offvalue="")
    lang_check2.pack(anchor='w')

    lang_check3 = ttk.Checkbutton(lang_wind, text="Italian Beginners", command=empty, variable=italy_beg_var, onvalue="Italian Beg", offvalue="")
    lang_check3.pack(anchor='w')

    lang_check4 = ttk.Checkbutton(lang_wind, text="Italian Continuers", command=empty, variable=italy_cont_var, onvalue="Italian Cont", offvalue="")
    lang_check4.pack(anchor='w')

    lang_check5 = ttk.Checkbutton(lang_wind, text="Japanese Beginners", command=empty, variable=japan_beg_var, onvalue="Japanese Beg", offvalue="")
    lang_check5.pack(anchor='w')

    lang_check6 = ttk.Checkbutton(lang_wind, text="Japanese Continuers", command=empty, variable=japan_cont_var, onvalue="Japanese Cont", offvalue="")
    lang_check6.pack(anchor='w')

    def submit():
        if (china_beg_var.get() and china_con_var.get()) or (italy_beg_var.get() and italy_cont_var.get()) or (japan_beg_var.get() and japan_cont_var.get()):
            messagebox.showerror("Error", "You cannot select both beginners and continuers for the same language.")
        else:
            selected_subjects = [
                china_beg_var.get(),
                china_con_var.get(),
                italy_beg_var.get(),
                italy_cont_var.get(),
                japan_beg_var.get(),
                japan_cont_var.get()
            ]
            for subject in selected_subjects:
                if subject and subject in user_selections:
                    if messagebox.askyesno(message="You have already selected this language. Do you want to remove it?", icon="warning", title="Warning"):
                        user_selections.remove(subject)
                        lang_wind.destroy()
                        update_selection_label()
                    return
            user_selections.extend(selected_subjects)
            lang_wind.destroy()
            update_selection_label()


    next_button = ttk.Button(lang_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

    def back():
        career_app.deiconify()
        lang_wind.destroy()

    back_button = ttk.Button(lang_wind, text="Back", command=back)
    back_button.pack(pady=10)

# If the user does a humanities subject, this opens the window to choose the humanities subject(s)
def humanities():
    career_app.withdraw()
    
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

    hum_check4 = ttk.Checkbutton(hum_wind, text="Buisness Studies", command=empty, variable=hum4_var, onvalue="Buisness Studies", offvalue="")
    hum_check4.pack(anchor='w')

    hum_check5 = ttk.Checkbutton(hum_wind, text="Economics", command=empty, variable=hum5_var, onvalue="Economics", offvalue="")
    hum_check5.pack(anchor='w')

    hum_check6 = ttk.Checkbutton(hum_wind, text="Legal Studies", command=empty, variable=hum6_var, onvalue="Legal Studies", offvalue="")
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

    def back():
        career_app.deiconify()
        hum_wind.destroy()

    back_button = ttk.Button(hum_wind, text="Back", command=back)
    back_button.pack(pady=10)

# Contains the subjects which do not fit into a category
def misc():
    career_app.withdraw()
    
    misc_wind = Toplevel(career_app)
    misc_wind.title("Miscellaneous Subjects")
    misc_wind.geometry("400x400")

    misc_label = ttk.Label(misc_wind, text= "Select Technologies completed")
    misc_label.pack(pady=10)

    misc1_var = tk.StringVar()
    misc2_var = tk.StringVar()
    misc3_var = tk.StringVar()
    misc4_var = tk.StringVar()
    misc5_var = tk.StringVar()

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

    misc_check5 = ttk.Checkbutton(misc_wind, text="Visual Arts", command=empty, variable=misc5_var, onvalue="Visual Arts")
    misc_check5.pack(anchor='w')

    def submit():
        user_selections.extend([
            misc1_var.get() if misc1_var.get() else "",
            misc2_var.get() if misc2_var.get() else "",
            misc3_var.get() if misc3_var.get() else "",
            misc4_var.get() if misc4_var.get() else "",
            misc5_var.get() if misc5_var.get() else ""
        ])
        misc_wind.destroy()
        update_selection_label()

    next_button = ttk.Button(misc_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

    def back():
        career_app.deiconify()
        misc_wind.destroy()

    back_button = ttk.Button(misc_wind, text="Back", command=back)
    back_button.pack(pady=10)

# FOR LATER. ALLOWS ME TO FORMAT WIDGETS NICER.
# canvas = Canvas()

# English button. Opens english() (same for all the _selection variables)
english_selection = ttk.Button(career_app, text= "English", command=english)
english_selection.pack(pady=1)

maths_selection = ttk.Button(career_app, text= "Mathematics", command=maths)
maths_selection.pack(pady=2)

science_selection = ttk.Button(career_app, text= "Sciences", command=science)
science_selection.pack(pady=3)

tech_selection = ttk.Button(career_app, text= "Technological and Applied Studies", command=technology)
tech_selection.pack(pady=4)

language_selection = ttk.Button(career_app, text= "Languages", command=language)
language_selection.pack(pady=5)

humanities_selection = ttk.Button(career_app, text= "Humanities", command=humanities)
humanities_selection.pack(pady=6)

misc_selection = ttk.Button(career_app, text= "Miscellaneous", command=misc)
misc_selection.pack(pady=7)

selection_label = ttk.Label(career_app, text="You've Selected: ")
selection_label.pack(pady= 8)

# Opens the ranking window so the user can determine the rank of their subject based off enjoyment
def ranking():
    if len(user_selections) == 0:
        messagebox.showerror("Error", "Please select at least one subject before proceeding.")
        return
    elif not any(subject in user_selections for subject in ["English Advanced", "English Standard", "English Extension 1", "English Extension 2", "English as an Aditional Language", "English Studies"]):
        messagebox.showerror("Error", "Please select the level of English you have completed before proceeding.")
        return
    else:
        # Hides main window
        career_app.withdraw()
        
        # Establish properties for new win
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
            
            # Creates combo boxes for each subject chosen
            rank_var = StringVar()
            rank_vars.append(rank_var)
            rank_combo = ttk.Combobox(rank_win, textvariable=rank_var, values=filtered_selections)
            rank_combo.pack(pady=2)
            rank_combos.append(rank_combo)
            rank_combo.state(['readonly']) # prevents people typing their own responses into dropdowns


        # Slider for projected/predicted ATAR
        number_slider = ttk.Scale(rank_win, from_=0, to=99.95, length=350, orient="horizontal")
        number_slider.pack(pady=10)
        
        # Label to display the user's projected ATAR
        number_label = ttk.Label(rank_win, text="Projected ATAR: ")
        number_label.pack(pady=5)
        
        # Function to update the label with the projected ATAR
        def update_ATAR_label():
            number_label.config(text="Selected Number: " + "{:.2f}".format(number_slider.get()))
        
        # Bind the slider's event to the update_number_label function
        number_slider.bind("<ButtonRelease-1>", lambda event: update_ATAR_label())


        # TBC Is the function which will process the user's final choices
        def subject_filter():
            # New array for ranked subject list
            rankings = [rank_var.get() for rank_var in rank_vars]
            # print(rankings)
            
            # Use only the first subject in the rankings array
            filtered_rankings = rankings[:1]
            
            # Reads the data from the csv file (containing all the degrees, subjects, universities, etc.)
            df = pd.read_csv("uac_data.csv")

            # Splits the strings in the columns into lists
            df['Subjects'] = df['Suggested HSC Subjects'].str.split(', ')
            df['Universities'] = df['Universities Offering the Degree'].str.split(', ') # I get an error if I don't do this line for some reason

            # Filters the dataframe to only include rows where the subjects are in the rankings
            filtered_df = df[df['Subjects'].apply(lambda x: any(subject in x for subject in filtered_rankings))]

            # Prints out the degrees, universities, and recommended subjects (will remove later on, just for testing purposes)
            for index, row in filtered_df.iterrows():
                print(f"Degree: {row['Unique Course Name']}")
                print(f"Universities: {', '.join(row['Universities'])}")
                print(f"Recommended Courses: {', '.join(row['Subjects'])}")
                print()

        submit_button = ttk.Button(rank_win, text="Submit Rankings", command=subject_filter)
        submit_button.pack(pady=10)

# Button to open ranking window
start_btn = ttk.Button(career_app, text= "Start", command=ranking)
start_btn.pack(pady=10)

career_app.mainloop()


# TO DO

# After subjects are selected, user needs to order their subjects in order of enjoyment ✅
# (MAYBE) List of hobbies, co-cirriculars, sports, etc. to further differentiate choices
# Collate possible degrees into a table, with university and reccomended courses listed next to it ✅

    # EG.        Bachelor of Science |  USYD  |  Biology, Chemistry, Physics, Earth and Env, Inv Science

# Take prioritised subject and the student type they fit into (eg. Science student) and eliminate degrees which don't fit user ✅
# Produce degree that most fits user, alongside which University(ies) that offers that degree
# Underneath produce alternative degrees possibly based off their second and third highest subject