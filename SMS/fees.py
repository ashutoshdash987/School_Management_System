from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

curdate = datetime.now().date()
app = Tk()
app.state('zoomed')
app.config(bg='black')
#----------functions for buttons------------
def spd():
    if e1.get() == "":
        messagebox.showerror("error","Registration Number is required")
    else:
        connection = mysql.connector.connect(host="localhost",username="root",password="",database="")
        mycursor = connection.cursor()
        mycursor.execute("UPDATE `cms`.`student` SET `course` = %s, `bus` = %s, `hostel` = %s, `coaching` = %s, `total` = %s WHERE (`registration_number` = %s)",( 
            course.get(), 
            bus.get(), 
            hostel.get(), 
            coaching.get(),
            int(course.get()) + int(bus.get()) + int(hostel.get()) + int(coaching.get()),
            registration_number.get()
        ))
        connection.commit()
        connection.close()
        fetch()
        messagebox.showinfo("message","Student Information has been saved Successfully !!!")
#---------------fetch data----------------
def fetch():
    connection = mysql.connector.connect(host="localhost",username="root",password="",database="")
    mycursor = connection.cursor()
    mycursor.execute("SELECT registration_number , student_name,date_of_admission, std , section , city, dommail,mentor, course , bus , hostel , coaching,total FROM cms.student")
    rows = mycursor.fetchall()
    table.delete(* table.get_children())
    for items in rows:
        table.insert("",END,values=items)
        connection.commit()
    connection.close()
#function for adding the table data into textfields
def get(event=""):
    cursor_row = table.focus()
    data = table.item(cursor_row)
    row = data['values']
    registration_number.set(row[0])
    student_name.set(row[1])
    date.set(row[2])
    std.set(row[3])
    section.set(row[4])
    course.set(row[8])
    bus.set(row[9])
    hostel.set(row[10])
    coaching.set(row[11])
    total.set(row[12])
#function for Progress Report button
def prescr():
    if int(course.get()) > 0:
        cou = 'Yes'
    else:
        cou = 'NO'
    
    if int(bus.get()) > 0:
        bu = 'YES'
    else:
        bu = 'NO'

    if int(hostel.get()) > 0:
        hos = 'YES'
    else:
        hos = 'NO'

    if int(coaching.get()) > 0:
        coa = 'YES'
    else:
        coa = 'NO'
    txt.insert(END,'\t\t    Gandhi Institute For Technology\n')
    txt.insert(END,'\t\t\t Bhubaneswar\n\n')
    txt.insert(END,'Regd. Number : ' + registration_number.get())
    txt.insert(END,'\t\t\t\t Student Name :' + student_name.get() + '\n\n')
    txt.insert(END,' Class : ' + std.get())
    txt.insert(END,'\t\t\t\t\t Section : '+ section.get() +'\n\n')
    txt.insert(END,'\t\t\t Facilities Opted \n')
    txt.insert(END,'_________________________________________________________________\n')
    txt.insert(END,'\n Course :  '+cou)
    txt.insert(END,'\t\t\t\t\t Bus :  '+bu+'\n\n')
    txt.insert(END,' Hostel :  '+hos)
    txt.insert(END,'\t\t\t\t\t Coaching :  '+coa+'\n')
    txt.insert(END,'\t\t\t Fees Breakdown \n')
    txt.insert(END,'_________________________________________________________________\n')
    txt.insert(END,'\n Course Fee:  Rs '+ course.get())
    txt.insert(END,'\t\t\t\t\t Bus :  Rs '+ bus.get() + '\n\n')
    txt.insert(END,' Hostel :  Rs '+hostel.get())
    txt.insert(END,'\t\t\t\t\t Coaching :  Rs '+coaching.get() + '\n\n')
    txt.insert(END,'\t\t   Total Fees :  Rs '+total.get() + '\n\n')
    txt.insert(END,'\n\t\t\t\t Gandhi Institute For Technology, BBSR')
    txt.insert(END,'\nParents Signature\t\t\t\t\tFull Signature/Stamp : \n\n')
#function for delete button
def dltt():
    confirm = messagebox.askyesnocancel('confirmation','Are you sure you want to delete')
    if confirm == TRUE:
        connection = mysql.connector.connect(host="localhost",username="root",password="",database="")
        mycursor = connection.cursor()
        query = ("DELETE FROM `cms`.`student` WHERE (`registration_number` = %s)")
        value = (registration_number.get(),)
        mycursor.execute(query,value)
        connection.commit()
    connection.close()
    fetch()
#function for clear butotn
def clr():
    registration_number.set('')
    student_name.set('')
    date.set('')
    std.set('')
    section.set('')
    course.set('')
    bus.set('')
    hostel.set('')
    coaching.set('')
    total.set('')
    txt.delete(1.0,END)
    cdate()
#function for exit button
def exit():
    confirm = messagebox.askyesnocancel('confirmation','Are you sure you want to exit')
    if confirm == TRUE:
        app.destroy()
