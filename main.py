import tkinter as tk
from tkinter import messagebox
from tkinter import *
from time import gmtime, strftime
import os


def is_number(s):
    try:
        float(s)
        return True
    except:
        return False


def check_acc_nmb(num):
    try:
        fpin = open(num + ".txt", 'r')
    except FileNotFoundError:
        messagebox.showinfo("Error", "Invalid Credentials!\nTry Again!")
        return 0
    fpin.close()
    return


def home_return(master):
    master.destroy()
    Main_Menu()


# logic to create an account
def write(master, name, oc, pin):
    if (is_number(name)) or (is_number(oc) == 0) or (is_number(pin) == 0) or name == "":
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.withdraw()
        return
    
    with open("Accnt_Record.txt", 'r') as f1:
        accnt_no = int(f1.readline())

    accnt_no += 1

    with open("Accnt_Record.txt", 'w') as f1:
        f1.write(str(accnt_no))

    with open(str(accnt_no) + ".txt", 'w') as fdet:
        fdet.write(pin + "\n")
        fdet.write(oc + "\n")
        fdet.write(str(accnt_no) + "\n")
        fdet.write(name + "\n")

    with open(str(accnt_no) + "-rec.txt", 'w') as frec:
        frec.write("Date        credit   Debit   Balance\n")
        frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S] ", gmtime())) + "    " + oc + "     " + oc + "\n")

    messagebox.showinfo("Details", "Your account number is:" + str(accnt_no))
    master.withdraw()
    master.mainloop()
    return


# logic to credit the amount
def cedt_write(master, amt, accnt, name):
    if (is_number(amt)<=0 or float(amt) <=0) :
        messagebox.showinfo("Error", "Invalid credentials\nPlease try again.")
        master.destroy()
        master.mainloop()
        return

    # Check if the file exists, if not, create it
    file_path = accnt + ".txt"
    if not os.path.exists(file_path):
        with open(file_path, 'w') as fdet:
            fdet.write("initial_pin\n0\n" + accnt + "\n" + name + "\n")

    #file_path = accnt + ".txt"
   # print("File path:", os.path.abspath(file_path))

    with open(accnt + ".txt", 'r') as fdet:
        pin = fdet.readline()
        camt = int(fdet.readline())

    amti = int(amt)
    cb = amti + camt

    with open(accnt + ".txt", 'w') as fdet:
        fdet.write(pin)
        fdet.write(str(cb) + "\n")
        fdet.write(accnt + "\n")
        fdet.write(name + "\n")

    with open(str(accnt) + "-rec.txt", 'a+') as frec:
        frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S] ", gmtime())) + "  " + str(amti) + "     " + str(cb) + "\n")

    messagebox.showinfo("Operation successful!!", "Amount Credited successfully!!")
    master.destroy()
    master.mainloop()
    return


# logic to debit the amount
def debit_write(master, amt, accnt, name):
    if (is_number(amt)<=0 or float(amt) <=0):
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        master.mainloop()
        return

    fdet = open(accnt + ".txt", 'r')
    pin = fdet.readline()
    camt = int(fdet.readline())
    fdet.close()
    if (int(amt) > camt):
        messagebox.showinfo("Error!!", "You dont have that amount left in your account\nPlease try again.")
    else:
        amti = int(amt)
        cb = camt - amti
        fdet = open(accnt + ".txt", 'w')
        fdet.write(pin)
        fdet.write(str(cb) + "\n")
        fdet.write(accnt + "\n")
        fdet.write(name + "\n")
        fdet.close()
        frec = open(str(accnt) + "-rec.txt", 'a+')
        frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + "     " + "              " + str(
            amti) + "              " + str(cb) + "\n")
        frec.close()
        messagebox.showinfo("Operation Successfull!!", "Amount Debited Successfully!!")
        master.destroy()
        master.mainloop()



# Function to display Credit Amount window:

def Cr_Amt(accnt, name):
    creditwn = tk.Toplevel()
    creditwn.geometry("600x300")
    creditwn.title("Credit Amount")
    creditwn.configure(bg="SteelBlue1")

    fr1 = tk.Frame(creditwn, bg="blue")
    l_title = tk.Message(creditwn, text="BANK MANAGEMENT SYSTEM", relief="raised", width=2000, padx=600, pady=0,
                         fg="white", bg="blue4", justify="center", anchor="center")
    l_title.config(font=("Arial", "50", "bold"))
    l_title.pack(side="top")

    l1 = tk.Label(creditwn, relief="raised", font=("Times", 16), text="Enter Amount to be credited: ")
    e1 = tk.Entry(creditwn, relief="raised")
    l1.pack(side="top")
    e1.pack(side="top")

    b = tk.Button(creditwn, text="Credit", font=("Times", 16), relief="raised",
                  command=lambda: cedt_write(creditwn, e1.get(), accnt, name))
    b.pack(side="top")

    creditwn.bind("<Return>", lambda x: cedt_write(creditwn, e1.get(), accnt, name))



