from tkinter import *

root=Tk()
root.config(bg='light green')
root.title("TEMPRATURE CONVERTOR")
root.geometry('855x800')
Label(root,text="TEMPRATURE CONVERTER",font="Revamped 40",fg="Dark ReD",relief=RAISED,padx=20,pady=20).grid(columnspan=7)

def C_to_f():
    my_label=Label(root,text="Enter the temperature in Celcius",anchor=CENTER,font="TIMES 25",bg="light green")
    my_label.grid(row=4,column=0)
    my_label1=Label(root,text="Temperature in Fahern is",anchor=CENTER,font="TIMES 25",bg="light green")
    my_label1.grid(row=5,column=0)
    e=Entry(root,width=60,borderwidth=3)
    e.grid(row=4,column=1,columnspan=3)
    e1=Entry(root,width=60,borderwidth=3)
    e1.grid(row=5,column=1,columnspan=3)
    def convert():
        cval=e.get()
        F = (9 / 5)*int(cval) + 32
        e1.insert(0,F)
        my_button_con['state']=DISABLED
    my_button_con = Button(root, text="CONVERT", padx=30, borderwidth=2, pady=20,font="Revamped 20",bg="Royal blue",command=convert)
    my_button_con.grid(row=6,column=1)
def k_to_cel():
    my_label = Label(root, text="Enter the temperature in Celcius",font="TIMES 25",bg="light green")
    my_label.grid(row=4, column=0)
    my_label1 = Label(root, text="Temperature in Kelvin is",font="TIMES 25",bg="light green")
    my_label1.grid(row=5, column=0)
    e = Entry(root, width=60, borderwidth=3)
    e.grid(row=4, column=1, columnspan=3)
    e1 = Entry(root, width=60, borderwidth=3)
    e1.grid(row=5, column=1, columnspan=3)

    def convert():
        cval1 = e.get()
        K=int(cval1)+273
        e1.insert(0, K)
        my_button_con['state']=DISABLED

    my_button_con = Button(root, text="CONVERT",padx=30,relief=RAISED,borderwidth=4,pady=20,font="Revamped 20",bg="Royal blue",command=convert)
    my_button_con.grid(row=6, column=1)

b1=Button(root,text="Celius to Fahernheit",anchor=NW,justify=LEFT,command=C_to_f)
b2=Button(root,text="Celcius to Kelvin",anchor=NW,justify=LEFT,command=k_to_cel)
b2.grid(row=1,column=0)
b1.grid(row=2,column=0)
root.mainloop()