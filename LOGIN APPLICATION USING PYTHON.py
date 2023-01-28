from tkinter import*
top=Tk()
top.title("LOGIN APPLICATION")
top.geometry("2000x100")
lbl1=Label(top,text="UserName")
lbl1.grid(column=1,row=1)
e1=Entry(top,bd=5)
e1.grid(column=2,row=1)
lbl2=Label(top,text="Password")
lbl2.grid(column=2,row=2)
e2=Entry(top,bd=5)
e2.grid(column=2,row=2)
def test():
    s1=e1.get()
    s2=e2.get()
    if(s1=="Admin" and s2=="Admin"):
        print("Login Success")
    else:
        print("Login Failed")
b1=Button(top,text="Login",command=test)
b1.grid(column=2,row=3)
top.mainloop()