# Trigger the credit window
#Cr_Amt(63710056780, "Anita")


def De_Amt(accnt, name):
    debitwn = tk.Toplevel()
    debitwn.geometry("600x300")
    debitwn.title("Debit Amount")
    debitwn.configure(bg="SteelBlue1")
    fr1 = tk.Frame(debitwn, bg="blue")
    l_title = tk.Message(debitwn, text="BANK MANAGEMENT SYSTEM", relief="raised", width=2000, padx=600, pady=0,
                         fg="white", bg="blue4", justify="center", anchor="center")
    l_title.config(font=("Arial", "50", "bold"))
    l_title.pack(side="top")
    l1 = tk.Label(debitwn, relief="raised", font=("Times", 16), text="Enter Amount to be debited: ")
    e1 = tk.Entry(debitwn, relief="raised")
    l1.pack(side="top")
    e1.pack(side="top")
    b = tk.Button(debitwn, text="Debit", font=("Times", 16), relief="raised",
                  command=lambda: debit_write(debitwn, e1.get(), accnt, name))
    b.pack(side="top")
    debitwn.bind("<Return>", lambda x: debit_write(debitwn, e1.get(), accnt, name))



#Function to display Balance:
def disp_bal(accnt):
    fdet = open(accnt + ".txt", 'r')
    fdet.readline()
    bal = fdet.readline()
    fdet.close()
    messagebox.showinfo("Balance", bal)


# Call the disp_bal function outside of the except block
#accnt_number_to_check = "63710056780"
# disp_bal(accnt_number_to_check)



#Function to display Transaction History window:
def disp_tr_hist(accnt):
    disp_wn = tk.Toplevel()
    disp_wn.geometry("900x600")
    disp_wn.title("Transaction History")
    disp_wn.configure(bg="SteelBlue1")

    fr1 = tk.Frame(disp_wn, bg="blue")
    fr1.pack(side="top")

    l_title = tk.Message(disp_wn, text="BANK MANAGEMENT SYSTEM", relief="raised", width=2000, padx=600, pady=0,
                         fg="white", bg="blue4", justify="center", anchor="center")
    l_title.config(font=("Arial", "50", "bold"))
    l_title.pack(side="top")

    l1 = tk.Message(disp_wn, text="Your Transaction History:", font=("Times", 16), padx=100, pady=20, width=1000,
                    bg="blue4", fg="SteelBlue1", relief="raised")
    l1.pack(side="top")

    # Open the transaction history file for reading
    frec = open(accnt + "-rec.txt", 'r')

    # Labels for Date, Credit, Debit, and Balance
    label_frame = tk.Frame(disp_wn)
    label_frame.pack(side="top")

    date_label = tk.Label(label_frame, text="Date", font=("Times", 12))
    date_label.grid(row=0, column=0, padx=15)

    credit_label = tk.Label(label_frame, text="Credit", font=("Times", 12))
    credit_label.grid(row=0, column=1, padx=20)  # Adjusted width for better alignment

    debit_label = tk.Label(label_frame, text="Debit", font=("Times", 12))
    debit_label.grid(row=0, column=2, padx=20)  # Adjusted width for better alignment

    balance_label = tk.Label(label_frame, text="Balance", font=("Times", 12))
    balance_label.grid(row=0, column=3, padx=30)  # Adjusted width for better alignment

    for line in frec:
        # Split the line into components
        components = line.split()

        # Create a Message widget for each line
        l = tk.Message(disp_wn, anchor="w", text=line, relief="ridge", width=4000)
        l.pack(side="top")

    b = tk.Button(disp_wn, text="Quit", relief="raised", command=disp_wn.destroy)
    b.pack(side="top")

    frec.close()
    #disp_wn.mainloop()


# Test the function with a specific account number
#accnt_number_to_check = "63710056780"
# disp_tr_hist(accnt_number_to_check)



#Function to handle Login and Logout:
def logout(master):
    messagebox.showinfo("Logged Out", "You Have Been Successfully Logged Out!!")
    master.destroy()
    Main_Menu()

