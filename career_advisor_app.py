import tkinter as tk
from tkinter import ttk

career_app = tk.Tk()
career_app.title("Career Advisor App")
career_app.geometry("400x400")


# Established initial window to select level of English completed at school

english_label = ttk.Label(career_app, text= "Select level of English completed")
english_label.pack(pady=10)

eng_var = tk.StringVar()

# Radiobuttons (singular selection) since you can't do more than one kind of English
# Started with English because all students in NSW must do it

eng_radio1 = ttk.Radiobutton(career_app, text="English Standard", variable=eng_var, value="English Standard")
eng_radio1.pack(anchor='w')

eng_radio2 = ttk.Radiobutton(career_app, text="English Advanced", variable=eng_var, value="English Advanced")
eng_radio2.pack(anchor='w')

eng_radio3 = ttk.Radiobutton(career_app, text="English Ext 1", variable=eng_var, value="English Ext 1")
eng_radio3.pack(anchor='w')

eng_radio4 = ttk.Radiobutton(career_app, text="English Ext 2", variable=eng_var, value="Englush Ext 2")
eng_radio4.pack(anchor='w')

# "Next" button will close current window and open new window (TBC)
def close_window():
    career_app.destroy()


next_button = ttk.Button(career_app, text="Next", command=close_window)
next_button.pack(pady=10)

career_app.mainloop()