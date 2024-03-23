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
    if e2.get() == "":
        messagebox.showerror("error","Student Name and Registration Number is required")
    else:
        connection = mysql.connector.connect(host="localhost",username="root",password="",database="")
        mycursor = connection.cursor()
        mycursor.execute("INSERT INTO `cms`.`student` (`student_name`, `date_of_admission`, `std`, `section`, `city`, `lastmark`, `stream`, `labgrp`, `dommail`, `mentor`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
            student_name.get(),
            date_of_admission.get(),
            std.get(),
            section.get(), 
            city.get(), 
            LastMark.get(), 
            stream.get(), 
            LabGroup.get(), 
            domMail.get(),
            mentor.get(),
        ))
        connection.commit()
        connection.close()
        fetch()
        messagebox.showinfo("message","Student Information has been saved Successfully !!!")
#---------------fetch data----------------
def fetch():
    connection = mysql.connector.connect(host="localhost",username="root",password="",database="")
    mycursor = connection.cursor()

    mycursor.execute("select * from student")
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
    date_of_admission.set(row[2])
    std.set(row[3])
    section.set(row[4])
    city.set(row[5])
    LastMark.set(row[6])
    stream.set(row[7])
    LabGroup.set(row[8])
    domMail.set(row[9])
    mentor.set(row[10])
#function for Progress Report button
def prescr():
    txt.insert(END,'\t\t    Gandhi Institute For Technology\n')
    txt.insert(END,'\t\t\t Bhubaneswar\n\n')
    txt.insert(END,'Student Name : \t\t'+student_name.get()+'\t\t\t Registration Number :\t'+registration_number.get()+'\n\n')
    txt.insert(END,'Mentor : \t\t'+mentor.get()+'\t\t              Date Of Admission : \t'+date_of_admission.get()+'\n\n')
    txt.insert(END,'Status : \t\t'+'active'+'\t\t Class : '+std.get()+'\t\tSection  '+section.get()+'\n\n')
    txt.insert(END,'_________________________________________________________________\n')
    txt.insert(END,'City : \t\t'+city.get() + '\t\t\t Last % : \t'+LastMark.get()+' %'+'\n')
    txt.insert(END,'Stream : \t\t'+stream.get() + '\t\t\t Lab Group : \t'+LabGroup.get() + '\n')
    txt.insert(END,'Domain ID : \t\t'+domMail.get() + '\n')
    txt.insert(END,'\nRemark : \n\n')
    txt.insert(END,'\n\t\t\t\t Gandhi Institute For Technology, BBSR')
    txt.insert(END,'\n\t\t\t\t\tFull Signature/Stamp : \n\n')
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
    date_of_admission.set('')
    std.set('')
    section.set('')
    city.set('')
    LastMark.set('')
    stream.set('')
    LabGroup.set('')
    domMail.set('')
    mentor.set('')
    txt.delete(1.0,END)
    cdate()
#function for exit button
def exit():
    confirm = messagebox.askyesnocancel('confirmation','Are you sure you want to exit')
    if confirm == TRUE:
        app.destroy()
# student management system heading
Label(app,text="Student Management System",font='impack 31 bold',bg='gray',fg='white').pack(fill='x')
#information frame
frame1 = Frame(app,bd='15',relief=RIDGE)
frame1.place(x = 0,y = 54,width=1540,height=450)
#frame for patient information
lf1 = LabelFrame(frame1,bd='5',text='Student Information',bg='white',fg='blue',font='ariel 12 bold')
lf1.place(x=10,y=0,width=900,height=420)
#label for student information
# Label(lf1,text='Registration Number*',font='ariel 12',bg='white',fg='brown').place(x=5,y=10)
Label(lf1,text='Name Of Student*',font='ariel 12',bg='white',fg='brown').place(x=5,y=60)
Label(lf1,text='Mentor',font='ariel 12',bg='white').place(x=5,y=110)
Label(lf1,text='City',font='ariel 12',bg='white').place(x=5,y=160)
Label(lf1,text='Last %',font='ariel 12',bg='white').place(x=5,y=210)
Label(lf1,text='Stream',font='ariel 12',bg='white').place(x=5,y=260)
Label(lf1,text='Lab Group',font='ariel 12',bg='white').place(x=5,y=310)
Label(lf1,text='Domain Id',font='ariel 12',bg='white').place(x=5,y=360)
Label(lf1,text='Date',font='ariel 12',bg='white').place(x=650,y=10)
Label(lf1,text='Class',font='ariel 12',bg='white').place(x=650,y=60)
Label(lf1,text='Section',font='ariel 12',bg='white').place(x=650,y=110)
#---------------text variable for every entry field------------
registration_number = StringVar()
student_name = StringVar()
date_of_admission = StringVar()
std = StringVar()
section = StringVar()
city = StringVar()
LastMark = StringVar()
stream = StringVar()
LabGroup = StringVar()
domMail = StringVar()
mentor = StringVar()
#--------------Entry Field For Information--------------------
# e1 = Entry(lf1,bd='3',font='impack 13',textvariable = registration_number)
# e1.place(x=160,y=10,width=300)

e2 = Entry(lf1,bd='3',font='impack 13',textvariable=student_name)
e2.place(x=160,y=60,width=300)

e3 = Entry(lf1,bd='3',font='impack 13',textvariable=mentor)
e3.place(x=160,y=110,width=300)

e4 = Entry(lf1,bd='3',font='impack 13',textvariable=city)
e4.place(x=160,y=160,width=300)

e5 = Entry(lf1,bd='3',font='impack 13',textvariable=LastMark)
e5.place(x=160,y=210,width=300)

e6 = Entry(lf1,bd='3',font='impack 13',textvariable=stream)
e6.place(x=160,y=260,width=300)

e7 = Entry(lf1,bd='3',font='impack 13',textvariable=LabGroup)
e7.place(x=160,y=310,width=300)

e8 = Entry(lf1,bd='3',font='impack 13',textvariable=domMail)
e8.place(x=160,y=360,width=300)

e9 = Entry(lf1,bd='3',font='impack 13',textvariable=date_of_admission)
e9.place(x=725,y=10,width=150)

e10 = Entry(lf1,bd='3',font='impack 13',textvariable=std)
e10.place(x=725,y=60,width=150)

e11 = Entry(lf1,bd='3',font='impack 13',textvariable=section)
e11.place(x=725,y=110,width=150)

def cdate():
    e9.insert(0,curdate)
#-----------------------------------------------------
#label for report generation
lf2 = LabelFrame(frame1,bd='5',text='Progress Report',bg='white',fg='blue',font='ariel 12 bold')
lf2.place(x=912,y=0,width=600,height=420)

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

save = Button(app,text='Save Student Data',font='ariel 15 bold',bg='green',fg='white',bd='5',cursor='hand2',command=spd)
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

table = ttk.Treeview(frame2,columns=('regd','name','date','std','section','city','last %','stream','lab group','domain ID','mentor'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
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
table.heading('last %',text='Last %')
table.heading('stream',text='Stream')
table.heading('lab group',text='Lab Group')
table.heading('domain ID',text='Domain ID')
table.heading('mentor',text='Mentor')
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
table.column('last %',width=100)
table.column('stream',width=100)
table.column('lab group',width=100)
table.column('domain ID',width=100)
table.column('mentor',width=100)
#--------------------------------
table.bind('<ButtonRelease-1>',get)
fetch()
cdate()
mainloop()
