from tkinter import *

root = Tk()
root.config(bg='light green')
root.title("TEMPRATURE CONVERTER")
root.geometry('855x400')
# heading
Label(root, text="TEMPRATURE CONVERTER", font="Revamped 40", fg="Dark ReD", relief=RAISED, padx=20, pady=20).grid(columnspan=7)
# create MENU
my_menu = Menu(root)
root.config(menu=my_menu)


# function to convert celcius to fahernheit
def comm():
    my_label = Label(root, text="Enter the temperature in Celcius", anchor=CENTER, font="TIMES 25", bg="light green")
    my_label.grid(row=4, column=0)
    my_label1 = Label(root, text="Temperature in Fahern is", anchor=CENTER, font="TIMES 25", bg="light green")
    my_label1.grid(row=5, column=0)
    e = Entry(root, width=60, borderwidth=3)
    e.grid(row=4, column=1, columnspan=3)
    e1 = Entry(root, width=60, borderwidth=3)
    e1.grid(row=5, column=1, columnspan=3)

    # main function which converts the temprature
    def convert():
        cval = e.get()
        F = (9 / 5) * int(cval) + 32
        e1.insert(0, str(F) + " "+ "F")
        my_button_con['state'] = DISABLED

    my_button_con = Button(root, text="CONVERT", padx=30, borderwidth=2, pady=20, font="Revamped 20", bg="Royal blue",
                           command=convert)
    my_button_con.grid(row=6, column=1)


# from  celcius to kelvin
def comm1():
    my_label = Label(root, text="Enter the temperature in Celcius", font="TIMES 25", bg="light green")
    my_label.grid(row=4, column=0)
    my_label1 = Label(root, text="Temperature in Kelvin is", font="TIMES 25", bg="light green")
    my_label1.grid(row=5, column=0)
    e = Entry(root, width=60, borderwidth=3)
    e.grid(row=4, column=1, columnspan=3)
    e1 = Entry(root, width=60, borderwidth=3)
    e1.grid(row=5, column=1, columnspan=3)

    # main function which converts the temprature
    def convert():
        cval1 = e.get()
        K = int(cval1) + 273
        e1.insert(0, str(K) + " "+"K")
        my_button_con['state'] = DISABLED

    my_button_con = Button(root, text="CONVERT", padx=30, relief=RAISED, borderwidth=4, pady=20, font="Revamped 20",
                           bg="Royal blue", command=convert)
    my_button_con.grid(row=6, column=1)


# create a menu items
file_menu = Menu(my_menu)
my_menu.add_cascade(label="Types", menu=file_menu)

# items of file
file_menu.add_command(label="C to F", command=comm)
file_menu.add_separator()             # seperates the options
file_menu.add_command(label="C to K", command=comm1)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=root.quit)

root.mainloop()
