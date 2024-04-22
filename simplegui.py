import csv
from pyexpat.errors import XML_ERROR_UNCLOSED_CDATA_SECTION
import tools

import tkinter as tk
from tkinter import ttk

from pandastable import Table, TableModel

from backend import  Database
from tkinter import *
database = Database("books.db")
LARGEFONT =("Verdana", 35)

view_definition_query = ""
filtration_query = ""

class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage, Page1, Page2):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# first window frame startpage

class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		
		# label of frame Layout 2
		label = ttk.Label(self, text ="DM project", font = LARGEFONT)
		
		# putting the grid in its place by using
		# grid
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		button1 = ttk.Button(self, text ="Create View",
		command = lambda : controller.show_frame(Page1))
	
		# putting the button in its place by
		# using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		## button to show frame 2 with text layout2
		button2 = ttk.Button(self, text ="Query View",
		command = lambda : controller.show_frame(Page2))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)

		


# second window frame page1
class Page1(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Create View", font = LARGEFONT)
		label.grid(row = 0, column = 2, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="HOME",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place
		# by using grid
		button1.grid(row = 1, column = 0, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button2 = ttk.Button(self, text ="Query View",
							command = lambda : controller.show_frame(Page2))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 1, column = 1, padx = 10, pady = 10)
		l1 =ttk.Label(self, text="Type View Def:")
		l1.grid(row = 3, column = 0, padx = 10, pady = 10)

		self.command = StringVar()
		e1 = ttk.Entry(self, textvariable=self.command)
		e1.grid(row = 3, column = 1, padx = 10, pady = 10)
		button3 = ttk.Button(self, text ="Submit",
							command = lambda : self.workOnInput(self.command, controller))

	
		# putting the button in its place by
		# using grid
		button3.grid(row = 3, column = 2, padx = 10, pady = 10)		
		#print(command.get())
	def workOnInput(self, command, controller):

		view_definition_query = command.get()
		print(view_definition_query)
		controller.show_frame(TablePage)

		
class TablePage(tk.Frame):
	def __init__(self, parent = None):
		tk.Frame.__init__(self, parent)
		self.parent = parent
		self.main = self.master
		self.main.geometry('600x400+200+100')
		self.main.title('Table Page')
		f = tk.Frame(self.main)
		columns = tools.parsing(view_definition_query)
		tools.generateDataFrames(columns, tools.rdbms, tools.csvinfo, view_definition_query)
		df = tools.getView(view_definition_query.split()[2])
		self.table = pt = Table(f, dataframe=df, showtoolbar=True, showstatusbar=True)


		pt.show()
	
		
		
		





# third window frame page2
class Page2(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Query View", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)
		l1 =ttk.Label(self, text="Cust_Id")
		l1.grid(row=0, column=0)

		l2 = ttk.Label(self, text="Sales")
		l2.grid(row=0, column=2)

		l3 =ttk.Label(self, text="Profit")
		l3.grid(row=1, column=0)

		l4 = ttk.Label(self, text="Discount")
		l4.grid(row=1, column=2)
		title_text = StringVar()
		e1 = ttk.Entry(self, textvariable=title_text)
		e1.grid(row=0, column=1)

		author_text = StringVar()
		e2 = ttk.Entry(self, textvariable=author_text)
		e2.grid(row=0, column=3)

		year_text = StringVar()
		e3 = ttk.Entry(self, textvariable=year_text)
		e3.grid(row=1, column=1)

		ISBN_text = StringVar()
		e4= ttk.Entry(self, textvariable=ISBN_text)
		e4.grid(row=1, column=3)
		
		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="Create View",
							command = lambda : controller.show_frame(Page1))
	
		# putting the button in its place by
		# using grid
		button1.grid(row = 3, column = 1, padx = 10, pady = 10)

		# button to show frame 3 with text
		# layout3
		button2 = ttk.Button(self, text ="HOME",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 3, column = 2, padx = 10, pady = 10)


"""
database = Database("books.db")

class Page12(tk.Frame):
	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)
		l1 = Label(self, text="Title")
		l1.grid(row=0, column=0)

		l2 = Label(self, text="Author")
		l2.grid(row=0, column=2)

		l3 = Label(self, text="Year")
		l3.grid(row=1, column=0)

		l4 = Label(self, text="ISBN")
		l4.grid(row=1, column=2)
class Page4(tk.Frame):
#class Window(object):
    def __init__(self,parent,window):
        tk.Frame.__init__(self, parent)    
        #self.window = window
        #self.window.wm_title("The Book Store")

        l1 = Label(self, text="Title")
        l1.grid(row=0, column=0)

        l2 = Label(self, text="Author")
        l2.grid(row=0, column=2)

        l3 = Label(self, text="Year")
        l3.grid(row=1, column=0)

        l4 = Label(self, text="ISBN")
        l4.grid(row=1, column=2)

        self.title_text = StringVar()
        self.e1 = Entry(self, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        self.author_text = StringVar()
        self.e2 = Entry(self, textvariable=self.author_text)
        self.e2.grid(row=0, column=3)

        self.year_text = StringVar()
        self.e3 = Entry(self, textvariable=self.year_text)
        self.e3.grid(row=1, column=1)

        self.ISBN_text = StringVar()
        self.e4= Entry(self, textvariable=self.ISBN_text)
        self.e4.grid(row=1, column=3)

        self.list1 = Listbox(self, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        # now we need to attach a scrollbar to the listbox, and the other direction,too
        sb1 = Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)
        self.list1.config(yscrollcommand=sb1.set)
        sb1.config(command=self.list1.yview)

        b1 = Button(self, text="View all", width=12, command=self.view_command)
        b1.grid(row=2, column=3)

        b2 = Button(self, text="Search entry", width=12, command=self.search_command)
        b2.grid(row=3, column=3)

        b3 = Button(self, text="Add entry", width=12, command=self.add_command)
        b3.grid(row=4, column=3)

        b4 = Button(self, text="Update selected", width=12, command=self.update_command)
        b4.grid(row=5, column=3)

        b5 = Button(self, text="Delete selected", width=12, command=self.delete_command)
        b5.grid(row=6, column=3)

        b6 = Button(self, text="Close", width=12, command=self.destroy)
        b6.grid(row=7, column=3)


    def get_selected_row(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
        try:
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END,self.selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END,self.selected_tuple[4])
        except IndexError:
            pass                #in the case where the listbox is empty, the code will not execute

    def view_command(self):
        self.list1.delete(0, END)  # make sure we've cleared all entries in the listbox every time we press the View all button
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get()):
            self.list1.insert(END, row)

    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[0])
        self.view_command()

    def update_command(self):
        #be careful for the next line ---> we are updating using the texts in the entries, not the selected tuple
        database.update(self.selected_tuple[0],self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get())
        self.view_command()
"""
#code for the GUI (front end)
#window = Tk()
#Window(window)

#window.mainloop()

# Driver Code
app = tkinterApp()
app.mainloop()

