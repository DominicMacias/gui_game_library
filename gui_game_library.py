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
class Main_Menu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.lbl_title = tk.Label(self, text = "Game Library", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, pady = 20)
        
        self.btn_add = tk.Button(self, text = " Add Game ", command = self.raise_add, font = NON_TITLE_FONT)
        self.btn_add.grid(row = 1, column = 0)
        
        self.btn_edit = tk.Button(self, text = "   Edit   ", command = self.raise_edit, font = NON_TITLE_FONT)
        self.btn_edit.grid(row = 2, column = 0)
        
        self.btn_search = tk.Button(self, text = "  Search  ", command = self.raise_search, font = NON_TITLE_FONT)
        self.btn_search.grid(row = 3, column = 0)
        
        self.btn_remove = tk.Button(self, text = "  Remove  ", font = NON_TITLE_FONT)
        self.btn_remove.grid(row = 4, column = 0)
        
        self.btn_save = tk.Button(self, text = "   Save   ", command = self.save, font = NON_TITLE_FONT)
        self.btn_save.grid(row = 5, column = 0)
    
    def raise_add(self):
        frame_add_or_edit.tkraise()
    
    def raise_edit(self):
        print("raising edit")
    
    def raise_search(self):
        frame_search.tkraise()
    
    def save(self):
        messagebox.showinfo("Save", "File Saved")
    


class Add_Or_edit(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
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
        
        self.dpdn_gamemodes = tk.OptionMenu(self, self.tkvar, *gamemodes)
        self.dpdn_gamemodes.grid(row = 4, column = 3, sticky = "news")
        
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
        
        self.scl_notes = ScrolledText(self, width = 40, height = 8)
        self.scl_notes.grid(row = 8, column = 0, columnspan = 4)
        
        #Buttons to cancel adding/editing, reset the changes, or to confirm changes
        frame_add_or_edit_buttons = Add_Or_Edit_Buttons(self)
        frame_add_or_edit_buttons.grid(row = 9, column = 0, columnspan = 4, sticky = "news")
        
        
class Add_Or_Edit_Buttons(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.btn_cancel = tk.Button(self, text = "Cancel", command = self.cancel, font = NON_TITLE_FONT)
        self.btn_cancel.grid(row = 0, column = 0)
        
        self.btn_reset = tk.Button(self, text = "Reset", font = NON_TITLE_FONT)
        self.btn_reset.grid(row = 0, column = 1, padx = 50)
        
        self.btn_confirm = tk.Button(self, text = "Confirm", font = NON_TITLE_FONT)
        self.btn_confirm.grid(row = 0, column = 2)
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
    
    def cancel(self):
        frame_menu.tkraise()


class Search(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        #Setup for the "Search By:" drop-down menu
        options = ["Genre", "Title", "Developer", "Publisher", "Platform", "Release Date",
                   "Rating", "Gamemode(s)", "Price (USD)", "Completion", "Purchase Date",
                   "Notes"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        #Search Parameters
        self.lbl_title = tk.Label(self, text = "Search", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, columnspan = 5, pady = 20)
        
        self.lbl_search_by = tk.Label(self, text = "Search By:", font = NON_TITLE_FONT)
        self.lbl_search_by.grid(row = 1, column = 0)
        
        self.dpdn_search_by = tk.OptionMenu(self, self.tkvar, *options)
        self.dpdn_search_by.grid(row = 2, column = 0, sticky = "news")
        
        self.lbl_search_for = tk.Label(self, text = "Search For:", font = NON_TITLE_FONT)
        self.lbl_search_for.grid(row = 3, column = 0)
        
        self.ent_search_for = tk.Entry(self, font = NON_TITLE_FONT)
        self.ent_search_for.grid(row = 4, column = 0)
        
        #Check boxes for printing specific catergories
        self.chk_search_filter = Search_Parameters(self)
        self.chk_search_filter.grid(row = 1, column = 1, rowspan = 4)
        
        #Scrolled Text Box that shows results
        self.scl_results = ScrolledText(self, width = 40, height = 8)
        self.scl_results.grid(row = 5, column = 0, columnspan = 5)
        
        #Buttons to leave the frame, do the search action, or clear the results
        frame_search_buttons = Search_Buttons(self)
        frame_search_buttons.grid(row = 6, column = 0, columnspan = 2, sticky="news")

class Search_Buttons(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.btn_back = tk.Button(self, text = "Back", command = self.go_back, font = NON_TITLE_FONT)
        self.btn_back.grid(row = 0, column = 0)
        
        self.btn_back = tk.Button(self, text = "Clear", font = NON_TITLE_FONT)
        self.btn_back.grid(row = 0, column = 1, padx = 50)
        
        self.btn_back = tk.Button(self, text = "Submit", font = NON_TITLE_FONT)
        self.btn_back.grid(row = 0, column = 2)
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        
    def go_back(self):
        frame_menu.tkraise()

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


#Global Functions
global games

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
    #Loads Window
    root = tk.Tk()
    root.title("Game Library")
    
    #Initializes the frames
    frame_menu = Main_Menu()
    frame_menu.grid(row = 0, column = 0, sticky = "news")
    
    frame_add_or_edit = Add_Or_edit()
    frame_add_or_edit.grid(row = 0, column = 0, sticky = "news")
    
    frame_search = Search()
    frame_search.grid(row = 0, column = 0, sticky = "news")
    
    frame_menu.tkraise()
    frame_add_or_edit.tkraise()
    root.mainloop()