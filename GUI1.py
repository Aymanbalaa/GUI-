import tkinter as tk
from tkinter import ttk
from datetime import datetime


def greet():  
    print("Welcome",user_name.get(),"!")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    str = user_name.get()+" has logged IN  at "+dt_string
    with open('LOGS.txt', 'a') as txt:
     txt.write(str)
     txt.write("\n")

def exit():
    print("Bye",user_name.get(),"!")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    str = user_name.get()+" has logged OFF at "+dt_string
    with open('LOGS.txt', 'a') as txt:
     txt.write(str)
     txt.write("\n")

root = tk.Tk()
root.title("Balaa INC")
#root.geometry("500x500")

user_name = tk.StringVar()

main = ttk.Frame(root, padding=(20, 10, 20, 0))
main.grid()

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)


#LABEL-TEXT- "NAME"
name_label = ttk.Label(main, text="Name: ")
name_label.grid(row=0, column=0, padx=(0, 10))

#INPUT FIELD FOR NAME
name_entry = ttk.Entry(main, width=15, textvariable=user_name)
name_entry.grid(row=0, column=1)
name_entry.focus()



buttons = ttk.Frame(root, padding=(20, 10))
buttons.grid(row=1, column=0, sticky="EW")

buttons.columnconfigure(0, weight=1)
buttons.columnconfigure(1, weight=1)



#LOGIN BUTTON
LOGIN_button = ttk.Button( buttons ,  text = "Log In" , command = greet)
LOGIN_button.grid(row=0, column=0, sticky="EW")

#EXIT BUTTON
destroy_button = ttk.Button( buttons ,  text = "Exit" , command = lambda:[root.destroy() , exit()])   #uses lambda to combine two functions in one command
destroy_button.grid(row=0, column=1, sticky="EW")




#ttk.Label(root,text = "Hi ayre",padding = (300,100) ).pack() 

#greet_button = ttk.Button( root ,  text = "Hi" , command = greet)

root.mainloop()


