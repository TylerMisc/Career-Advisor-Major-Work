import tkinter as tk # GUI Library
from tkinter import * # Imports all of tkinter
from tkinter import ttk # Themed Tkinter widgets
import pandas as pd # API used to filter tables (from excel)
from tkinter import messagebox # Error messages
from tkinter.scrolledtext import ScrolledText # Scrolled text widget

# Root window
career_app = tk.Tk()
career_app.title("Career Advisor App")
career_app.geometry("500x600") # Sets the size of the window
career_app.configure(bg="#e6ffe6") # Sets the background colour of the window

# Stores the subjects that the user has selected
user_selections = []

# Styling for the widgets
style = ttk.Style()
style.configure("TButton", background="#00264d", foreground="black", font=("Helvetica", 10), padding=7)
style.configure("TLabel", background='#e6ffe6', font=("Helvetica", 10))
style.configure("TCombobox", fieldbackground='#e6ffe6', font=("Helvetica", 10))
style.map("TCombobox", background=[("readonly", "white"), ('active', '#e6ffe6')])
style.configure("TCheckbutton", background='#e6ffe6', font=("Helvetica", 10))
style.configure("TScale", background="#e6ffe6", foreground="white", font=("Helvetica", 10))
style.configure("TRadiobutton", background='#e6ffe6', font=("Helvetica", 10))

# Updates the label which reads "You've Selected: "
def update_selection_label():
    # Filter out empty strings from the list
    filtered_selections = [selection for selection in user_selections if selection]
    
    # Join the filtered selections with a comma and space
    selections_text = ", ".join(filtered_selections)
    selection_label.config(text=f"You've Selected: {selections_text}")

