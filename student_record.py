from tkinter import *
from student_backend import *

"""A simple program to store the cgpa details of student making use of Tkinter module"""


def get_selected(event):
    try:
        global select
        index = lb.curselection()[0]
        select = lb.get(index)
        e1.delete(0, END)
        e1.insert(END, select[1])
        e2.delete(0, END)
        e2.insert(END, select[2])
        e3.delete(0, END)
        e3.insert(END, select[3])
        e4.delete(0, END)
        e4.insert(END, select[4])
    except:
        pass


def command_view():
    lb.delete(0, END)
    for rows in view():
        lb.insert(END, rows)


def command_search():
    lb.delete(0, END)
    for rows in search(roll.get(), sgpa.get(), semester.get(), year.get()):
        lb.insert(END, rows)


def command_add():
    insert(roll.get(), sgpa.get(), semester.get(), year.get())
    lb.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    command_view()


def command_delete():
    delete(select[0])
    lb.delete(0, END)
    command_view()
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


def command_update():
    update(select[0], roll.get(), sgpa.get(), semester.get(), year.get())
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    lb.delete(0, END)
    command_view()


window = Tk()

l1 = Label(window, text="Roll No")
l1.grid(row=0, column=0)

roll = StringVar()
e1 = Entry(window, textvariable=roll)
e1.grid(row=0, column=1)

l2 = Label(window, text="SGPA")
l2.grid(row=0, column=2)

sgpa = StringVar()
e2 = Entry(window, textvariable=sgpa)
e2.grid(row=0, column=3)

l3 = Label(window, text="Semester")
l3.grid(row=1, column=0)

semester = StringVar()
e3 = Entry(window, textvariable=semester)
e3.grid(row=1, column=1)

l4 = Label(window, text="Year")
l4.grid(row=1, column=2)

year = StringVar()
e4 = Entry(window, textvariable=year)
e4.grid(row=1, column=3)

lb = Listbox(window, height=10, width=35)
lb.grid(row=2, column=0, rowspan=6, columnspan=2)

sb = Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

lb.bind('<<ListboxSelect>>', get_selected)

b1 = Button(window, text="View All", width=12, command=command_view)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12, command=command_search)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12, command=command_add)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update Selected", width=12, command=command_update)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete Selected", width=12, command=command_delete)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.wm_title("Student Record")
window.mainloop()
