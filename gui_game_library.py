#!/usr/bin/python3
# Dominic Macias
# 2/10/2020

"""Creates a user-friendly interface version of the game_libary program"""

#Imports
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import pickle as p
import dictionary_reset

#Constants
TITLE_FONT = ("Times New Roman", 30)
NON_TITLE_FONT = ("Courier", 15)

#Classes
class Screen(tk.Frame):
    current = 0
    
    def __init__(self):
        tk.Frame.__init__(self)
        
    def switch_frame():
        screens[Screen.current].tkraise()


class MainMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.lbl_title = tk.Label(self, text = "Game Library", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, pady = 20)
        
        self.btn_add = tk.Button(self, text = " Add Game ", command = self.raise_add, font = NON_TITLE_FONT)
        self.btn_add.grid(row = 1, column = 0)
        
        self.btn_edit = tk.Button(self, text = "   Edit   ", command = self.raise_edit, font = NON_TITLE_FONT)
        self.btn_edit.grid(row = 2, column = 0)
        
        self.btn_search = tk.Button(self, text = "  Search  ", command = self.raise_search, font = NON_TITLE_FONT)
        self.btn_search.grid(row = 3, column = 0)
        
        self.btn_remove = tk.Button(self, text = "  Remove  ", command = self.raise_remove, font = NON_TITLE_FONT)
        self.btn_remove.grid(row = 4, column = 0)
        
        self.btn_save = tk.Button(self, text = "   Save   ", command = self.save, font = NON_TITLE_FONT)
        self.btn_save.grid(row = 5, column = 0)
    
    def raise_add(self):
        Screen.current = 1
        Screen.switch_frame()
    
    def raise_edit(self):
        pop_up = tk.Tk()
        pop_up.title("Edit")
        frm_edit = EditSelect(pop_up)
        frm_edit.grid(row = 0, column = 0)
    
    def raise_search(self):
        Screen.current = 2
        Screen.switch_frame()
        
    def raise_remove(self):
        pop_up = tk.Tk()
        pop_up.title("Remove")
        frm_remove = Remove(pop_up)
        frm_remove.grid(row = 0, column = 0)
    
    def save(self):
        messagebox.showinfo("Save", "File Saved")
    


