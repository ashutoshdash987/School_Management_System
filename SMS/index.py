from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from datetime import datetime
import subprocess

curdate = datetime.now().date()
apu = Tk()
apu.state('zoomed')
apu.config(bg='black')

connection = mysql.connector.connect(host="localhost",username="root",password="",database="")
def cal():
    username = e1.get()
    password = e2.get()
    mycursor = connection.cursor()
    mycursor.execute("SELECT count(1) FROM login WHERE username = %s and password = %s",(username,password))
    count = mycursor.fetchall()
    if count[0][0] == 1:
        subprocess.Popen(["python","admission.py"])
        apu.destroy()
    else:
        messagebox.showerror("error","incorrect username or password !!")
def fees():
    username = e1.get()
    password = e2.get()
    mycursor = connection.cursor()
    mycursor.execute("SELECT count(1) FROM login WHERE username = %s and password = %s",(username,password))
    count = mycursor.fetchall()
    if count[0][0] == 1:
        subprocess.Popen(["python","fees.py"])
        apu.destroy()
    else:
        messagebox.showerror("error","incorrect username or password !!")
def pay():
    username = e1.get()
    password = e2.get()
    mycursor = connection.cursor()
    mycursor.execute("SELECT count(1) FROM login WHERE username = %s and password = %s",(username,password))
    count = mycursor.fetchall()
    if count[0][0] == 1:
        subprocess.Popen(["python","dues.py"])
        apu.destroy()
    else:
        messagebox.showerror("error","incorrect username or password !!")

Label(apu,text="Student Management System",font='impack 31 bold',bg='gray',fg='white').pack(fill='x')
#information frame
frame1 = Frame(apu,bd='15',relief=RIDGE)
frame1.place(x = 0,y = 54,width=1540,height=740)

lf1 = LabelFrame(frame1,bd='5',text='Student Information',bg='white',fg='blue',font='ariel 12 bold')
lf1.place(x=350,y=20,width=800,height=620)

Label(lf1,text='Username',font='ariel 12',bg='white',fg='brown').place(x=200,y=50)
Label(lf1,text='Password',font='ariel 12',bg='white',fg='brown').place(x=200,y=100)

username = StringVar()
password = StringVar()

e1 = Entry(lf1,bd='0.8',font='impack 13',textvariable = username)
e1.place(x=280,y=50,width=300)

e2 = Entry(lf1,bd='0.8',font='impack 13',textvariable=password)
e2.place(x=280,y=100,width=300)

sin = Button(apu,text='New Admission',font='ariel 15 bold',bg='red',fg='white',bd='2',cursor='hand2',command=cal)
sin.place(x=380,y=300,width=250)

sin2 = Button(apu,text='Add Fees',font='ariel 15 bold',bg='red',fg='white',bd='2',cursor='hand2',command=fees)
sin2.place(x=640,y=300,width=250)

sin3 = Button(apu,text='Fee Payment',font='ariel 15 bold',bg='red',fg='white',bd='2',cursor='hand2',command=pay)
sin3.place(x=900,y=300,width=250)

mainloop()