def check_log_in(master, name, acc_num, pin):
    try:
        if check_acc_nmb(acc_num) == 0:
            master.destroy()
            Main_Menu()
            return

        if is_number(name) or is_number(pin) == 0:
            messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
            master.destroy()
            Main_Menu()
        else:
            master.destroy()
            master.after(100, lambda: logged_in_menu(acc_num, name))
    except Exception as e:
        print(f"An error occurred: {e}")




#Function to display Logged In Menu:
def logged_in_menu(accnt, name):
    rootwn = tk.Toplevel()
    rootwn.geometry("1600x500")
    rootwn.title("CopyAssignment Bank | Welcome - " + name)
    rootwn.configure(background='SteelBlue1')

    fr1 = tk.Frame(rootwn)
    fr1.pack(side="top")

    l_title = tk.Message(rootwn, text="BANK MANAGEMENT SYSTEM", relief="raised", width=2000, padx=600, pady=0,
                         fg="white", bg="blue4", justify="center", anchor="center")
    l_title.config(font=("Arial", "50", "bold"))
    l_title.pack(side="top")

    label = tk.Label(rootwn, text="Logged in as: " + name, relief="raised", bg="blue3", font=("Times", 16), fg="white",
                     anchor="center", justify="center")
    label.pack(side="top")

    img2 = tk.PhotoImage(file="images/credit (2).gif")
    myimg2 = img2.subsample(2, 2)

    img3 = tk.PhotoImage(file="images/debit.gif")
    myimg3 = img3.subsample(2, 2)

    img4 = tk.PhotoImage(file="images/balance1.gif")
    myimg4 = img4.subsample(2, 2)

    img5 = tk.PhotoImage(file="images/transaction-1 (1).gif")
    myimg5 = img5.subsample(2, 2)

    b2 = tk.Button(rootwn, image=myimg2, command=lambda: Cr_Amt(accnt, name))
    b2.image = myimg2

    b3 = tk.Button(rootwn, image=myimg3, command=lambda: De_Amt(accnt, name))
    b3.image = myimg3

    b4 = tk.Button(rootwn, image=myimg4, command=lambda: disp_bal(accnt))
    b4.image = myimg4

    b5 = tk.Button(rootwn, image=myimg5, command=lambda: disp_tr_hist(accnt))
    b5.image = myimg5

    img6 = tk.PhotoImage(file="images/logout-1.gif")
    myimg6 = img6.subsample(2, 2)

    b6 = tk.Button(rootwn, image=myimg6, relief="raised", command=lambda: logout(rootwn))
    b6.image = myimg6

    b2.place(x=100, y=150)
    b3.place(x=100, y=220)
    b4.place(x=900, y=150)
    b5.place(x=900, y=220)
    b6.place(x=500, y=400)

    #rootwn.mainloop()


# Test the function with a specific account number
#accnt_number_to_check = "63710056789"
#logged_in_menu(accnt_number_to_check, "John Doe")





# Function to display Login window:

def log_in(master):
    def check_and_login():
        check_log_in(loginwn, e1.get().strip(), e2.get().strip(), e3.get().strip())

    master.withdraw()

    loginwn = tk.Toplevel(master)
    loginwn.geometry("600x300")
    loginwn.title("Log in")
    loginwn.configure(bg="SteelBlue1")

    l_title = tk.Message(loginwn, text="BANK MANAGEMENT SYSTEM", relief="raised", width=2000, padx=600, pady=0,
                         fg="white", bg="blue4", justify="center", anchor="center")
    l_title.config(font=("Arial", "50", "bold"))
    l_title.pack(side="top")

    l1 = tk.Label(loginwn, text="Enter Name:", font=("Times", 16), relief="raised")
    l1.pack(side="top")
    e1 = tk.Entry(loginwn)
    e1.pack(side="top")

    l2 = tk.Label(loginwn, text="Enter account number:", font=("Times", 16), relief="raised")
    l2.pack(side="top")
    e2 = tk.Entry(loginwn)
    e2.pack(side="top")

    l3 = tk.Label(loginwn, text="Enter your PIN:", font=("Times", 16), relief="raised")
    l3.pack(side="top")
    e3 = tk.Entry(loginwn, show="*")
    e3.pack(side="top")

    b = tk.Button(loginwn, text="Submit", command=check_and_login)
    b.pack(side="top")

    b1 = tk.Button(loginwn, text="HOME", font=("Times", 16), relief="raised", bg="blue4", fg="white",
                   command=lambda: home_return(loginwn))
    b1.pack(side="top")



    loginwn.bind("<Return>", lambda x: check_and_login())

    # Start the login window's event loop
    loginwn.mainloop()

