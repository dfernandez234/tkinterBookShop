from tkinter import *
import library

def view_func():
    list1.delete(0, END)
    rows=library.view_all()
    for item in rows:
        list1.insert(END, item)

def search_func():
    result=library.search_entry(entrie_values[0].get(), entrie_values[1].get(), entrie_values[2].get(), entrie_values[3].get())
    for item in result:
        list1.insert(END, item)

def add_func():
    library.add_entry(entrie_values[0].get(), entrie_values[1].get(), entrie_values[2].get(), entrie_values[3].get())
    for i in range(0,len(entries)):
        entries[i].delete(0,"end")
    view_func()

def selection(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple=list1.get(index)
        for i in range(0,len(entries)):
            entries[i].delete(0,"end")
            entries[i].insert(i,selected_tuple[i+1])
    except IndexError:
        pass

def delete_func():
    library.delete_selected(int(selected_tuple[0]))
    view_func()

def update_func():
    index = selected_tuple[0]
    library.update_selected(entrie_values[0].get(), entrie_values[1].get(), entrie_values[2].get(), entrie_values[3].get(),index)
    view_func()



window  = Tk()
library.connect()

label_text = ["Title", "Author", "Year", "ISBN"]
labels = []
entries = []
entrie_values=[]

for i in range(0,len(label_text)):
    entrie_values.append(StringVar())
    labels.append(Label(window, text=label_text[i]))
    entries.append(Entry(window, textvariable=entrie_values[i]))

labels[0].grid(row = 0, column = 0)
labels[1].grid(row = 0, column = 2)  
labels[2].grid(row = 1, column = 0)
labels[3].grid(row = 1, column = 2)

entries[0].grid(row = 0, column = 1)
entries[1].grid(row = 0, column = 3)
entries[2].grid(row = 1, column = 1)
entries[3].grid(row = 1, column = 3)


button_text = ["View All", "Search Entry", "Add Entry", "Update Selected", "Delete Selected", "Close"]
buttons = []

for i in range(0,len(button_text)):
    buttons.append(Button(window, text=button_text[i], width = 15))
    buttons[i].grid(row = i+2, column = 3)

buttons[0].configure(command=view_func)
buttons[1].configure(command=search_func)
buttons[2].configure(command=add_func)
buttons[3].configure(command=update_func)
buttons[4].configure(command=delete_func)
buttons[5].configure(command=window.destroy)

list1 = Listbox(window, height = 6, width = 40)
list1.grid(row =2, column = 0, rowspan=6, columnspan= 2)
sb1 = Scrollbar(window)
sb1.grid(row = 4, column = 2)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command = list1.yview)
list1.bind('<<ListboxSelect>>', selection)

window.mainloop()