class Add(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.lbl_title = tk.Label(self, text = "  Add Game  ", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, columnspan = 4, pady = 20)
        
        self.lbl_genre = tk.Label(self, text = "Genre:", font = NON_TITLE_FONT)
        self.lbl_genre.grid(row = 1, column = 0)
        
        self.ent_genre = tk.Entry(self, font = NON_TITLE_FONT, bd = 3)
        self.ent_genre.grid(row = 1, column = 1)
        
        self.lbl_title = tk.Label(self, text = "Title:", font = NON_TITLE_FONT)
        self.lbl_title.grid(row = 1, column = 2)
        
        self.ent_title = tk.Entry(self, font = NON_TITLE_FONT, bd = 3)
        self.ent_title.grid(row = 1, column = 3)
        
        self.lbl_developer = tk.Label(self, text = "Developer:", font = NON_TITLE_FONT)
        self.lbl_developer.grid(row = 2, column = 0)
        
        self.ent_developer = tk.Entry(self, font = NON_TITLE_FONT, bd = 3)
        self.ent_developer.grid(row = 2, column = 1)
        
        self.lbl_publisher = tk.Label(self, text = "Publisher:", font = NON_TITLE_FONT)
        self.lbl_publisher.grid(row = 2, column = 2)
        
        self.ent_publisher = tk.Entry(self, font = NON_TITLE_FONT, bd = 3)
        self.ent_publisher.grid(row = 2, column = 3)
        
        self.lbl_platform = tk.Label(self, text = "Platform:", font = NON_TITLE_FONT)
        self.lbl_platform.grid(row = 3, column = 0)
        
        self.ent_platform = tk.Entry(self, font = NON_TITLE_FONT, bd = 3)
        self.ent_platform.grid(row = 3, column = 1)
        
        self.lbl_release_date = tk.Label(self, text = "Release Date:", font = NON_TITLE_FONT)
        self.lbl_release_date.grid(row = 3, column = 2)
        
        self.ent_release_date = tk.Entry(self, font = NON_TITLE_FONT, bd = 3)
        self.ent_release_date.grid(row = 3, column = 3)
        
        self.lbl_rating = tk.Label(self, text = "Rating:", font = NON_TITLE_FONT)
        self.lbl_rating.grid(row = 4, column = 0)
        
        self.ent_rating = tk.Entry(self, font = NON_TITLE_FONT, bd = 3)
        self.ent_rating.grid(row = 4, column = 1)
        
        #Setup for the "gamemode(s)" drop-down menu
        gamemodes = ["Single", "Multi", "Either"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(gamemodes[0])        
        
        self.lbl_gamemodes = tk.Label(self, text = "Gamemode(s):", font = NON_TITLE_FONT)
        self.lbl_gamemodes.grid(row = 4, column = 2)
        
        self.dbx_gamemodes = tk.OptionMenu(self, self.tkvar, *gamemodes)
        self.dbx_gamemodes.grid(row = 4, column = 3, sticky = "news")
        
        self.lbl_price = tk.Label(self, text = "Price (USD):", font = NON_TITLE_FONT)
        self.lbl_price.grid(row = 5, column = 0)
        
        self.ent_price = tk.Entry(self, font = NON_TITLE_FONT, bd = 3)
        self.ent_price.grid(row = 5, column = 1)
        
        self.lbl_purchase_date = tk.Label(self, text = "Purchase Date:", font = NON_TITLE_FONT)
        self.lbl_purchase_date.grid(row = 5, column = 2)
        
        self.ent_purchase_date = tk.Entry(self, font = NON_TITLE_FONT, bd = 3)
        self.ent_purchase_date.grid(row = 5, column = 3)
        
        self.chk_completed = tk.Checkbutton(self, text = "Completed?", font = NON_TITLE_FONT)
        self.chk_completed.grid(row = 6, column = 0, columnspan = 4, sticky = "news")
        
        self.lbl_notes = tk.Label(self, text = "Notes:", font = NON_TITLE_FONT)
        self.lbl_notes.grid(row = 7, column = 0,  columnspan = 4, sticky = "news")
        
        self.scr_notes = ScrolledText(self, width = 40, height = 8)
        self.scr_notes.grid(row = 8, column = 0, columnspan = 4)
        
        #Buttons to cancel adding/editing, reset the changes, or to confirm changes
        frm_add_or_edit_buttons = Add_Buttons(self)
        frm_add_or_edit_buttons.grid(row = 9, column = 0, columnspan = 4, sticky = "news")

class Add_Buttons(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.btn_cancel = tk.Button(self, text = "Cancel", command = self.cancel, font = NON_TITLE_FONT)
        self.btn_cancel.grid(row = 0, column = 0)
        
        self.btn_reset = tk.Button(self, text = "Reset", font = NON_TITLE_FONT)
        self.btn_reset.grid(row = 0, column = 1, padx = 50)
        
        self.btn_confirm = tk.Button(self, text = "Confirm", command = self.confirm, font = NON_TITLE_FONT)
        self.btn_confirm.grid(row = 0, column = 2)
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
    
    def cancel(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def confirm(self):
        Screen.current = 0
        Screen.switch_frame()


class Edit(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.lbl_title = tk.Label(self, text = "  Edit Game  ", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, columnspan = 4, pady = 20)
        
        self.lbl_genre = tk.Label(self, text = "Genre:", font = NON_TITLE_FONT)
        self.lbl_genre.grid(row = 1, column = 0)
        
        self.ent_genre = tk.Entry(self, font = NON_TITLE_FONT, bd = 3)
        self.ent_genre.grid(row = 1, column = 1)
        
        self.lbl_title = tk.Label(self, text = "Title:", font = NON_TITLE_FONT)
        self.lbl_title.grid(row = 1, column = 2)
        
        self.ent_title = tk.Entry(self, font = NON_TITLE_FONT, bd = 3)
        self.ent_title.grid(row = 1, column = 3)
        
        self.lbl_developer = tk.Label(self, text = "Developer:", font = NON_TITLE_FONT)
        self.lbl_developer.grid(row = 2, column = 0)
        
        self.ent_developer = tk.Entry(self, font = NON_TITLE_FONT, bd = 3)
        self.ent_developer.grid(row = 2, column = 1)
        
        self.lbl_publisher = tk.Label(self, text = "Publisher:", font = NON_TITLE_FONT)
        self.lbl_publisher.grid(row = 2, column = 2)
        
        self.ent_publisher = tk.Entry(self, font = NON_TITLE_FONT, bd = 3)
        self.ent_publisher.grid(row = 2, column = 3)
        
        self.lbl_platform = tk.Label(self, text = "Platform:", font = NON_TITLE_FONT)
        self.lbl_platform.grid(row = 3, column = 0)
        
        self.ent_platform = tk.Entry(self, font = NON_TITLE_FONT, bd = 3)
        self.ent_platform.grid(row = 3, column = 1)
        
        self.lbl_release_date = tk.Label(self, text = "Release Date:", font = NON_TITLE_FONT)
        self.lbl_release_date.grid(row = 3, column = 2)
        
        self.ent_release_date = tk.Entry(self, font = NON_TITLE_FONT, bd = 3)
        self.ent_release_date.grid(row = 3, column = 3)
        
        self.lbl_rating = tk.Label(self, text = "Rating:", font = NON_TITLE_FONT)
        self.lbl_rating.grid(row = 4, column = 0)
        
        self.ent_rating = tk.Entry(self, font = NON_TITLE_FONT, bd = 3)
        self.ent_rating.grid(row = 4, column = 1)
        
        #Setup for the "gamemode(s)" drop-down menu
        gamemodes = ["Single", "Multi", "Either"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(gamemodes[0])        
        
        self.lbl_gamemodes = tk.Label(self, text = "Gamemode(s):", font = NON_TITLE_FONT)
        self.lbl_gamemodes.grid(row = 4, column = 2)
        
        self.dbx_gamemodes = tk.OptionMenu(self, self.tkvar, *gamemodes)
        self.dbx_gamemodes.grid(row = 4, column = 3, sticky = "news")
        
        self.lbl_price = tk.Label(self, text = "Price (USD):", font = NON_TITLE_FONT)
        self.lbl_price.grid(row = 5, column = 0)
        
        self.ent_price = tk.Entry(self, font = NON_TITLE_FONT, bd = 3)
        self.ent_price.grid(row = 5, column = 1)
        
        self.lbl_purchase_date = tk.Label(self, text = "Purchase Date:", font = NON_TITLE_FONT)
        self.lbl_purchase_date.grid(row = 5, column = 2)
        
        self.ent_purchase_date = tk.Entry(self, font = NON_TITLE_FONT, bd = 3)
        self.ent_purchase_date.grid(row = 5, column = 3)
        
        self.chk_completed = tk.Checkbutton(self, text = "Completed?", font = NON_TITLE_FONT)
        self.chk_completed.grid(row = 6, column = 0, columnspan = 4, sticky = "news")
        
        self.lbl_notes = tk.Label(self, text = "Notes:", font = NON_TITLE_FONT)
        self.lbl_notes.grid(row = 7, column = 0,  columnspan = 4, sticky = "news")
        
        self.scr_notes = ScrolledText(self, width = 40, height = 8)
        self.scr_notes.grid(row = 8, column = 0, columnspan = 4)
        
        #Buttons to cancel adding/editing, reset the changes, or to confirm changes
        frm_add_or_edit_buttons = Edit_Buttons(self)
        frm_add_or_edit_buttons.grid(row = 9, column = 0, columnspan = 4, sticky = "news")

class Edit_Buttons(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.btn_cancel = tk.Button(self, text = "Cancel", command = self.cancel, font = NON_TITLE_FONT)
        self.btn_cancel.grid(row = 0, column = 0)
        
        self.btn_reset = tk.Button(self, text = "Reset", font = NON_TITLE_FONT)
        self.btn_reset.grid(row = 0, column = 1, padx = 50)
        
        self.btn_confirm = tk.Button(self, text = "Confirm", command = self.confirm, font = NON_TITLE_FONT)
        self.btn_confirm.grid(row = 0, column = 2)
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
    
    def cancel(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def confirm(self):
        Screen.current = 0
        Screen.switch_frame()

class EditSelect(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        
        self.lbl_which_title = tk.Label(self, text = "Which Title would you like to edit?", font = TITLE_FONT)
        self.lbl_which_title.grid(row = 0, column = 0, columnspan = 2, sticky = "news")
        
        titles = ["Title1", "Title2"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(titles[0])
        
        self.dbx_titles = tk.OptionMenu(self, self.tkvar, *titles)
        self.dbx_titles.grid(row = 1, column = 0, columnspan = 2, pady = 50, sticky = "news")
        
        self.btn_cancel = tk.Button(self, text = "Cancel", command = self.cancel, font = NON_TITLE_FONT)
        self.btn_cancel.grid(row = 2, column = 0, sticky = "news")
        
        self.btn_confirm = tk.Button(self, text = "Confirm", command = self.confirm, font = NON_TITLE_FONT)
        self.btn_confirm.grid(row = 2, column = 1, sticky = "news")
        
    def cancel(self):
        self.parent.destroy()
        
    def confirm(self):
        Screen.current = 2
        Screen.switch_frame()
        self.parent.destroy()

class Search(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        #Setup for the "Search By:" drop-down menu
        options = ["Genre", "Title", "Developer", "Publisher", "Platform", "Release Date",
                   "Rating", "Gamemode(s)", "Price (USD)", "Completion", "Purchase Date",
                   "Notes"]
        self.tk_search_by = tk.StringVar(self)
        self.tk_search_by.set(options[0])
        
        #Search Parameters
        self.lbl_title = tk.Label(self, text = "Search", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, columnspan = 5, pady = 20)
        
        self.lbl_search_by = tk.Label(self, text = "Search By:", font = NON_TITLE_FONT)
        self.lbl_search_by.grid(row = 1, column = 0)
        
        self.dbx_search_by = tk.OptionMenu(self, self.tk_search_by, *options)
        self.dbx_search_by.grid(row = 2, column = 0, sticky = "news")
        
        self.lbl_search_for = tk.Label(self, text = "Search For:", font = NON_TITLE_FONT)
        self.lbl_search_for.grid(row = 3, column = 0)
        
        self.ent_search_for = tk.Entry(self, font = NON_TITLE_FONT)
        #Screen.current = 2grid(row = 4, column = 0)
        
        #Check boxes for printing specific catergories
        self.chk_search_filter = Search_Parameters(self)
        self.chk_search_filter.grid(row = 1, column = 1, rowspan = 4)
        
        #Scrolled Text Box that shows results
        self.scr_results = ScrolledText(self, width = 40, height = 8)
        self.scr_results.grid(row = 5, column = 0, columnspan = 5)
        
        #Buttons to leave the frame, do the search action, or clear the results
        frm_search_buttons = Search_Buttons(self)
        frm_search_buttons.grid(row = 6, column = 0, columnspan = 2, sticky="news")

class Search_Buttons(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.btn_back = tk.Button(self, text = "Back", command = self.go_back, font = NON_TITLE_FONT)
        self.btn_back.grid(row = 0, column = 0)
        
        self.btn_back = tk.Button(self, text = "Clear", font = NON_TITLE_FONT)
        self.btn_back.grid(row = 0, column = 1, padx = 50)
        
        self.btn_back = tk.Button(self, text = "Submit", command = self.submit, font = NON_TITLE_FONT)
        self.btn_back.grid(row = 0, column = 2)
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        
    def go_back(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def submit(self):
        Screen.current = 0
        Screen.switch_frame()    

class Search_Parameters(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        
        #Choice to print specified catergories
        self.lbl_print_filter = tk.Label(self, text = "Print Filter:", font = NON_TITLE_FONT)
        self.lbl_print_filter.grid(row = 0, column = 2, columnspan = 3, sticky = "news")
        
        self.chk_genre = tk.Checkbutton(self, text = "Genre", font = NON_TITLE_FONT)
        self.chk_genre.grid(row = 1, column = 2, sticky = "nsw")
        
        self.chk_title = tk.Checkbutton(self, text = "Title", font = NON_TITLE_FONT)
        self.chk_title.grid(row = 1, column = 3, sticky = "nsw")
        
        self.chk_developer = tk.Checkbutton(self, text = "Developer", font = NON_TITLE_FONT)
        self.chk_developer.grid(row = 1, column = 4, sticky = "nsw")
        
        self.chk_genre = tk.Checkbutton(self, text = "Publisher", font = NON_TITLE_FONT)
        self.chk_genre.grid(row = 2, column = 2, sticky = "nsw")
        
        self.chk_title = tk.Checkbutton(self, text = "Platform", font = NON_TITLE_FONT)
        self.chk_title.grid(row = 2, column = 3, sticky = "nsw")
        
        self.chk_developer = tk.Checkbutton(self, text = "Release Date", font = NON_TITLE_FONT)
        self.chk_developer.grid(row = 2, column = 4, sticky = "nsw")

        self.chk_genre = tk.Checkbutton(self, text = "Rating", font = NON_TITLE_FONT)
        self.chk_genre.grid(row = 3, column = 2, sticky = "nsw")
        
        self.chk_title = tk.Checkbutton(self, text = "Gamemode(s)", font = NON_TITLE_FONT)
        self.chk_title.grid(row = 3, column = 3, sticky = "nsw")
        
        self.chk_developer = tk.Checkbutton(self, text = "Price (USD)", font = NON_TITLE_FONT)
        self.chk_developer.grid(row = 3, column = 4, sticky = "nsw")

        self.chk_genre = tk.Checkbutton(self, text = "Completed?", font = NON_TITLE_FONT)
        self.chk_genre.grid(row = 4, column = 2, sticky = "nsw")
        
        self.chk_title = tk.Checkbutton(self, text = "Purchase Date", font = NON_TITLE_FONT)
        self.chk_title.grid(row = 4, column = 3, sticky = "nsw")
        
        self.chk_developer = tk.Checkbutton(self, text = "Notes", font = NON_TITLE_FONT)
        self.chk_developer.grid(row = 4, column = 4, sticky = "nsw")

class Remove(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        
        self.lbl_which_title = tk.Label(self, text = "Which Title would you like to remove?", font = TITLE_FONT)
        self.lbl_which_title.grid(row = 0, column = 0, columnspan = 2, sticky = "news")
        
        titles = ["Title1", "Title2"]
        self.tk_which_title = tk.StringVar(self)
        self.tk_which_title.set(titles[0])
        
        self.dbx_titles = tk.OptionMenu(self, self.tk_which_title, *titles)
        self.dbx_titles.grid(row = 1, column = 0, columnspan = 2, pady = 50, sticky = "news")
        
        self.btn_cancel = tk.Button(self, text = "Cancel", command = self.cancel, font = NON_TITLE_FONT)
        self.btn_cancel.grid(row = 2, column = 0, sticky = "news")
        
        self.btn_remove = tk.Button(self, text = "Confirm", command = self.remove, font = NON_TITLE_FONT)
        self.btn_remove.grid(row = 2, column = 1, sticky = "news")
        
    def cancel(self):
        self.parent.destroy()
        
    def remove(self):
        messagebox.showinfo("Remove", "Title Removed")
        self.parent.destroy()
        Screen.current = 0
        Screen.switch_frame()

#Main Function
if __name__ == "__main__":
    #File Loader
    try:
        datafile = open("game_lib.pickle", "rb")
        games = p.load(datafile)
        datafile.close()
    except:
        #Placeholder of info in case of missing pickle file
        dictionary_reset.Reset

    #Loads Main Window
    root = tk.Tk()
    root.title("Game Library")
    
    #Initializes the frames 
    screens = [MainMenu(), Add(), Edit(), Search()]
    screens[0].grid(row=0,column=0,sticky="news")
    screens[1].grid(row=0,column=0,sticky="news")
    screens[2].grid(row=0,column=0,sticky="news")
    screens[3].grid(row=0,column=0,sticky="news")

    screens[0].tkraise()
    root.mainloop()