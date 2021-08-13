#Salary Slip
#accept emp id,name of emp,department,grade,basic and allownces offered (LTA,Educational,Laundry)
#fixed(HRA,DA,Medical)
#claculate gross pay
#(basic+hra+da+selected allownces)
from tkinter import *
from tkinter import ttk
def show():
    bp=int(basic.get())
    grade=0
    if r_button.get()>0:
        grade=r_button.get()
    else:
        grade=0
    if v1.get():
        hr= v1.get()
    else:
        hr=0
    if v2.get():
        d= v2.get()
    else:
        d=0
    if v3.get():
        med= v3.get()
    else:
        med=0
    gross_salary= bp + hr + d + med + grade
    hra.delete(0,'end')
    da.delete(0,'end')
    basic.delete(0,'end')
    medical.delete(0,'end')
    gross.delete(0,'end')
    hra.insert(0,str(hr))
    da.insert(0,str(d))
    medical.insert(0,str(med))
    gross.insert(0,str(gross_salary))

page=Tk()
page.geometry('500x500')
page.title('Salary Slip')
Label(page,text='Emp_ID',height=2,width=10,bg='darkgrey').grid(row=0,column=0)
id=Entry(page,width=15,bd=10,bg='cornflowerblue',justify='center')
id.grid(row=0,column=1)
Label(page,text='Name',height=2,width=10,bg='darkgrey').grid(row=1,column=0)
na=Entry(page,width=15,bg='cornflowerblue',bd=10,justify='center')
na.grid(row=1,column=1)
cbox1=StringVar()
cbox2=StringVar()
r_button=IntVar()
v1=IntVar()
v2=IntVar()
v3=IntVar()
Label(page,text='Department',height=2,width=10,bg='darkgrey').grid(row=2,column=0)
dep=ttk.Combobox(page,width=15,textvariable=cbox1)
dep.grid(row=2,column=1)
dep['values']=('Software developer','Software tester','Sales','Manger','Accounts','Marketing','Technical support')
dep.current()
r1=Radiobutton(page,text='G1',value=1500,variable=r_button)
r1.grid(row=3,column=0)
r2=Radiobutton(page,text='G2',value=1000,variable=r_button)
r2.grid(row=3,column=1)
r3=Radiobutton(page,text='G3',value=500,variable=r_button)
r3.grid(row=3,column=2)
r4=Radiobutton(page,text='Contract',value=2,variable=r_button)
r4.grid(row=3,column=3)
Label(page,text='Basic Pay',height=2,width=10,bg='darkgrey').grid(row=4,column=0)
basic=Entry(page,width=15,bd=10,bg='cornflowerblue',justify='center')
basic.grid(row=4,column=1)
c1=Checkbutton(page,text='HRA',variable=v1,onvalue=2500,offvalue=0)
c1.grid(row=5,column=0)
hra=Entry(page,width=15,bd=10,bg='cornflowerblue',justify='center')
hra.grid(row=5,column=1)
c2=Checkbutton(page,text='DA',variable=v2,onvalue=2000,offvalue=0)
c2.grid(row=6,column=0)
da=Entry(page,width=15,bd=10,bg='cornflowerblue',justify='center')
da.grid(row=6,column=1)
c3=Checkbutton(page,text='Medical',variable=v3,onvalue=2500,offvalue=0)
c3.grid(row=7,column=0)
medical=Entry(page,width=15,bd=10,bg='cornflowerblue',justify='center')
medical.grid(row=7,column=1)
btn=Button(page,text='Submit',command=show,height=2,width=10,bd=10,bg='wheat',relief='groove',cursor='dot',justify='center')
btn.grid(row=7,column=2)
Label(page,text='Gross Pay',height=2,width=10,bg='darkgrey').grid(row=8,column=0)
gross=Entry(page,width=15,bd=10,bg='cornflowerblue',justify='center')
gross.grid(row=8,column=1)
page.mainloop()