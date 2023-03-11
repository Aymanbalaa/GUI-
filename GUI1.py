import tkinter as tk
from tkinter import ttk
from datetime import datetime

import GUI2

def Contact():
    Contact = tk.Tk()
    Contact.title("contact")
    Contact_label = ttk.Label(Contact, text= "Name : Ayman El Balaa \n Email : Aymanbalaa@hotmail.com")
    Contact_label.grid(row=1, column=0, padx=(0, 20))



def greet():  
    print("Welcome",user_name.get(),"!")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    if (user_name.get() == ""):
        user_name.set("Guest")

    str = user_name.get()+" has logged IN  at "+dt_string
    with open('LOGS.txt', 'a') as txt:
     txt.write(str)
     txt.write("\n")

def exit():
    print("Bye",user_name.get(),"!")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    #if (user_name.get() == 0 | user_name.get() == ""):
     #   user_name.set("Guest")

    str = user_name.get()+" has logged OFF at "+dt_string
    with open('LOGS.txt', 'a') as txt:
     txt.write(str)
     txt.write("\n")


   

menu = tk.Tk()
menu.title("Balaa INC")

#menu.geometry("500x500")

user_name = tk.StringVar()

main = ttk.Frame(menu, padding=(20, 10, 20, 0))
main.grid()

menu.columnconfigure(0, weight=1)
menu.rowconfigure(1, weight=1)



#LABEL-TEXT- "NAME"
name_label = ttk.Label(main, text="Name: ")
name_label.grid(row=0, column=0, padx=(0, 10))
#INPUT FIELD FOR NAME
name_entry = ttk.Entry(main, width=15, textvariable=user_name)
name_entry.grid(row=0, column=1)
name_entry.focus()
    



buttons = ttk.Frame(menu, padding=(20, 10))
buttons.grid(row=1, column=0, sticky="EW")

buttons.columnconfigure(0, weight=1)
buttons.columnconfigure(1, weight=1)



#LOGIN BUTTON
LOGIN_button = ttk.Button( buttons ,  text = "Log In" , command = greet)
LOGIN_button.grid(row=0, column=0, sticky="EW")

#EXIT BUTTON
destroy_button = ttk.Button( buttons ,  text = "Exit" , command = lambda:[menu.destroy() , exit()])   #uses lambda to combine two functions in one command
destroy_button.grid(row=0, column=1, sticky="EW")

Contact_button = ttk.Button( menu ,  text = "Contact" , command = lambda:[menu.destroy() , Contact()])   #uses lambda to combine two functions in one command
Contact_button.grid(row=7, column=0, sticky="EW")

text_scroll = ttk.Scrollbar(menu , orient = "vertical" )
text_scroll.grid ( row = 0,column =1,sticky = "ns")
#text["yscrollcommand"] = text_scroll.set

#ttk.Label(menu,text = "Hi ayre",padding = (300,100) ).pack() 

#greet_button = ttk.Button( menu ,  text = "Hi" , command = greet)


ttk.Separator(menu, orient="horizontal").grid(row=2, column=0, sticky="EW", pady=10)

credits_label = ttk.Label(menu, text="© 2023 Balaa INC , All Rights Reserved")
credits_label.grid(row=6, column=0, padx=(0, 10))
menu.mainloop()



