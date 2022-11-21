# importing modules
from tkinter import *
import tkinter.messagebox
import sqlite3

# connect to database
conn = sqlite3.connect('database.db')
# cursor to move around the db
c = conn.cursor()

class Application:
    def __init__(self, master):
        self.master = master
        self.heading = Label(master, text="Update Appointments", fg='steelblue', font=('Poppins 40 bold'))
        self.heading.place(x=150, y=0)

        self.name = Label(master, text="Enter patient's name", font=('Poppins 10 bold'))
        self.name.place(x=0, y=80)

        self.namenet = Entry(master, width=30)
        self.namenet.place(x=200, y=82)

        self.search = Button(master, text='Search', width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=350, y=122)

    def search_db(self):
        self.input = self.namenet.get()

        #execute sql
        sql = "SELECT * FROM appointments WHERE name LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.name1 = self.row[1]
            self.age = self.row[2]
            self.gender = self.row[3]
            self.location = self.row[4]
            self.time = self.row[6]
            self.phone = self.row[5]
        #the update form
        self.uname = Label(self.master, text="Patient's name", font=('Poppins 18 bold'))
        self.uname.place(x=0, y=160)

        self.uage = Label(self.master, text="Age", font=('Poppins 18 bold'))
        self.uage.place(x=0, y=200)

        self.ugender = Label(self.master, text="gender", font=('Poppins 18 bold'))
        self.ugender.place(x=0, y=240)

        self.ulocation = Label(self.master, text="Location", font=('Poppins 18 bold'))
        self.ulocation.place(x=0, y=280)

        self.utime = Label(self.master, text="Appointment time", font=('Poppins 18 bold'))
        self.utime.place(x=0, y=320)

        self.uphone = Label(self.master, text="Patient's name", font=('Poppins 18 bold'))
        self.uphone.place(x=0, y=360)

        #entries
        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=300, y=162)
        self.ent1.insert(END, str(self.name1))

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=202)
        self.ent2.insert(END, str(self.age))

        self.ent3 = Entry(self.master, width=30)
        self.ent3.place(x=300, y=242)
        self.ent3.insert(END, str(self.gender))

        self.ent4 = Entry(self.master, width=30)
        self.ent4.place(x=300, y=282)
        self.ent4.insert(END, str(self.location))

        self.ent5 = Entry(self.master, width=30)
        self.ent5.place(x=300, y=322)
        self.ent5.insert(END, str(self.time))

        self.ent6 = Entry(self.master, width=30)
        self.ent6.place(x=300, y=362)
        self.ent6.insert(END, str(self.phone))

        self.update = Button(self.master, text="Update", width=20, height=2, bg='lightblue', command=self.update_db)
        self.update.place(x=400, y=400)

        self.delete = Button(self.master, text="Delete", width=20, height=2, bg='red', command=self.delete_db)
        self.delete.place(x=150, y=400)

    def update_db(self):
        self.var1 = self.ent1.get()
        self.var2 = self.ent2.get()
        self.var3 = self.ent3.get()
        self.var4 = self.ent4.get()
        self.var5 = self.ent5.get()
        self.var6 = self.ent6.get()

        query = "UPDATE appointments SET name=?, age=?, gender=?, location=?, phone=?, scheduled_time=? WHERE name LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo('Updated', "Sucessfully Updated")

    def delete_db(self):
        sql2 = "DELETE FROM appointments WHERE name LIKE ?"
        c.execute(sql2, (self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Deleted", "Sucessfully Deleted")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()
        self.ent6.destroy()
#creating the object
root = Tk()
b = Application(root)

#resolution of the screen
root.geometry("1200x720+0+0")

#preventing the resize feature
root.resizable(False, False)

#end the loop
root.mainloop()