# Student management system heading
Label(app,text="Student Management System(Fees)",font='impack 31 bold',bg='gray',fg='white').pack(fill='x')
#information frame
frame1 = Frame(app,bd='15',relief=RIDGE)
frame1.place(x = 0,y = 54,width=1540,height=450)
#frame for student information
lf1 = LabelFrame(frame1,bd='5',text='Fees Details',bg='white',fg='blue',font='ariel 12 bold')
lf1.place(x=10,y=0,width=900,height=420)
#label for student information
Label(lf1,text='Registration Number*',font='ariel 12',bg='white',fg='brown').place(x=5,y=10)
Label(lf1,text='Name Of Student*',font='ariel 12',bg='white',fg='brown').place(x=5,y=60)
Label(lf1,text='Course fees (Rs)',font='ariel 12',bg='white').place(x=5,y=110)
Label(lf1,text='Bus Fees (Rs)',font='ariel 12',bg='white').place(x=5,y=160)
Label(lf1,text='Hostel Fees (Rs)',font='ariel 12',bg='white').place(x=5,y=210)
Label(lf1,text='Coaching Fees (Rs)',font='ariel 12',bg='white').place(x=5,y=260)
Label(lf1,text='Total Fees (Rs)',font='ariel 12',bg='white',fg='indigo').place(x=5,y=310)
Label(lf1,text='Date',font='ariel 12',bg='white').place(x=650,y=10)
Label(lf1,text='Class',font='ariel 12',bg='white').place(x=650,y=60)
Label(lf1,text='Section',font='ariel 12',bg='white').place(x=650,y=110)
#---------------text variable for every entry field------------
registration_number = StringVar()
student_name = StringVar()
course = StringVar()
bus = StringVar()
hostel = StringVar()
coaching = StringVar()
date = StringVar()
std = StringVar()
section = StringVar()
total = StringVar()
#--------------Entry Field For Information--------------------
e1 = Entry(lf1,bd='3',font='impack 13',textvariable = registration_number)
e1.place(x=160,y=10,width=300)

e2 = Entry(lf1,bd='3',font='impack 13',textvariable=student_name)
e2.place(x=160,y=60,width=300)

e3 = Entry(lf1,bd='3',font='impack 13',textvariable=course)
e3.place(x=160,y=110,width=300)

e4 = Entry(lf1,bd='3',font='impack 13',textvariable=bus)
e4.place(x=160,y=160,width=300)

e5 = Entry(lf1,bd='3',font='impack 13',textvariable=hostel)
e5.place(x=160,y=210,width=300)

e6 = Entry(lf1,bd='3',font='impack 13',textvariable=coaching)
e6.place(x=160,y=260,width=300)

e7 = Entry(lf1,bd='3',font='impack 13',textvariable=total)
e7.place(x=160,y=310,width=300)

e9 = Entry(lf1,bd='3',font='impack 13',textvariable=date)
e9.place(x=725,y=10,width=150)

e10 = Entry(lf1,bd='3',font='impack 13',textvariable=std)
e10.place(x=725,y=60,width=150)

e11 = Entry(lf1,bd='3',font='impack 13',textvariable=section)
e11.place(x=725,y=110,width=150) 
def cdate():
    e9.insert(0,curdate)
#-----------------------------------------------------
#label for report
lf2 = LabelFrame(frame1,bd='5',text='Report',bg='white',fg='blue',font='ariel 12 bold')
lf2.place(x=912,y=0,width=600,height=420)
#textbox for report
txt = Text(lf2,font='impack 12',width=40,height=30,bg='pink')
txt.pack(fill=BOTH)
#details frame
frame2 = Frame(app,bd='15',relief=RIDGE)
frame2.place(x='0',y='500',width=1540,height=250)
#----------------buttons for function---------------------
dlt = Button(app,text='Delete',font='ariel 15 bold',bg='red',fg='white',bd='5',cursor='hand2',command=dltt)
dlt.place(x=0,y=750,width=280)

pres = Button(app,text='Generate Report',font='ariel 15 bold',bg='violet',fg='white',bd='5',cursor='hand2',command=prescr)
pres.place(x=280,y=750,width=280)

save = Button(app,text='Update Fees',font='ariel 15 bold',bg='green',fg='white',bd='5',cursor='hand2',command=spd)
save.place(x=560,y=750,width=420)

clear = Button(app,text='Clear',font='ariel 15 bold',bg='violet',fg='white',bd='5',cursor='hand2',command=clr)
clear.place(x=980,y=750,width=280)

exit = Button(app,text='Exit',font='ariel 15 bold',bg='red',fg='white',bd='5',cursor='hand2',command=exit)
exit.place(x=1260,y=750,width=280)
#---------------------------------------------------------
#---------scroll bar for student data----------
scrollx=ttk.Scrollbar(frame2,orient=HORIZONTAL)
scrollx.pack(side='bottom',fill='x')

scrolly=ttk.Scrollbar(frame2,orient=VERTICAL)
scrolly.pack(side='right',fill='y')

table = ttk.Treeview(frame2,columns=('regd','name','date','std','section','city','dommail','mentor','course','bus','hostel','coaching'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
scrollx = ttk.Scrollbar(command=table.xview())
scrolly = ttk.Scrollbar(command=table.yview())
#---------------------------------------------------

#-------heading for student data----------
table.heading('regd',text='Registration Number')
table.heading('name',text='Student Name')
table.heading('date',text='Date')
table.heading('std',text='Class')
table.heading('section',text='Section')
table.heading('city',text='City')
table.heading('dommail',text='Dommail')
table.heading('mentor',text='Mentor')
table.heading('course',text='Course Fee')
table.heading('bus',text='Bus Fee')
table.heading('hostel',text='Hostel Fee')
table.heading('coaching',text='Coaching Fee')
table['show'] = 'headings'
table.pack(fill=BOTH,expand=1)
#---------------------------------------------
#-------Table column width-------
table.column('regd',width=100)
table.column('name',width=100)
table.column('date',width=100)
table.column('std',width=100)
table.column('section',width=100)
table.column('city',width=100)
table.column('dommail',width=100)
table.column('mentor',width=100)
table.column('course',width=100)
table.column('bus',width=100)
table.column('hostel',width=100)
table.column('coaching',width=100)
#--------------------------------
table.bind('<ButtonRelease-1>',get)
fetch()
cdate()
mainloop()