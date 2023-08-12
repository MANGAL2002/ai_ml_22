import tkinter as ttk
from tkinter import font
app=ttk.Tk()
app.geometry('800x800')
app.title('Attendance System')
font_=font.Font(size=20)
#main code is hear

ttk.Label(app,text='Face Recognition System',font=font_).pack()

def register():
    app.destroy()

    with open('opr','w') as f:
        f.write('register')
    import login_admin
    

def attendance():
    print("Attendance")

def clear_data():
    app.destroy()

    with open('opr','w') as f:
        f.write('clear')
    import login_admin
      

ttk.Button(app,text='register',command=register,font=font_,height=3,width=15,bg='#DC7633').pack(expand=True)
ttk.Button(app,text='Attendance',command=attendance,font=font_,height=3,width=15,bg='#DC7633').pack(expand=True)
ttk.Button(app,text='Clear_data',command=clear_data,font=font_,height=3,width=15,bg='#DC7633').pack(expand=True)

# end the main code and run the main code
app.mainloop()