# Opens the window for the user to choose their level of English completed
def english():
    # Closes the main window
    career_app.withdraw()
    
    # Establish properties for new window
    english_wind = Toplevel(career_app)
    english_wind.title("English")
    english_wind.geometry("400x400")
    english_wind.configure(bg="#e6ffe6")

    # Labels for the window
    english_label = ttk.Label(english_wind, text= "Select level of English completed.")
    english_label.pack(pady=10)

    english_info = ttk.Label(english_wind, text="If you do Extension, you don't need to select Advanced.")
    english_info.pack(pady=10)

    # Variable to store the user's selection
    eng_var = tk.StringVar()


    # List of English subjects
    english_subjects = ["English Standard", 
                        "English Advanced", 
                        "English Extension 1", 
                        "English Extension 2", 
                        "English as an Additional Language", 
                        "English Studies"]
    length = len(english_subjects)

    # Loops through the list of English subjects and creates a radio button for each one
    for i in range(length):
        radio_btn = ttk.Radiobutton(english_wind, 
                                    text=english_subjects[i], 
                                    variable=eng_var, 
                                    value=english_subjects[i])
        radio_btn.pack(anchor='w')

    # Function to submit the user's selection
    def submit():
        # Check if the user has already selected an English subject
        if any(subject in user_selections for subject in english_subjects):

            # If they have, ask if they want to change it
            if messagebox.askyesno(message="You have already selected an English subject. Are you sure you want to change it?", icon="warning", title="Warning"):
                user_selections.remove([subject for subject in user_selections if subject in english_subjects][0]) # removes the selected English subject
                user_selections.append(eng_var.get()) # adds the new selected English subject
                english_wind.destroy() # closes the window
                update_selection_label() # updates the label
        else:
            user_selections.append(eng_var.get()) # adds the selected English subject
            english_wind.destroy() # closes the window
            update_selection_label() # updates the label
            career_app.deiconify() # shows the main window

    # Button to submit the user's selection
    next_button = ttk.Button(english_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

    # Function to go back to the main window
    def back():
        career_app.deiconify()
        english_wind.destroy()

    back_button = ttk.Button(english_wind, text="Back", command=back)
    back_button.pack(pady=10)

# If the user has completed maths, they can choose their level of maths
def maths():
    # Hides the main window
    career_app.withdraw()
    
    # Properties for the new window
    maths_wind = Toplevel(career_app)
    maths_wind.title("Maths")
    maths_wind.geometry("400x400")
    maths_wind.configure(bg="#e6ffe6")

    maths_label = ttk.Label(maths_wind, text= "Select level of Maths completed")
    maths_label.pack(pady=10)

    maths_info = ttk.Label(maths_wind, text="If you do Extension, you don't need to select Advanced.")
    maths_info.pack(pady=10)

    maths_var = tk.StringVar()

    # List of maths subjects
    math_subjects = ["Mathematics Standard",
                     "Mathematics Advanced",
                     "Mathematics Extension 1",
                     "Mathematics Extension 2"]
    length = len(math_subjects)

    # Loops through the list of maths subjects and creates a radio button for each one
    for i in range(length):
        radio_btn = ttk.Radiobutton(maths_wind, text=math_subjects[i], variable=maths_var, value=math_subjects[i])
        radio_btn.pack(anchor='w')

    def submit():
        user_selections.append(maths_var.get())
        maths_wind.destroy()
        update_selection_label()
        career_app.deiconify()

    next_button = ttk.Button(maths_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

    def back():
        career_app.deiconify()
        maths_wind.destroy()

    back_button = ttk.Button(maths_wind, text="Back", command=back)
    back_button.pack(pady=10)

# If the user is doing a science, this opens the window to choose the science(s)
def science():
    # Hides the main window
    career_app.withdraw()
    
    # Properties for the new window
    sci_wind = Toplevel(career_app)
    sci_wind.title("Science")
    sci_wind.geometry("400x400")
    sci_wind.configure(bg="#e6ffe6")

    sci_label = ttk.Label(sci_wind, text= "Select Science(s) completed")
    sci_label.pack(pady=10)

    sci_info = ttk.Label(sci_wind, text="You can select at most three science subjects.")
    sci_info.pack(pady=10)

    # Checkboxes in Tkinter require a function, but since they don't need to do anything, we can just pass
    def empty():
        pass
    
    # Variables to store the user's selection
    bio_var = tk.StringVar()
    chem_var = tk.StringVar()
    phys_var = tk.StringVar()
    eae_var = tk.StringVar()
    inv_var = tk.StringVar()

    # Checkbuttons (multiple selection) since you can do more than one science

    bio_check = ttk.Checkbutton(sci_wind, text="Biology", command=empty, variable=bio_var, onvalue="Biology", offvalue="")
    bio_check.pack(anchor='w')

    chem_check = ttk.Checkbutton(sci_wind, text="Chemistry", command=empty, variable=chem_var, onvalue="Chemistry", offvalue="")
    chem_check.pack(anchor='w')

    phys_check = ttk.Checkbutton(sci_wind, text="Physics", command=empty, variable=phys_var, onvalue="Physics", offvalue="")
    phys_check.pack(anchor='w')

    eae_check = ttk.Checkbutton(sci_wind, text="Earth & Environmental", command=empty, variable=eae_var, onvalue="Earth and Environmental", offvalue="")
    eae_check.pack(anchor='w')

    inv_check = ttk.Checkbutton(sci_wind, text="Investigating Science", command=empty, variable=inv_var, onvalue="Investigating Science", offvalue="")
    inv_check.pack(anchor='w')

    def submit():
        global user_selections
        global duplicates
        
        # Stores the selected sciences in an array
        sciences_selected = [sci_var.get() for sci_var in [bio_var, chem_var, phys_var, eae_var, inv_var] if sci_var.get()]
        num_of_sciences = len(sciences_selected)
        
        # Check if more than three checkboxes are selected (NESA prevents students from doing more than three sciences)
        if num_of_sciences > 3:
            messagebox.showerror("Error", "Please select at most three science subjects.")
        else:
            # Check if any selected science subjects have already been selected before
            duplicates = [subject for subject in sciences_selected if subject in user_selections]
            if duplicates:
                message = "You have already selected these subject(s), would you like to remove them?"
                response = messagebox.askyesno("Duplicate Subjects", message)
                if response:
                    # Remove the duplicate subjects from user_selections
                    user_selections = [subject for subject in user_selections if subject not in duplicates]
                    sci_wind.destroy()
                    update_selection_label()
                    career_app.deiconify()
                else:
                    return  # Exit the function without updating the selections
            
            else:
                # .extend() is used. It's an alternative to .append() and allows us to add multiple things to an array at once
                user_selections.extend([
                    bio_var.get() if bio_var.get() else "",
                    chem_var.get() if chem_var.get() else "",
                    phys_var.get() if phys_var.get() else "",
                    eae_var.get() if eae_var.get() else "",
                    inv_var.get() if inv_var.get() else ""
                ])
        
                sci_wind.destroy()
                update_selection_label()
                career_app.deiconify()


    next_button = ttk.Button(sci_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

    def back():
        career_app.deiconify()
        sci_wind.destroy()

    back_button = ttk.Button(sci_wind, text="Back", command=back)
    back_button.pack(pady=10)

# If the user does a technology subject, this opens the window to choose the technology
def technology():
    # Hides the main window
    career_app.withdraw()
    
    # Properties for the new window
    tech_wind = Toplevel(career_app)
    tech_wind.title("Technological and Applied Studies")
    tech_wind.geometry("400x400")
    tech_wind.configure(bg="#e6ffe6")

    tech_label = ttk.Label(tech_wind, text= "Select Technologies completed")
    tech_label.pack(pady=10)

    # Variables to store the user's selection
    dt_var = tk.StringVar()
    sdd_var = tk.StringVar()
    timb_var = tk.StringVar()
    engi_var = tk.StringVar()

    def empty():
        pass

    # Checkbuttons (multiple selection) since you can do more than one technology

    dt_check = ttk.Checkbutton(tech_wind, text="Design and Technology", command=empty, variable=dt_var, onvalue="Design and Technology", offvalue="")
    dt_check.pack(anchor='w')

    sdd_check = ttk.Checkbutton(tech_wind, text="Software Design and Development", command=empty, variable=sdd_var, onvalue="Software Design and Development", offvalue="")
    sdd_check.pack(anchor='w')

    timber_check = ttk.Checkbutton(tech_wind, text="Industrial Technology - Timber and Furniture", command=empty, variable=timb_var, onvalue="Timber", offvalue="")
    timber_check.pack(anchor='w')

    engineering_check = ttk.Checkbutton(tech_wind, text="Engineering Studies", command=empty, variable=engi_var, onvalue="Engineering", offvalue="")
    engineering_check.pack(anchor='w')

    def submit():
        # These variables need to be global so they can be accessed outside of the function
        global user_selections
        global duplicates

        tech_selected = [tech_var.get() for tech_var in [dt_var, sdd_var, timb_var, engi_var] if tech_var.get()]

        # Checks if a subject has already been selected
        duplicates = [subject for subject in tech_selected if subject in user_selections]
        if duplicates:
            message = "You have already selected these subject(s), would you like to remove them?"
            response = messagebox.askyesno("Duplicate Subjects", message)
            if response:
                user_selections = [subject for subject in user_selections if subject not in duplicates]
                tech_wind.destroy()
                update_selection_label()
                career_app.deiconify()
            else:
                return
        else:
            user_selections.extend([
                dt_var.get() if dt_var.get() else "",
                sdd_var.get() if sdd_var.get() else "",
                timb_var.get() if timb_var.get() else "",
                engi_var.get() if engi_var.get() else ""
            ])

            tech_wind.destroy()
            update_selection_label()
            career_app.deiconify()

    next_button = ttk.Button(tech_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

    def back():
        career_app.deiconify()
        tech_wind.destroy()

    back_button = ttk.Button(tech_wind, text="Back", command=back)
    back_button.pack(pady=10)

# If the user does a language, this opens the window to choose the language(s)
def language():
    # Hides the main window
    career_app.withdraw()
    
    # Properties for the new window
    lang_wind = Toplevel(career_app)
    lang_wind.title("Languages")
    lang_wind.geometry("400x400")
    lang_wind.configure(bg="#e6ffe6")

    lang_label = ttk.Label(lang_wind, text= "Select Language(s) completed")
    lang_label.pack(pady=10)

    lang_info = ttk.Label(lang_wind, text="You cannot select both beginners and continuers for the same language.")
    lang_info.pack(pady=10)

    # Variables to store the user's selection
    china_beg_var = tk.StringVar()
    china_con_var = tk.StringVar()
    italy_beg_var = tk.StringVar()
    italy_cont_var = tk.StringVar()
    japan_beg_var = tk.StringVar()
    japan_cont_var = tk.StringVar()

    def empty():
        pass

    # Checkbuttons (multiple selection) since you can do more than one language

    chi_b_check = ttk.Checkbutton(lang_wind, text="Chinese Beginners", command=empty, variable=china_beg_var, onvalue="Chinese Beg", offvalue="")
    chi_b_check.pack(anchor='w')

    chi_c_check = ttk.Checkbutton(lang_wind, text="Chinese Continuers", command=empty, variable=china_con_var, onvalue="Chinese Cont", offvalue="")
    chi_c_check.pack(anchor='w')

    ita_b_check = ttk.Checkbutton(lang_wind, text="Italian Beginners", command=empty, variable=italy_beg_var, onvalue="Italian Beg", offvalue="")
    ita_b_check.pack(anchor='w')

    ita_c_check = ttk.Checkbutton(lang_wind, text="Italian Continuers", command=empty, variable=italy_cont_var, onvalue="Italian Cont", offvalue="")
    ita_c_check.pack(anchor='w')

    japa_b_check = ttk.Checkbutton(lang_wind, text="Japanese Beginners", command=empty, variable=japan_beg_var, onvalue="Japanese Beg", offvalue="")
    japa_b_check.pack(anchor='w')

    japa_c_check = ttk.Checkbutton(lang_wind, text="Japanese Continuers", command=empty, variable=japan_cont_var, onvalue="Japanese Cont", offvalue="")
    japa_c_check.pack(anchor='w')

    def submit():
        # Detects if a user has selected both a beginners and continuers course
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
                # Detects if the user has selected a subject that they've already selected
                if subject and subject in user_selections:
                    if messagebox.askyesno(message="You have already selected this language. Do you want to remove it?", icon="warning", title="Warning"):
                        user_selections.remove(subject) # removes subject
                        lang_wind.destroy()
                        update_selection_label()
                        career_app.deiconify()
                    return
            user_selections.extend(selected_subjects)
            lang_wind.destroy()
            update_selection_label()
            career_app.deiconify()


    next_button = ttk.Button(lang_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

    def back():
        career_app.deiconify()
        lang_wind.destroy()

    back_button = ttk.Button(lang_wind, text="Back", command=back)
    back_button.pack(pady=10)

# If the user does a humanities subject, this opens the window to choose the humanities subject(s)
def humanities():
    # Hides the main window
    career_app.withdraw()
    
    # Properties for the new window
    hum_wind = Toplevel(career_app)
    hum_wind.title("Humanities")
    hum_wind.geometry("400x400")
    hum_wind.configure(bg="#e6ffe6")

    hum_label = ttk.Label(hum_wind, text= "Select Humanities completed")
    hum_label.pack(pady=10)

    # Variables to store the user's selection
    anc_hist_var = tk.StringVar()
    mod_hist_var = tk.StringVar()
    hist_ext_var = tk.StringVar()
    business_var = tk.StringVar()
    eco_var = tk.StringVar()
    legal_var = tk.StringVar()
    geo_var = tk.StringVar()
    sor1_var = tk.StringVar()
    sor2_var = tk.StringVar()

    def empty():
        pass

    # Checkbuttons (multiple selection) since you can do more than one technology

    ancient_hist_check = ttk.Checkbutton(hum_wind, text="Ancient History", command=empty, variable=anc_hist_var, onvalue="Ancient Hist", offvalue="")
    ancient_hist_check.pack(anchor='w')

    modern_hist_check = ttk.Checkbutton(hum_wind, text="Modern History", command=empty, variable=mod_hist_var, onvalue="Modern Hist", offvalue="")
    modern_hist_check.pack(anchor='w')

    hist_ext_check = ttk.Checkbutton(hum_wind, text="History Extension", command=empty, variable=hist_ext_var, onvalue="History Ext", offvalue="")
    hist_ext_check.pack(anchor='w')

    business_studies_check = ttk.Checkbutton(hum_wind, text="Business Studies", command=empty, variable=business_var, onvalue="Business Studies", offvalue="")
    business_studies_check.pack(anchor='w')

    economics_check = ttk.Checkbutton(hum_wind, text="Economics", command=empty, variable=eco_var, onvalue="Economics", offvalue="")
    economics_check.pack(anchor='w')

    legal_studies_check = ttk.Checkbutton(hum_wind, text="Legal Studies", command=empty, variable=legal_var, onvalue="Legal Studies", offvalue="")
    legal_studies_check.pack(anchor='w')

    geography_check = ttk.Checkbutton(hum_wind, text="Geography", command=empty, variable=geo_var, onvalue="Geography", offvalue="")
    geography_check.pack(anchor='w')

    sor1_check = ttk.Checkbutton(hum_wind, text="Studies of Religion I", command=empty, variable=sor1_var, onvalue="SOR I", offvalue="")
    sor1_check.pack(anchor='w')

    sor2_check = ttk.Checkbutton(hum_wind, text="Studies of Religion II", command=empty, variable=sor2_var, onvalue="SOR II", offvalue="")
    sor2_check.pack(anchor='w')

    def submit():
       # These variables need to be global so they can be accessed outside of the function
        global user_selections
        global duplicates
        
        # Checks if a subject has already been selected
        duplicates = [subject for subject in [anc_hist_var.get(), mod_hist_var.get(), hist_ext_var.get(), business_var.get(), eco_var.get(), legal_var.get(), geo_var.get(), sor1_var.get(), sor2_var.get()] if subject in user_selections]
        if duplicates:
            message = "You have already selected these subject(s), would you like to remove them?"
            response = messagebox.askyesno("Duplicate Subjects", message)
            if response:
                # Remove the duplicate subjects from user_selections
                user_selections = [subject for subject in user_selections if subject not in duplicates]
                hum_wind.destroy()
                update_selection_label()
                career_app.deiconify()
            else:
                return
        else:
            user_selections.extend([
                anc_hist_var.get() if anc_hist_var.get() else "",
                mod_hist_var.get() if mod_hist_var.get() else "",
                hist_ext_var.get() if hist_ext_var.get() else "",
                business_var.get() if business_var.get() else "",
                eco_var.get() if eco_var.get() else "",
                legal_var.get() if legal_var.get() else "",
                geo_var.get() if geo_var.get() else "",
                sor1_var.get() if sor1_var.get() else "",
                sor2_var.get() if sor2_var.get() else ""
            ])
            hum_wind.destroy()
            update_selection_label()
            career_app.deiconify()


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
    misc_wind.configure(bg="#e6ffe6")

    misc_label = ttk.Label(misc_wind, text= "Select Technologies completed")
    misc_label.pack(pady=10)

    pdhpe_var = tk.StringVar()
    drama_var = tk.StringVar()
    music1_var = tk.StringVar()
    music2_var = tk.StringVar()
    visual_arts_var = tk.StringVar()

    def empty():
        pass

    # Checkbuttons (multiple selection) since you can do more than one technology

    pdhpe_check = ttk.Checkbutton(misc_wind, text="PDHPE", command=empty, variable=pdhpe_var, onvalue="PDHPE", offvalue="")
    pdhpe_check.pack(anchor='w')

    drama_check = ttk.Checkbutton(misc_wind, text="Drama", command=empty, variable=drama_var, onvalue="Drama", offvalue="")
    drama_check.pack(anchor='w')

    music1_check = ttk.Checkbutton(misc_wind, text="Music 1", command=empty, variable=music1_var, onvalue="Music 1", offvalue="")
    music1_check.pack(anchor='w')

    music2_check = ttk.Checkbutton(misc_wind, text="Music 2", command=empty, variable=music2_var, onvalue="Music 2", offvalue="")
    music2_check.pack(anchor='w')

    visual_arts_check = ttk.Checkbutton(misc_wind, text="Visual Arts", command=empty, variable=visual_arts_var, onvalue="Visual Arts")
    visual_arts_check.pack(anchor='w')

    def submit():
        # These variables need to be global so they can be accessed outside of the function
        global user_selections
        global duplicates
        
        # Checks if a subject has already been selected
        duplicates = [subject for subject in [pdhpe_var.get(), drama_var.get(), music1_var.get(), music2_var.get(), visual_arts_var.get()] if subject in user_selections]
        if duplicates:
            message = "You have already selected these subject(s), would you like to remove them?"
            response = messagebox.askyesno("Duplicate Subjects", message)
            if response:
                user_selections = [subject for subject in user_selections if subject not in duplicates]
                misc_wind.destroy()
                update_selection_label()
                career_app.deiconify()
            else:
                return
        else:
            user_selections.extend([
                pdhpe_var.get() if pdhpe_var.get() else "",
                drama_var.get() if drama_var.get() else "",
                music1_var.get() if music1_var.get() else "",
                music2_var.get() if music2_var.get() else "",
                visual_arts_var.get() if visual_arts_var.get() else ""
            ])
            misc_wind.destroy()
            update_selection_label()
            career_app.deiconify()

    next_button = ttk.Button(misc_wind, text="Submit", command=submit)
    next_button.pack(pady=10)

    def back():
        career_app.deiconify()
        misc_wind.destroy()

    back_button = ttk.Button(misc_wind, text="Back", command=back)
    back_button.pack(pady=10)

# Test function to automatically select subjects, uncomment the test button in the main window to use (uses my subjects as an example)
def test():
    user_selections.append("Mathematics Advanced")
    user_selections.append("English Advanced")
    user_selections.append("Biology")
    user_selections.append("Chemistry")
    user_selections.append("Software Design and Development")
    update_selection_label()

title_label = ttk.Label(career_app, text="Welcome to the Career Advisor App", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

info_label = ttk.Label(career_app, text="Please select the subjects you have completed in the HSC.")
info_label.pack(pady=10)

info_label2 = ttk.Label(career_app, text="To remove a subject, select it again in that respective screen.")
info_label2.pack(pady=10)

# Uncomment the following lines to test show the test button

#test_btn = ttk.Button(career_app, text="Test", command=test)
#test_btn.pack(pady=10)

# English button. Opens english() (same for all the selection variables)
english_selection = ttk.Button(career_app, text= "English", command=english, width = 30)
english_selection.pack(pady=1)

maths_selection = ttk.Button(career_app, text= "Mathematics", command=maths, width = 30)
maths_selection.pack(pady=2)

science_selection = ttk.Button(career_app, text= "Sciences", command=science, width = 30)
science_selection.pack(pady=3)

tech_selection = ttk.Button(career_app, text= "Technological and Applied Studies", command=technology, width = 30)
tech_selection.pack(pady=4)

language_selection = ttk.Button(career_app, text= "Languages", command=language, width = 30)
language_selection.pack(pady=5)

humanities_selection = ttk.Button(career_app, text= "Humanities", command=humanities, width = 30)
humanities_selection.pack(pady=6)

misc_selection = ttk.Button(career_app, text= "Miscellaneous", command=misc, width = 30)
misc_selection.pack(pady=7)

selection_label = ttk.Label(career_app, text="You've Selected: ", wraplength=300, justify="left")
selection_label.pack(pady= 8)

# Opens the ranking window so the user can determine the rank of their subject based off enjoyment
def ranking():
    # Check if the user has selected at least three subjects
    if len(user_selections) <= 3:
        messagebox.showerror("Error", "You must have at least three HSC subjects")
        return
    # Check if the user has selected an English subject
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
        rank_win.configure(bg="#e6ffe6")

        rank_main_label = ttk.Label(rank_win, text= "Please fill out the following fields")
        rank_main_label.pack(pady=1)

        # Filter out empty strings
        filtered_selections = []
        for selection in user_selections:
            if selection:
                filtered_selections.append(selection)

        # Dropdown lists so user can select favourite subject, least favourite subject, and best performing subject
        favourite_var = StringVar()
        favourite_label = ttk.Label(rank_win, text="Select your favourite subject (enjoyment)")
        favourite_label.pack(pady=2)
        favourite_combo = ttk.Combobox(rank_win, textvariable=favourite_var, values=filtered_selections)
        favourite_combo.pack(pady=2)
        favourite_combo.state(['readonly'])

        least_favourite_var = StringVar()
        least_favourite_label = ttk.Label(rank_win, text="Select your least favourite subject")
        least_favourite_label.pack(pady=2)
        least_favourite_combo = ttk.Combobox(rank_win, textvariable=least_favourite_var, values=filtered_selections)
        least_favourite_combo.pack(pady=2)
        least_favourite_combo.state(['readonly'])

        performance_var = StringVar()
        performance_label = ttk.Label(rank_win, text="Select the subject where you recieve the best marks")
        performance_label.pack(pady=2)
        performance_combo = ttk.Combobox(rank_win, textvariable=performance_var, values=filtered_selections)
        performance_combo.pack(pady=2)
        performance_combo.state(['readonly'])

        # Dropdown list for the user to select their ideal university
        uni_list = ["University of Sydney", "University of New South Wales", "University of Technology Sydney", 
                    "Macquarie University", "University of Wollongong", "University of Newcastle", 
                    "University of New England", "Charles Sturt University", "Southern Cross University", 
                    "Australian Catholic University", "Western Sydney University", "University of Notre Dame Australia", 
                    "University of Canberra", "Australian National University", "La Trobe University",  
                    "Griffith University", "CQ University", "Torrens University Australia",
                    "Charles Darwin University"]


        university_selection_var = StringVar()
        university_selection_label = ttk.Label(rank_win, text="Select your ideal university")
        university_selection_label.pack(pady=2)
        university_selection_combo = ttk.Combobox(rank_win, textvariable=university_selection_var, values=uni_list)
        university_selection_combo.pack(pady=2)
        university_selection_combo.state(['readonly'])


        # Slider for projected/predicted ATAR
        number_slider = ttk.Scale(rank_win, from_=30, to=99.95, length=350, orient="horizontal")
        number_slider.pack(pady=10)
        
        # Label to display the user's projected ATAR
        number_label = ttk.Label(rank_win, text="Projected ATAR: ")
        number_label.pack(pady=5)
        
        # Function to update the label with the projected ATAR
        def update_ATAR_label():
            number_label.config(text="Selected Number: " + "{:.2f}".format(number_slider.get()))
        
        # Bind the slider's event to the update_number_label function
        number_slider.bind("<ButtonRelease-1>", lambda event: update_ATAR_label())


    # Function to process user's selections and display the results
    def results():
        # Detects if user hasn't chosen anything in the four dropdown lists and displays an error message
        if not favourite_var.get() or not least_favourite_var.get() or not performance_var.get() or not university_selection_var.get():
            messagebox.showerror("Error", "Please select a value for each dropdown list.")
            return
        
        # Detects if user hasn't selected a projected ATAR and displays an error message
        if not number_slider.get():
            messagebox.showerror("Error", "Please select a projected ATAR.")
            return
        
        # Initialize choice filters
        choice_filters = [favourite_var.get(), performance_var.get()]

        # Technically doesn't matter what language the user does, so replace favourite_var.get() as "Languages"
        if "Chinese Beginners" or "Chinese Continuers" or "Japanese Beginners" or "Japanese Continuers" or "Italian Beginners" or "Italian Continuers" in favourite_var.get():
            choice_filters[0] = "Languages"

        # Replaces performance_var.get() with "Languages"
        if "Chinese Beginners" or "Chinese Continuers" or "Japanese Beginners" or "Japanese Continuers" or "Italian Beginners" or "Italian Continuers" in performance_var.get():
            choice_filters[1] = "Languages"
        
        # Read the data from the csv file (containing all the degrees, subjects, universities, etc.)
        df = pd.read_csv("degree_table.csv")

        # Splits the strings in the columns into lists
        df['Subjects'] = df['Relevant HSC Subjects'].str.split(', ')
        df['Universities'] = df['University'].str.split(', ')

        # Initial filtering by the selected university
        filtered_df = df[df['Universities'].apply(lambda x: university_selection_var.get() in x)]

        # Initial filtering by subjects, including least favourite subject, and LSR
        filtered_df = filtered_df[
            filtered_df['Subjects'].apply(lambda x: all(subject in x for subject in choice_filters) and least_favourite_var.get() in x)
            & (filtered_df['Prev LSR'] <= number_slider.get())
        ]

        # Check if the filtered list is empty
        if filtered_df.empty:
            # Remove the least favourite subject modifier from filtering
            filtered_df = df[
                df['Universities'].apply(lambda x: university_selection_var.get() in x)
                & df['Subjects'].apply(lambda x: all(subject in x for subject in choice_filters))
                & (df['Prev LSR'] <= number_slider.get())
            ]
            
            # Check again if the filtered list is empty after excluding the least favourite subject
            if filtered_df.empty:
                # Remove the best performing subject if it exists in choice_filters
                if performance_var.get() in choice_filters:
                    choice_filters.remove(performance_var.get())
                
                filtered_df = df[
                    df['Universities'].apply(lambda x: university_selection_var.get() in x)
                    & df['Subjects'].apply(lambda x: all(subject in x for subject in choice_filters))]
                
                # Check again if the filtered list is empty after excluding the best performing subject
                if filtered_df.empty:
                    messagebox.showerror("Error", "No degrees found with the given criteria.")
                    return


        # Close the ranking window and open the results window
        rank_win.destroy()
        result_win = Toplevel(career_app)
        result_win.title("Results")
        result_win.geometry("450x450")
        result_win.configure(bg="#e6ffe6")

        result_label = ttk.Label(result_win, text="Your Results!", font=("Helvetica", 16, "bold"))
        result_label.grid(column=0, row=0, sticky=(N,W,E,S))

        result_text = ScrolledText(result_win, width=10, height=40, wrap=tk.WORD)
        result_text.grid(column=0, row=1, sticky=(N,W,E,S))

        # Contains the degrees outputted
        list_box = Listbox(result_win, height=10, width=60)
        list_box.grid(column=0, row=1, sticky=(N,W,E,S))
        scroll = ttk.Scrollbar(result_win, orient=VERTICAL, command=list_box.yview)
        scroll.grid(column=1, row=1, sticky=(N,S))
        list_box['yscrollcommand'] = scroll.set
        
        for index, row in filtered_df.iterrows():
            list_box.insert('end', f"{row['Course name']}\n")


    submit_button = ttk.Button(rank_win, text="Submit Rankings", command=results)
    submit_button.pack(pady=10)

# Button to open ranking window
start_btn = ttk.Button(career_app, text= "Start", command=ranking, width = 30)
start_btn.pack(pady=10)

# Runs program!
career_app.mainloop()