# Example usage
# root = tk.Tk()
# log_in(root)


#Logic to generate account Number

import random

def create_account(crwn, name, credit, pin):
    if (is_number(name)) or (is_number(credit) == 0) or (is_number(pin) == 0) or name == "":
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        crwn.withdraw()
        return

    # Generate a random account number
    accnt_no = random.randint(1000000000, 9999999999)

    # Check if the file with the generated account number already exists
    while os.path.exists(f"{accnt_no}.txt"):
        accnt_no = random.randint(1000000000, 9999999999)

    # Write account details to a new file
    with open(f"{accnt_no}.txt", 'w') as fdet:
        fdet.write(pin + "\n")
        fdet.write(credit + "\n")
        fdet.write(str(accnt_no) + "\n")
        fdet.write(name + "\n")

    with open(f"{accnt_no}-rec.txt", 'w') as frec:
        frec.write("Date        credit   Debit   Balance\n")
        frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S] ", gmtime())) + "    " + credit + "     " + credit + "\n")

    messagebox.showinfo("Details", f"Your account number is: {accnt_no}")
    crwn.withdraw()




#Function to display Create New Account window:

def write(crwn, name, credit, pin):
    # Implement your account creation logic here
    # For example, you can write the account details to a file
    with open("account_data.txt", "a") as file:
        file.write(f"Name: {name}, Credit: {credit}, PIN: {pin}\n")

    # Destroy the current window (account creation window)
    crwn.destroy()

def Create():
    crwn = tk.Toplevel()
    crwn.geometry("600x300")
    crwn.title("Create Account")
    crwn.configure(bg="SteelBlue1")

    fr1 = tk.Frame(crwn, bg="blue")
    l_title = tk.Message(crwn, text="BANK MANAGEMENT SYSTEM", relief="raised", width=2000, padx=600, pady=0, fg="white",
                         bg="blue4", justify="center", anchor="center")
    l_title.config(font=("Arial", "50", "bold"))
    l_title.pack(side="top")

    l1 = tk.Label(crwn, text="Enter Name:", font=("Times", 16), relief="raised")
    l1.pack(side="top")
    e1 = tk.Entry(crwn)
    e1.pack(side="top")

    l2 = tk.Label(crwn, text="Enter opening credit:", font=("Times", 16), relief="raised")
    l2.pack(side="top")
    e2 = tk.Entry(crwn)
    e2.pack(side="top")

    l3 = tk.Label(crwn, text="Enter desired PIN:", font=("Times", 16), relief="raised")
    l3.pack(side="top")
    e3 = tk.Entry(crwn, show="*")
    e3.pack(side="top")

    b = tk.Button(crwn, text="Submit", font=("Times", 16),
                  command=lambda: create_account(crwn, e1.get().strip(), e2.get().strip(), e3.get().strip()))
    b.pack(side="top")

    crwn.bind("<Return>", lambda x: create_account(crwn, e1.get().strip(), e2.get().strip(), e3.get().strip()))
    return
    #crwn.mainloop()

# Test the function
#Create()


#Function to display Main Menu window & call to Main_Menu():

def Main_Menu():
    rootwn = tk.Tk()
    rootwn.geometry("1600x500")
    rootwn.title("Bank Management System - CopyAssignment")
    rootwn.configure(background='SteelBlue1')

    fr1 = tk.Frame(rootwn)
    fr1.pack(side="top")

    l_title = tk.Message(text="BANK MANAGEMENT SYSTEM ", relief="raised", width=2000, padx=600, pady=0, fg="white",
                         bg="blue4", justify="center", anchor="center")
    l_title.config(font=("Verdana", "40", "bold"))
    l_title.pack(side="top")

    imgc1 = tk.PhotoImage(file="images/new-1.gif")
    imglo = tk.PhotoImage(file="images/login (3).gif")
    imgc = imgc1.subsample(2, 2)
    imglog = imglo.subsample(2, 2)

    b1 = tk.Button(image=imgc, command=Create)
    b1.image = imgc
    b2 = tk.Button(image=imglog, command=lambda: log_in(rootwn))
    b2.image = imglog

    

    b1.place(x=800, y=300)
    b2.place(x=800, y=200)

    img6 = tk.PhotoImage(file="images/quit-1 (1).gif")
    myimg6 = img6.subsample(2, 2)

    b6 = tk.Button(image=myimg6, command=rootwn.destroy)
    b6.image = myimg6
    b6.place(x=920, y=400)

    rootwn.mainloop()

Main_Menu()
