# importing modules
from tkinter import *
import tkinter.messagebox
import sqlite3

# connect to database
conn = sqlite3.connect('database.db')
# cursor to move around the db
c = conn.cursor()
ids = []
# tkinter window
class Application:
    def __init__(self, master):
        self.master = master

        #creating the frames in the master
        self.left = Frame(master, width=800, height=720, bg='lightgreen')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side=RIGHT)

        self.heading = Label(self.left, text="POLy clinic", font=('Poppins 40 bold'), bg='lightgreen', fg='black')
        self.heading.place(x=0, y=0)

        #patient name
        self.name = Label(self.left, text="Patient's name", font=('Poppins 10 bold'), bg='lightgreen', fg='black')
        self.name.place(x=0, y=100)

        # patient age
        self.age = Label(self.left, text="Age", font=('Poppins 10 bold'), bg='lightgreen', fg='black')
        self.age.place(x=0, y=140)

        # patient gender
        self.gender = Label(self.left, text="Gender", font=('Poppins 10 bold'), bg='lightgreen', fg='black')
        self.gender.place(x=0, y=180)

        # patient location
        self.location = Label(self.left, text="Location", font=('Poppins 10 bold'), bg='lightgreen', fg='black')
        self.location.place(x=0, y=220)

        # appointment time
        self.time = Label(self.left, text="Appointment time", font=('Poppins 10 bold'), bg='lightgreen', fg='black')
        self.time.place(x=0, y=260)

        # phone number
        self.phone = Label(self.left, text="Phone number", font=('Poppins 10 bold'), bg='lightgreen', fg='black')
        self.phone.place(x=0, y=300)

        # entries for all labels
        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=250, y=100)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250, y=140)

        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=250, y=180)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=250, y=220)

        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=250, y=260)

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=250, y=300)

        #button
        self.submit = Button(self.left, text="Add Participant", width=20, height=2, bg='steelblue', command=self.add_appoinment)
        self.submit.place(x=280, y=340)

        #displaying logs on the right
        sql2 = "SELECT ID FROM appointments"
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        #ordering the ids
        self.new = sorted(ids)
        self.final_id = self.new[len(ids)-1]
        self.logs = Label(self.right, text='Logs', font=('Poppins 20 bold'), fg='white', bg='steelblue')
        self.logs.place(x=0, y=0)
        self.box = Text(self.right, width=45, height=40)
        self.box.place(x=20, y=60)
        self.box.insert(END, "Total Appointments till now: " +str(self.final_id))

    #function called when submit button is clicked
    def add_appoinment(self):
        # getting user values
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()


        # checking if any box is empty
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '' or self.val6 == '':
            tkinter.messagebox.showinfo('Warning 🤯', "Please fill up all boxes")
        else:
            sql = "INSERT INTO appointments (name, age, gender, location, scheduled_time, phone) VALUES(?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            conn.commit()
            tkinter.messagebox.showinfo('Sucess', "Appointment for " +str(self.val1) +" has been created")

            self.box.insert(END, 'Appointment fixed for '+str(self.val1) +' at '+str(self.val5) )






#creating the object
root = Tk()
b = Application(root)

#resolution of the screen
root.geometry("1200x720+0+0")

#preventing the resize feature
root.resizable(False, False)

#end the loop
root.mainloop()