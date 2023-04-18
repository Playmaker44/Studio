# dictionary
from tkinter import *
from tkinter import ttk
import random  # Contains functions for generating  random numbers, random selections from sequences & other random - related operations
import tkinter.messagebox
import datetime
import time
import tkinter.ttk as tkrtk
import tkinter as tkr
import pymysql


# studio management system


class Studio:
    # method "init" which initializes the root window and creates a notebook with two tabs, one for the studio system and the other for client details.
    # It initializes all the instance variables to empty strings.
    def __init__(self, root):
        self.root = root
        self.root.title("Studio Management System")
        self.root.geometry("1350x800+0+0")

        notebook = ttk.Notebook(self.root)
        self.TabControl1 = ttk.Frame(notebook)
        self.TabControl2 = ttk.Frame(notebook)
        notebook.add(self.TabControl1, text="Studio System")
        notebook.add(self.TabControl2, text="Clients Details")

        notebook.grid()

       # =====================variables=======================
# store various pieces of information related to the studio management system
# such as customer information, photographer information, studio information, and equipment information.
#
        self.CustomerNumber = StringVar()
        self.CustomerName = StringVar()
        self.CustomerSurname = StringVar()
        self.CustomerAddress = StringVar()
        self.CustomerMobile = StringVar()
        self.CustomerEmail = StringVar()
        self.CustomerIDNumber = StringVar()
        self.CustomerGender = StringVar()
        self.CustomerDOB = StringVar()

        self.PhotoGrapherRent = StringVar()
        self.FirstName = StringVar()
        self.Surname = StringVar()
        self.ID = StringVar()
        self.Mobile = StringVar()
        self.WorkPhone = StringVar()
        self.Email = StringVar()

        self.StudioType = StringVar()
        self.StudioRoomNumber = StringVar()
        self.StudioPrice = StringVar()
        self.StudioDate = StringVar()
        self.StudioDuration = StringVar()
        self.StudioName = StringVar()
        self.StudioDeposit = StringVar()
        self.StudioPaymentMethod = StringVar()
        self.StudioSpecialDiscount = StringVar()
        self.StudioNote = StringVar()

        self.CheckInTime = StringVar()
        self.CheckOutTime = StringVar()

        self.LightingEquiqments = StringVar()
        self.BackDrops = StringVar()
        self.GreenScreen = StringVar()
        self.AudioEquiqments = StringVar()
        self.Funitures = StringVar()
        self.WIFI = StringVar()
        self.Tripods = StringVar()
        self.Projectors = StringVar()
        self.Decorations = StringVar()
        self.Aircondioner = StringVar()
        self.VideoMonitors = StringVar()
        self.Cosmetics = StringVar()
        self.Cameras = StringVar()
        self.Clothes = StringVar()
        self.Props = StringVar()
        self.StudioAccessories = StringVar()


# =====================frame=======================
# organize the different sections of the user interface and control their placement on the screen.

        MainFrame = Frame(self.TabControl1, bd=10,
                          width=1350, height=700, relief=RIDGE)
        MainFrame.grid(padx=5, pady=10)

        Tab2Frame = Frame(self.TabControl2, bd=10,
                          width=1350, height=700, relief=RIDGE)
        Tab2Frame.grid(padx=10)

        TopFrame3 = Frame(MainFrame, bd=10, width=1340,
                          height=500, relief=RIDGE)
        TopFrame3.grid()

        RightFrame1 = Frame(TopFrame3, bd=5, width=320,
                            height=400, padx=2, bg="cadetblue", relief=RIDGE)
        RightFrame1.pack(side=RIGHT, pady=1)
        ItemsFrame = Frame(RightFrame1, bd=5, width=320,
                           height=300, padx=2, relief=RIDGE)
        ItemsFrame.pack(side=TOP, pady=2)

        LeftFrame = Frame(TopFrame3, bd=5, width=1340,
                          height=400, padx=2, bg="cadetblue", relief=RIDGE)
        LeftFrame.pack(side=RIGHT)
        StudioFrame = Frame(LeftFrame, bd=5, width=600,
                            height=180, padx=4, relief=RIDGE)
        StudioFrame.pack(side=TOP)

        LeftFrame2 = Frame(LeftFrame, bd=5, width=600,
                           height=180, padx=2, bg="cadetblue", relief=RIDGE)
        LeftFrame2.pack(side=TOP)
        ClientStatusFrame = Frame(
            LeftFrame2, bd=5, width=300, height=170, padx=2, relief=RIDGE)
        ClientStatusFrame.pack(side=LEFT)
        TimeFrame = Frame(LeftFrame2, bd=5, width=300,
                          height=170, padx=2, relief=RIDGE)
        TimeFrame.pack(side=RIGHT)

        ButtonFrame = Frame(LeftFrame, bd=5, width=320,
                            height=50, padx=4, relief=RIDGE)
        ButtonFrame.pack(side=LEFT)

        RightFrame2 = Frame(TopFrame3, bd=5, width=300,
                            height=400, padx=2, bg="cadetblue", relief=RIDGE)
        RightFrame2.pack(side=LEFT, pady=5)

# The frame for the client details tab contains two sub-frames, ClientFrame and PhotoGrapherFrame.
        ClientFrame = Frame(RightFrame2, bd=5, width=280,
                            height=50, padx=2, bg="cadetblue", relief=RIDGE)
        ClientFrame.pack(side=TOP)
        PhotoGrapherFrame = Frame(
            RightFrame2, bd=5, width=280, height=50, padx=3, relief=RIDGE)
        PhotoGrapherFrame.pack(side=TOP)


# =====================Functions=== Exit====================
# when the user clicks on the exit or reset buttons

        def iExit():
            # called when the user clicks the "Exit" button.

            iExit = tkinter.messagebox.askyesno(
                "Studio Management System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                # If the user clicks "Yes", then root.destroy() is called to destroy the main window and end the program.
                # If the user clicks "No", nothing happens and the function returns.
                return


# =====================Functions=== Reset====================

        def iReset():
            # used to clear all the fields in the GUI. This function resets all the variables in the GUI to empty strings, which clears all the data entered into the fields.
            # The function is called when the "Reset" button is clicked in the GUI.
            self.CustomerNumber.set("")
# 'self' prefix before the variable names indicates that these are instance variables of the class. They are used to store the values of the fields in the GUI
            self.CustomerName.set("")
            self.CustomerSurname.set("")
            self.CustomerAddress.set("")
            self.CustomerMobile.set("")
            self.CustomerEmail.set("")
            self.CustomerIDNumber.set("")
            self.CustomerGender.set("")
            self.CustomerDOB.set("")

            self.PhotoGrapherRent.set("")
            self.FirstName.set("")
            self.Surname.set("")
            self.ID.set("")
            self.Mobile.set("")
            self.WorkPhone.set("")
            self.Email.set("")

            self.StudioType.set("")
            self.StudioRoomNumber.set("")
            self.StudioPrice.set("")
            self.StudioDate.set("")
            self.StudioDuration.set("")
            self.StudioName.set("")
            self.StudioDeposit.set("")
            self.StudioPaymentMethod.set("")
            self.StudioSpecialDiscount.set("")
            self.StudioNote.set("")

            self.CheckInTime.set("")
            self.CheckOutTime.set("")

            self.LightingEquiqments.set("")
            self.BackDrops.set("")
            self.GreenScreen.set("")
            self.AudioEquiqments.set("")
            self.Funitures.set("")
            self.WIFI.set("")
            self.Tripods.set("")
            self.Projectors.set("")
            self.Decorations.set("")
            self.Aircondioner.set("")
            self.VideoMonitors.set("")
            self.Cosmetics.set("")
            self.Cameras.set("")
            self.Clothes.set("")
            self.Props.set("")
            self.StudioAccessories.set("")


# =====================Studio Data====================

        def StudioData(event):
            # This code defines a function called StudioData that is triggered when an event (presumably a selection of a studio type) occurs.
            # It checks the value of the StudioType variable and sets various attributes accordingly.
            if self.StudioType.get() == 'Portrait':
                self.StudioName.set("Portrait Studio")
                self.StudioRoomNumber.set("1")
                self.StudioDuration.set("1 Hour")
                self.StudioPrice.set(" 600 USD")
                self.StudioDeposit.set(" 1000 USD")
                self.StudioPaymentMethod.set("Cash")
                self.StudioSpecialDiscount.set("10%")
                self.StudioNote.set("No Note")
            if self.StudioType.get() == 'Fashion':
                self.StudioName.set("Fashion Studio")
                self.StudioRoomNumber.set("2")
                self.StudioDuration.set("1 Hour")
                self.StudioPrice.set("200 USD")
                self.StudioDeposit.set(" 850 USD ")
                self.StudioPaymentMethod.set("Cash")
                self.StudioSpecialDiscount.set("10%")
                self.StudioNote.set("No Note")
            if self.StudioType.get() == 'Wedding':
                self.StudioName.set("Wedding Studio")
                self.StudioRoomNumber.set("3")
                self.StudioDuration.set("1 Hour")
                self.StudioPrice.set("450 USD")
                self.StudioDeposit.set("650 USD")
                self.StudioPaymentMethod.set("Cash")
                self.StudioSpecialDiscount.set("10%")
                self.StudioNote.set("No Note")
            if self.StudioType.get() == 'Product':
                self.StudioName.set("Product Studio")
                self.StudioRoomNumber.set("4")
                self.StudioDuration.set("1 Hour")
                self.StudioPrice.set("500 USD")
                self.StudioDeposit.set("1000 USD")
                self.StudioPaymentMethod.set("Cash")
                self.StudioSpecialDiscount.set("10%")
                self.StudioNote.set("No Note")
            if self.StudioType.get() == 'Music Video':
                self.StudioName.set("Music Video Studio")
                self.StudioRoomNumber.set("5")
                self.StudioDuration.set("1 Hour")
                self.StudioPrice.set("350 USD")
                self.StudioDeposit.set("700 USD")
                self.StudioPaymentMethod.set("Cash")
                self.StudioSpecialDiscount.set("10%")
                self.StudioNote.set("No Note")
            if self.StudioType.get() == 'Landscape':
                self.StudioName.set("Landscape Studio")
                self.StudioRoomNumber.set("6")
                self.StudioDuration.set("1 Hour")
                self.StudioPrice.set("350 USD")
                self.StudioDeposit.set("800 USD")
                self.StudioPaymentMethod.set("Cash")
                self.StudioSpecialDiscount.set("10%")
                self.StudioNote.set("No Note")
            if self.StudioType.get() == 'Sports':
                self.StudioName.set("Sports Studio")
                self.StudioRoomNumber.set("7")
                self.StudioDuration.set("1 Hour")
                self.StudioPrice.set("650 USD")
                self.StudioDeposit.set("1000 USD")
                self.StudioPaymentMethod.set("Cash")
                self.StudioSpecialDiscount.set("10%")
                self.StudioNote.set("No Note")
            if self.StudioType.get() == 'Editorial':
                self.StudioName.set("Editorial Studio")
                self.StudioRoomNumber.set("8")
                self.StudioDuration.set("1 Hour")
                self.StudioPrice.set("550 USD")
                self.StudioDeposit.set("1000 USD")
                self.StudioPaymentMethod.set("Cash")
                self.StudioSpecialDiscount.set("10%")
                self.StudioNote.set("Studio is under maintainance")
# purpose of this function is likely to provide default values for the studio booking based on the selected studio type.
# The specific values that are set may not be accurate or useful in practice, and it would be better to base them on real data or user input.
# the repetition of code for each possible studio type could be improved by using a data structure  to map each studio type to its corresponding values.


# =====================MySQL Database Connection====================


        def addData():
            # inserts data into a MySQL database table named "studio". The function first checks if all the required fields are filled in.
            # If all the fields are filled, the function establishes a connection with the MySQL server using the pymysql module and inserts the data into the "studio"
            # table using a SQL INSERT statement
            if self.CustomerNumber.get() == "" or self.CustomerName.get() == "" or self.CustomerSurname.get() == "":
                tkinter.messagebox.showerror(
                    "Booking System", "Please fill in all the fields")
            else:
                sqlcon = pymysql.connect(
                    host="localhost", user="root", password="260103s1X", database="studio")
                cur = sqlcon.cursor()
                cur.execute("insert into studio values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.CustomerNumber.get(),
                    self.CustomerName.get(),
                    self.CustomerSurname.get(),
                    self.CustomerAddress.get(),
                    self.CustomerIDNumber.get(),
                    self.CustomerMobile.get(),
                    self.CustomerEmail.get(),
                    self.CustomerGender.get(),
                    self.CustomerDOB.get(),

                    self.PhotoGrapherRent.get(),
                    self.FirstName.get(),
                    self.Surname.get(),
                    self.ID.get(),
                    self.Mobile.get(),
                    self.Email.get(),
                    self.WorkPhone.get(),

                    self.StudioType.get(),
                    self.StudioName.get(),
                    self.StudioRoomNumber.get(),
                    self.StudioDuration.get(),
                    self.StudioPrice.get(),
                    self.StudioDeposit.get(),
                    self.StudioPaymentMethod.get(),
                    self.StudioSpecialDiscount.get(),
                    self.StudioNote.get(),

                    self.CheckInTime.get(),
                    self.CheckOutTime.get(),

                    self.LightingEquiqments.get(),
                    self.BackDrops.get(),
                    self.GreenScreen.get(),
                    self.AudioEquiqments.get(),
                    self.Cameras.get(),
                    self.Funitures.get(),
                    self.StudioAccessories.get(),
                    self.WIFI.get(),
                    self.Tripods.get(),
                    self.Projectors.get(),
                    self.Decorations.get(),
                    self.Aircondioner.get(),
                    self.VideoMonitors.get(),
                    self.Cosmetics.get(),
                    self.Clothes.get(),
                    self.Props.get(),
                ))
                sqlcon.commit()
# called to save the changes to the database
                DisplayData()
# called to display the updated data on the GUI.
#  Finally, the function closes the database connection and displays a message box to inform the user that the data has been saved successfully.
                sqlcon.close()
                tkinter.messagebox.showinfo(
                    "Booking System", "Data has been saved successfully")


# =====================Display Data=======================

        def DisplayData():
            # used to display the data stored in a MySQL database table named 'studio'.
            sqlcon = pymysql.connect(
                host="localhost", user="root", password="260103s1X", database="studio")
# takes as arguments the hostname, username, password, database name...
            cur = sqlcon.cursor()
            # creates a cursor object to execute SQL queries against the database.
            cur.execute("select * from studio")
            # cursor executes a "SELECT *" query on the "studio" table, which retrieves all rows and columns from the table.
            result = cur.fetchall()
            # called on the cursor object to fetch all rows returned by the query.
            if len(result) != 0:
                self.StudioTable.delete(*self.StudioTable.get_children())
                for row in result:
                    self.StudioTable.insert('', END, values=row)
                sqlcon.commit()
            sqlcon.close()


# =======================Delete Button=======================

        def DeleteData():
            # delete data from the studio table in a MySQL database.
            sqlcon = pymysql.connect(
                host="localhost", user="root", password="260103s1X", database="studio")
            cur = sqlcon.cursor()
            cur.execute("delete from studio where CustomerNumber=%s",
                        self.CustomerNumber.get())  # tuple
            # delete a row from the studio table where the CustomerNumber field matches the value obtained from self.CustomerNumber.get().
            # This value is passed as a parameter to the execute() method as a tuple.
            sqlcon.commit()
            DisplayData()
            # update the table in the GUI to reflect the changes
            sqlcon.close()
            tkinter.messagebox.showinfo(
                "Booking System", "Data has been deleted successfully")
            # displays a message box informing the user that the data has been deleted successfully
            iReset()
            # reset input fields in the GUI

# =======================Booking Information=======================
        def bookingInfo(ev):
            # populate the entry fields of a GUI form with the details of a selected booking when the user clicks on a row of the booking table.
            viewInfo = self.StudioTable.focus()
            # get the currently selected row in the StudioTable
            learnerInfo = self.StudioTable.item(viewInfo)
            # retrieve all the values in that row and store them in the row variable
            row = learnerInfo['values']

            self.CustomerNumber.set(row[0])
            # set the values of variou
            self.CustomerName.set(row[1])
            self.CustomerSurname.set(row[2])
            self.CustomerIDNumber.set(row[3])
            self.CustomerAddress.set(row[4])
            self.CustomerMobile.set(row[5])
            self.CustomerEmail.set(row[6])
            self.CustomerGender.set(row[7])
            self.CustomerDOB.set(row[8])

            self.PhotoGrapherRent.set(row[9])
            self.FirstName.set(row[10])
            self.Surname.set(row[11])
            self.ID.set(row[12])
            self.Mobile.set(row[13])
            self.Email.set(row[14])
            self.WorkPhone.set(row[15])

            self.StudioType.set(row[16])
            self.StudioName.set(row[17])
            self.StudioRoomNumber.set(row[18])
            self.StudioDuration.set(row[19])
            self.StudioPrice.set(row[20])
            self.StudioDeposit.set(row[21])
            self.StudioPaymentMethod.set(row[22])
            self.StudioSpecialDiscount.set(row[23])
            self.StudioNote.set(row[24])

            self.CheckInTime.set(row[25])
            self.CheckOutTime.set(row[26])

            self.LightingEquiqments.set(row[27])
            self.BackDrops.set(row[28])
            self.GreenScreen.set(row[29])
            self.AudioEquiqments.set(row[30])
            self.Cameras.set(row[31])
            self.Funitures.set(row[32])
            self.StudioAccessories.set(row[33])
            self.WIFI.set(row[34])
            self.Tripods.set(row[35])
            self.Projectors.set(row[36])
            self.Decorations.set(row[37])
            self.Aircondioner.set(row[38])
            self.VideoMonitors.set(row[39])
            self.Cosmetics.set(row[40])
            self.Clothes.set(row[41])
            self.Props.set(row[42])


# =======================Update Button=======================

        def UpdateData():
            # updates an existing record in the studio table of a MySQL database
            sqlcon = pymysql.connect(
                host="localhost", user="root", password="260103s1X", database="studio")
            # connecting to the database
            cur = sqlcon.cursor()
            # creating a cursor object to execute SQL statements
            cur.execute("update studio set firstname=%s,surname=%s,idnumber=%s,address=%s,mobile=%s,email=%s,gender=%s,dob=%s,\
                        photographer=%s,pname=%s,psurname=%s,pid=%s,pmobile=%s,pemail=%s,pworkphone=%s,\
                        stype=%s,sname=%s,sroomno=%s,sduration=%s,sprice=%s,sdeposit=%s,smethod=%s,sdiscount=%s,snotes=%s,\
                        checkin=%s,checkout=%s,\
                        lighting=%s,sound=%s,backdrops=%s,cameras=%s,tripods=%s,funiture=%s,projectors=%s,wifi=%s,green=%s,cosmetics=%s,decorations=%s,clothes=%s,props=%s,air=%s,monitors=%s,accessories=%s where customernumber=%s", (
                # executes an SQL UPDATE statement
                self.CustomerName.get(),
                self.CustomerSurname.get(),
                self.CustomerIDNumber.get(),
                self.CustomerAddress.get(),
                self.CustomerMobile.get(),
                self.CustomerEmail.get(),
                self.CustomerGender.get(),
                self.CustomerDOB.get(),

                self.PhotoGrapherRent.get(),
                self.FirstName.get(),
                self.Surname.get(),
                self.ID.get(),
                self.Mobile.get(),
                self.Email.get(),
                self.WorkPhone.get(),

                self.StudioType.get(),
                self.StudioName.get(),
                self.StudioRoomNumber.get(),
                self.StudioDuration.get(),
                self.StudioPrice.get(),
                self.StudioDeposit.get(),
                self.StudioPaymentMethod.get(),
                self.StudioSpecialDiscount.get(),
                self.StudioNote.get(),

                self.CheckInTime.get(),
                self.CheckOutTime.get(),

                self.LightingEquiqments.get(),
                self.BackDrops.get(),
                self.GreenScreen.get(),
                self.AudioEquiqments.get(),
                self.Cameras.get(),
                self.Funitures.get(),
                self.StudioAccessories.get(),
                self.WIFI.get(),
                self.Tripods.get(),
                self.Projectors.get(),
                self.Decorations.get(),
                self.Aircondioner.get(),
                self.VideoMonitors.get(),
                self.Cosmetics.get(),
                self.Clothes.get(),
                self.Props.get(),
                self.CustomerNumber.get()
            ))
            sqlcon.commit()
            sqlcon.close()
            tkinter.messagebox.showinfo(
                "Studio Management System", "Successfully Updated")

# =====================Customer widget=======================

        self.lblCustomerNumber = Label(ClientFrame, font=(
            'arial', 12, 'bold'), text="Customer Number", bd=7, anchor='w', justify=LEFT)
        self.lblCustomerNumber.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtCustomerNumber = Entry(ClientFrame, font=(
            'arial', 12, 'bold'), textvariable=self.CustomerNumber, bd=5, width=25)
        self.txtCustomerNumber.grid(row=0, column=1)

        self.lblCustomerName = Label(ClientFrame, font=(
            'arial', 12, 'bold'), text="Customer Name", bd=7, anchor='w', justify=LEFT)
        self.lblCustomerName.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtCustomerName = Entry(ClientFrame, font=(
            'arial', 12, 'bold'), textvariable=self.CustomerName, bd=5, width=25)
        self.txtCustomerName.grid(row=1, column=1)

        self.lblCustomerSurname = Label(ClientFrame, font=(
            'arial', 12, 'bold'), text="Customer Surname", bd=7, anchor='w', justify=LEFT)
        self.lblCustomerSurname.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtCustomerSurname = Entry(ClientFrame, font=(
            'arial', 12, 'bold'), textvariable=self.CustomerSurname, bd=5, width=25)
        self.txtCustomerSurname.grid(row=2, column=1)

        self.lblCustomerAddress = Label(ClientFrame, font=(
            'arial', 12, 'bold'), text="Customer Address", bd=7, anchor='w', justify=LEFT)
        self.lblCustomerAddress.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtCustomerAddress = Entry(ClientFrame, font=(
            'arial', 12, 'bold'), textvariable=self.CustomerAddress, bd=5, width=25)
        self.txtCustomerAddress.grid(row=3, column=1)

        self.lblCustomerMobile = Label(ClientFrame, font=(
            'arial', 12, 'bold'), text="Customer Mobile", bd=7, anchor='w', justify=LEFT)
        self.lblCustomerMobile.grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txtCustomerMobile = Entry(ClientFrame, font=(
            'arial', 12, 'bold'), textvariable=self.CustomerMobile, bd=5, width=25)
        self.txtCustomerMobile.grid(row=4, column=1)

        self.lblCustomerEmail = Label(ClientFrame, font=(
            'arial', 12, 'bold'), text="Customer Email", bd=7, anchor='w', justify=LEFT)
        self.lblCustomerEmail.grid(row=5, column=0, sticky=W, padx=5, pady=5)
        self.txtCustomerEmail = Entry(ClientFrame, font=(
            'arial', 12, 'bold'), textvariable=self.CustomerEmail, bd=5, width=25)
        self.txtCustomerEmail.grid(row=5, column=1)

        self.lblCustomerIDNumber = Label(ClientFrame, font=(
            'arial', 12, 'bold'), text="Customer ID", bd=7, anchor='w', justify=LEFT)
        self.lblCustomerIDNumber.grid(
            row=6, column=0, sticky=W, padx=5, pady=5)
        self.txtCustomerIDNumber = Entry(ClientFrame, font=(
            'arial', 12, 'bold'), textvariable=self.CustomerIDNumber, bd=5, width=25)
        self.txtCustomerIDNumber.grid(row=6, column=1)

        self.lblCustomerGender = Label(ClientFrame, font=(
            'arial', 12, 'bold'), text="Customer Gender", bd=7, anchor='w', justify=LEFT)
        self.lblCustomerGender.grid(row=7, column=0, sticky=W, padx=5, pady=5)
        self.txtCustomerGender = Entry(ClientFrame, font=(
            'arial', 12, 'bold'), textvariable=self.CustomerGender, bd=5, width=25)
        self.txtCustomerGender.grid(row=7, column=1)

        self.lblCustomerDOB = Label(ClientFrame, font=(
            'arial', 12, 'bold'), text="Customer DOB", bd=7, anchor='w', justify=LEFT)
        self.lblCustomerDOB.grid(row=8, column=0, sticky=W, padx=5, pady=5)
        self.txtCustomerDOB = Entry(ClientFrame, font=(
            'arial', 12, 'bold'), textvariable=self.CustomerDOB, bd=5, width=25)
        self.txtCustomerDOB.grid(row=8, column=1)

# =====================rent widget=======================
        self.lblPhotoGrapherRent = Label(PhotoGrapherFrame, font=(
            'arial', 12, 'bold'), text="PhotoGrapher Rent", bd=7)
        self.lblPhotoGrapherRent.grid(row=0, column=0, sticky=W, padx=5)
        self.cboPhotoGrapherRent = ttk.Combobox(PhotoGrapherFrame, font=(
            'arial', 12, 'bold'), textvariable=self.PhotoGrapherRent, state='readonly', width=16)
        self.cboPhotoGrapherRent['values'] = ('', 'Yes', 'No')
        self.cboPhotoGrapherRent.current(0)
        self.cboPhotoGrapherRent.grid(row=0, column=1)

        self.lblName = Label(PhotoGrapherFrame, font=(
            'arial', 12, 'bold'), text="PhotoGrapher Name", bd=7)
        self.lblName.grid(row=1, column=0, sticky=W, padx=5)
        self.txtName = Entry(PhotoGrapherFrame, font=(
            'arial', 12, 'bold'), textvariable=self.FirstName, bd=6, width=17, justify=LEFT)
        self.txtName.grid(row=1, column=1)

        self.lblSurname = Label(PhotoGrapherFrame, font=(
            'arial', 12, 'bold'), text="Surname", bd=7)
        self.lblSurname.grid(row=2, column=0, sticky=W, padx=5)
        self.txtSurname = Entry(PhotoGrapherFrame, font=(
            'arial', 12, 'bold'), textvariable=self.Surname, bd=6, width=17, justify=LEFT)
        self.txtSurname.grid(row=2, column=1)

        self.lblID = Label(PhotoGrapherFrame, font=(
            'arial', 12, 'bold'), text="ID", bd=7)
        self.lblID.grid(row=3, column=0, sticky=W, padx=5)
        self.txtID = Entry(PhotoGrapherFrame, font=(
            'arial', 12, 'bold'), textvariable=self.ID, bd=6, width=17, justify=LEFT)
        self.txtID.grid(row=3, column=1)

        self.lblMobile = Label(PhotoGrapherFrame, font=(
            'arial', 12, 'bold'), text="Mobile", bd=7)
        self.lblMobile.grid(row=4, column=0, sticky=W, padx=5)
        self.txtMobile = Entry(PhotoGrapherFrame, font=(
            'arial', 12, 'bold'), textvariable=self.Mobile, bd=6, width=17, justify=LEFT)
        self.txtMobile.grid(row=4, column=1)

        self.lblWorkPhone = Label(PhotoGrapherFrame, font=(
            'arial', 12, 'bold'), text="Work Phone", bd=7)
        self.lblWorkPhone.grid(row=5, column=0, sticky=W, padx=5)
        self.txtWorkPhone = Entry(PhotoGrapherFrame, font=(
            'arial', 12, 'bold'), textvariable=self.WorkPhone, bd=6, width=17, justify=LEFT)
        self.txtWorkPhone.grid(row=5, column=1)

        self.lblEmail = Label(PhotoGrapherFrame, font=(
            'arial', 12, 'bold'), text="Email", bd=7)
        self.lblEmail.grid(row=6, column=0, sticky=W, padx=5)
        self.txtEmail = Entry(PhotoGrapherFrame, font=(
            'arial', 12, 'bold'), textvariable=self.Email, bd=6, width=17, justify=LEFT)
        self.txtEmail.grid(row=6, column=1, pady=3)

# =====================StudioWidgets=======================
        self.lblStudioType = Label(StudioFrame, font=(
            'arial', 12, 'bold'), text="Studio Type", bd=6)
        self.lblStudioType.grid(row=0, column=0, sticky=W)
        self.cboStudioType = ttk.Combobox(StudioFrame, font=(
            'arial', 12, 'bold'), textvariable=self.StudioType, state='readonly', width=20)
        self.cboStudioType['values'] = (
            '', 'Portrait', 'Fashion', 'Wedding', 'Product', 'Landscape', 'Sports', 'Music Video', 'Editorial')
        self.cboStudioType.current(0)
        self.cboStudioType.grid(row=0, column=1)
        self.cboStudioType.bind("<<ComboboxSelected>>", StudioData)

        self.lblStudioName = Label(StudioFrame, font=(
            'arial', 12, 'bold'), text="Studio Name", bd=7)
        self.lblStudioName.grid(row=1, column=0, sticky=W, padx=5)
        self.txtStudioName = Entry(StudioFrame, font=(
            'arial', 12, 'bold'), textvariable=self.StudioName, bd=6, width=17, justify=LEFT)
        self.txtStudioName.grid(row=1, column=1)

        self.lblStudioRoomNumber = Label(StudioFrame, font=(
            'arial', 12, 'bold'), text="Studio Room Number", bd=7)
        self.lblStudioRoomNumber.grid(row=2, column=0, sticky=W, padx=5)
        self.txtStudioRoomNumber = Entry(StudioFrame, font=(
            'arial', 12, 'bold'), textvariable=self.StudioRoomNumber, bd=6, width=17, justify=LEFT)
        self.txtStudioRoomNumber.grid(row=2, column=1)

        self.lblStudioDuration = Label(StudioFrame, font=(
            'arial', 12, 'bold'), text="Studio Duration", bd=7)
        self.lblStudioDuration.grid(row=3, column=0, sticky=W, padx=5)
        self.txtStudioDuration = Entry(StudioFrame, font=(
            'arial', 12, 'bold'), textvariable=self.StudioDuration, bd=6, width=17, justify=LEFT)
        self.txtStudioDuration.grid(row=3, column=1)

        self.lblStudioPrice = Label(StudioFrame, font=(
            'arial', 12, 'bold'), text="Studio Price", bd=7)
        self.lblStudioPrice.grid(row=4, column=0, sticky=W, padx=5)
        self.txtStudioPrice = Entry(StudioFrame, font=(
            'arial', 12, 'bold'), textvariable=self.StudioPrice, bd=6, width=17, justify=LEFT)
        self.txtStudioPrice.grid(row=4, column=1)

        self.lblStudioDeposit = Label(StudioFrame, font=(
            'arial', 12, 'bold'), text="Studio Deposit", bd=7)
        self.lblStudioDeposit.grid(row=5, column=0, sticky=W, padx=5)
        self.txtStudioDeposit = Entry(StudioFrame, font=(
            'arial', 12, 'bold'), textvariable=self.StudioDeposit, bd=6, width=17, justify=LEFT)
        self.txtStudioDeposit.grid(row=5, column=1)

        self.lblStudioPaymentMethod = Label(StudioFrame, font=(
            'arial', 12, 'bold'), text="Payment Method", bd=7)
        self.lblStudioPaymentMethod.grid(row=6, column=0, sticky=W, padx=5)
        self.cboStudioPaymentMethod = ttk.Combobox(StudioFrame, font=(
            'arial', 12, 'bold'), textvariable=self.StudioPaymentMethod, state='readonly', width=16)
        self.cboStudioPaymentMethod['values'] = (
            '', 'Cash ', 'Credit Card ', 'Debit Card ', 'Cheque ')
        self.cboStudioPaymentMethod.current(0)
        self.cboStudioPaymentMethod.grid(row=6, column=1)

        self.lblStudioSpecialDiscount = Label(StudioFrame, font=(
            'arial', 12, 'bold'), text="Special Discount", bd=7)
        self.lblStudioSpecialDiscount.grid(row=7, column=0, sticky=W, padx=5)
        self.cboStudioSpecialDiscount = ttk.Combobox(StudioFrame, font=(
            'arial', 12, 'bold'), textvariable=self.StudioSpecialDiscount, state='readonly', width=16)
        self.cboStudioSpecialDiscount['values'] = ('', 'Yes ', 'No ')
        self.cboStudioSpecialDiscount.current(0)
        self.cboStudioSpecialDiscount.grid(row=7, column=1)

        self.lblStudioNotes = Label(StudioFrame, font=(
            'arial', 12, 'bold'), text="Notes", bd=7)
        self.lblStudioNotes.grid(row=8, column=0, sticky=W, padx=5)
        self.txtStudioNotes = Entry(StudioFrame, font=(
            'arial', 12, 'bold'), textvariable=self.StudioNote, bd=6, width=17, justify=LEFT)
        self.txtStudioNotes.grid(row=8, column=1)

# =====================Checkin/CheckoutWidgets=======================
        self.lblCheckinDate = Label(ClientStatusFrame, font=(
            'arial', 12, 'bold'), text="Checkin Time", bd=10)
        self.lblCheckinDate.grid(row=0, column=0, sticky=W)
        self.txtCheckinDate = Entry(ClientStatusFrame, font=(
            'arial', 12, 'bold'), textvariable=self.CheckInTime, bd=6, width=17, justify=LEFT)
        self.txtCheckinDate.grid(row=0, column=1, pady=5)

        self.lblCheckoutDate = Label(TimeFrame, font=(
            'arial', 12, 'bold'), text="Checkout Time", bd=10)
        self.lblCheckoutDate.grid(row=0, column=0, sticky=W)
        self.txtCheckoutDate = Entry(TimeFrame, font=(
            'arial', 12, 'bold'), textvariable=self.CheckOutTime, bd=6, width=17, justify=LEFT)
        self.txtCheckoutDate.grid(row=0, column=1, pady=5)

# =====================ClientStatusWidgets=======================
        self.lblLightningEquiqments = Label(ItemsFrame, font=(
            'arial', 12, 'bold'), text="Lightning Equiqments", bd=7)
        self.lblLightningEquiqments.grid(row=0, column=0, sticky=W)
        self.cboLightningEquiqments = ttk.Combobox(ItemsFrame, font=(
            'arial', 12, 'bold'), textvariable=self.LightingEquiqments, state='readonly', width=16)
        self.cboLightningEquiqments['values'] = ('', 'Yes ', 'No ')
        self.cboLightningEquiqments.current(0)
        self.cboLightningEquiqments.grid(row=0, column=1)

        self.lblSoundEquiqments = Label(ItemsFrame, font=(
            'arial', 12, 'bold'), text="Sound Equiqments", bd=7)
        self.lblSoundEquiqments.grid(row=1, column=0, sticky=W)
        self.cboSoundEquiqments = ttk.Combobox(ItemsFrame, font=(
            'arial', 12, 'bold'), textvariable=self.AudioEquiqments, state='readonly', width=16)
        self.cboSoundEquiqments['values'] = ('', 'Yes ', 'No ')
        self.cboSoundEquiqments.current(0)
        self.cboSoundEquiqments.grid(row=1, column=1)

        self.lblBackDrops = Label(ItemsFrame, font=(
            'arial', 12, 'bold'), text="BackDrops", bd=7)
        self.lblBackDrops.grid(row=2, column=0, sticky=W)
        self.cboBackDrops = ttk.Combobox(ItemsFrame, font=(
            'arial', 12, 'bold'), textvariable=self.BackDrops, state='readonly', width=16)
        self.cboBackDrops['values'] = ('', 'Yes ', 'No ')
        self.cboBackDrops.current(0)
        self.cboBackDrops.grid(row=2, column=1)

        self.lblCameras = Label(ItemsFrame, font=(
            'arial', 12, 'bold'), text="Cameras", bd=7)
        self.lblCameras.grid(row=3, column=0, sticky=W)
        self.cboCameras = ttk.Combobox(ItemsFrame, font=(
            'arial', 12, 'bold'), textvariable=self.Cameras, state='readonly', width=16)
        self.cboCameras['values'] = ('', 'Yes ', 'No ')
        self.cboCameras.current(0)
        self.cboCameras.grid(row=3, column=1)

        self.lblTripods = Label(ItemsFrame, font=(
            'arial', 12, 'bold'), text="Tripods", bd=7)
        self.lblTripods.grid(row=4, column=0, sticky=W)
        self.cboTripods = ttk.Combobox(ItemsFrame, font=(
            'arial', 12, 'bold'), textvariable=self.Tripods, state='readonly', width=16)
        self.cboTripods['values'] = ('', 'Yes ', 'No ')
        self.cboTripods.current(0)
        self.cboTripods.grid(row=4, column=1)

        self.lblFunitures = Label(ItemsFrame, font=(
            'arial', 12, 'bold'), text="Furniture", bd=7)
        self.lblFunitures.grid(row=5, column=0, sticky=W)
        self.cboFunitures = ttk.Combobox(ItemsFrame, font=(
            'arial', 12, 'bold'), textvariable=self.Funitures, state='readonly', width=16)
        self.cboFunitures['values'] = ('', 'Yes ', 'No ')
        self.cboFunitures.current(0)
        self.cboFunitures.grid(row=5, column=1)

        self.lblProjectors = Label(ItemsFrame, font=(
            'arial', 12, 'bold'), text="Projectors", bd=7)
        self.lblProjectors.grid(row=6, column=0, sticky=W)
        self.cboProjectors = ttk.Combobox(ItemsFrame, font=(
            'arial', 12, 'bold'), textvariable=self.Projectors, state='readonly', width=16)
        self.cboProjectors['values'] = ('', 'Yes ', 'No ')
        self.cboProjectors.current(0)
        self.cboProjectors.grid(row=6, column=1)

        self.lblWIFI = Label(ItemsFrame, font=(
            'arial', 12, 'bold'), text="WIFI", bd=7)
        self.lblWIFI.grid(row=7, column=0, sticky=W)
        self.cboWIFI = ttk.Combobox(ItemsFrame, font=(
            'arial', 12, 'bold'), textvariable=self.WIFI, state='readonly', width=16)
        self.cboWIFI['values'] = ('', 'Yes ', 'No')
        self.cboWIFI.current(0)
        self.cboWIFI.grid(row=7, column=1)

        self.lblGreenScreen = Label(ItemsFrame, font=(
            'arial', 12, 'bold'), text="Green Screen", bd=7)
        self.lblGreenScreen.grid(row=8, column=0, sticky=W)
        self.cboGreenScreen = ttk.Combobox(ItemsFrame, font=(
            'arial', 12, 'bold'), textvariable=self.GreenScreen, state='readonly', width=16)
        self.cboGreenScreen['values'] = ('', 'Yes ', 'No ')
        self.cboGreenScreen.current(0)
        self.cboGreenScreen.grid(row=8, column=1)

        self.lblCosmetics = Label(ItemsFrame, font=(
            'arial', 12, 'bold'), text="Cosmetics", bd=7)
        self.lblCosmetics.grid(row=9, column=0, sticky=W)
        self.cboCosmetics = ttk.Combobox(ItemsFrame, font=(
            'arial', 12, 'bold'), textvariable=self.Cosmetics, state='readonly', width=16)
        self.cboCosmetics['values'] = ('', 'Yes ', 'No ')
        self.cboCosmetics.current(0)
        self.cboCosmetics.grid(row=9, column=1)

        self.lblDecorations = Label(ItemsFrame, font=(
            'arial', 12, 'bold'), text="Decorations", bd=7)
        self.lblDecorations.grid(row=10, column=0, sticky=W)
        self.cboDecorations = ttk.Combobox(ItemsFrame, font=(
            'arial', 12, 'bold'), textvariable=self.Decorations, state='readonly', width=16)
        self.cboDecorations['values'] = ('', 'Yes ', 'No ')
        self.cboDecorations.current(0)
        self.cboDecorations.grid(row=10, column=1)

        self.lblClothes = Label(ItemsFrame, font=(
            'arial', 12, 'bold'), text="Clothes", bd=7)
        self.lblClothes.grid(row=11, column=0, sticky=W)
        self.cboClothes = ttk.Combobox(ItemsFrame, font=(
            'arial', 12, 'bold'), textvariable=self.Clothes, state='readonly', width=16)
        self.cboClothes['values'] = ('', 'Yes ', 'No ')
        self.cboClothes.current(0)
        self.cboClothes.grid(row=11, column=1)

        self.lblProps = Label(ItemsFrame, font=(
            'arial', 12, 'bold'), text="Props", bd=7)
        self.lblProps.grid(row=12, column=0, sticky=W)
        self.cboProps = ttk.Combobox(ItemsFrame, font=(
            'arial', 12, 'bold'), textvariable=self.Props, state='readonly', width=16)
        self.cboProps['values'] = ('', 'Yes ', 'No ')
        self.cboProps.current(0)
        self.cboProps.grid(row=12, column=1)

        self.lblAircontioner = Label(ItemsFrame, font=(
            'arial', 12, 'bold'), text="Air Conditioner", bd=7)
        self.lblAircontioner.grid(row=13, column=0, sticky=W)
        self.cboAircontioner = ttk.Combobox(ItemsFrame, font=(
            'arial', 12, 'bold'), textvariable=self.Aircondioner, state='readonly', width=16)
        self.cboAircontioner['values'] = ('', 'Yes ', 'No ')
        self.cboAircontioner.current(0)
        self.cboAircontioner.grid(row=13, column=1)

        self.lblVideoMonitors = Label(ItemsFrame, font=(
            'arial', 12, 'bold'), text="Video Monitors", bd=7)
        self.lblVideoMonitors.grid(row=14, column=0, sticky=W)
        self.cboVideoMonitors = ttk.Combobox(ItemsFrame, font=(
            'arial', 12, 'bold'), textvariable=self.VideoMonitors, state='readonly', width=16)
        self.cboVideoMonitors['values'] = ('', 'Yes ', 'No ')
        self.cboVideoMonitors.current(0)
        self.cboVideoMonitors.grid(row=14, column=1)

        self.lblStudioAccessories = Label(ItemsFrame, font=(
            'arial', 12, 'bold'), text="Studio Accessories", bd=7)
        self.lblStudioAccessories.grid(row=15, column=0, sticky=W)
        self.cboStudioAccessories = ttk.Combobox(ItemsFrame, font=(
            'arial', 12, 'bold'), textvariable=self.StudioAccessories, state='readonly', width=16)
        self.cboStudioAccessories['values'] = ('', 'Yes ', 'No ')
        self.cboStudioAccessories.current(0)
        self.cboStudioAccessories.grid(row=15, column=1)

# =====================Treeview frame=======================
        TopFrame11 = Frame(Tab2Frame, bd=10, width=1350,
                           height=60, relief=RIDGE)
        TopFrame11.grid(row=0, column=0)
        TopFrame12 = Frame(Tab2Frame, bd=10, width=1600,
                           height=500, relief=RIDGE)
        TopFrame12.grid(row=1, column=0)
# =====================Treeview title=======================
        self.lblTitle = Label(TopFrame11, font=(
            'arial', 20, 'bold'), text="Studio Management System", bd=7)
        self.lblTitle.grid(row=0, column=0)
# =====================Treeview table=======================
        scroll_x = Scrollbar(TopFrame12, orient=HORIZONTAL)
        scroll_y = Scrollbar(TopFrame12, orient=VERTICAL)

        self.StudioTable = ttk.Treeview(TopFrame12, columns=("customernumber", "firstname", "surname", "idnumber", "address", "mobile", "email", "gender",
                                        "dob", "photographer", "pname", "psurname", "pid", "pemail", "pworkphone", "pmobile"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=BOTTOM, fill=Y)

        self.StudioTable.heading("customernumber", text="Client No")
        self.StudioTable.heading("firstname", text="First Name")
        self.StudioTable.heading("surname", text="Surname")
        self.StudioTable.heading("idnumber", text="ID Number")
        self.StudioTable.heading("address", text="Address")
        self.StudioTable.heading("mobile", text="Mobile")
        self.StudioTable.heading("email", text="Email")
        self.StudioTable.heading("gender", text="Gender")
        self.StudioTable.heading("dob", text="DOB")

        self.StudioTable.heading("photographer", text="Photographer")
        self.StudioTable.heading("pname", text="Name")
        self.StudioTable.heading("psurname", text="Surname")
        self.StudioTable.heading("pid", text="ID")
        self.StudioTable.heading("pmobile", text="Mobile")
        self.StudioTable.heading("pworkphone", text="Work Phone")
        self.StudioTable.heading("pemail", text="Email")

        self.StudioTable['show'] = 'headings'
        self.StudioTable.column("customernumber", width=70)
        self.StudioTable.column("firstname", width=90)
        self.StudioTable.column("surname", width=90)
        self.StudioTable.column("address", width=200)
        self.StudioTable.column("mobile", width=70)
        self.StudioTable.column("email", width=100)
        self.StudioTable.column("idnumber", width=80)
        self.StudioTable.column("gender", width=60)
        self.StudioTable.column("dob", width=70)

        self.StudioTable.column("photographer", width=70)
        self.StudioTable.column("pname", width=90)
        self.StudioTable.column("psurname", width=90)
        self.StudioTable.column("pid", width=70)
        self.StudioTable.column("pemail", width=70)
        self.StudioTable.column("pworkphone", width=70)
        self.StudioTable.column("pmobile", width=70)

        self.StudioTable.pack(fill=BOTH, expand=1)
        self.StudioTable.bind("<ButtonRelease-1>", bookingInfo)
        DisplayData()


# =====================Buttons=======================
        self.btnAddNew = Button(ButtonFrame, pady=1, bd=4, fg="black", font=(
            'arial', 17,), width=6, text="AddNew", command=addData, padx=11).grid(row=0, column=0, padx=2)
        self.btnUpdate = Button(ButtonFrame, pady=1, bd=4, fg="black", font=(
            'arial', 17,), width=6, text="Update", command=UpdateData, padx=12).grid(row=0, column=1, padx=2)
        self.btnDelete = Button(ButtonFrame, pady=1, bd=4, fg="black", font=(
            'arial', 17,), width=6, text="Delete", command=DeleteData, padx=12,).grid(row=0, column=2, padx=2)
        self.btnReset = Button(ButtonFrame, pady=1, bd=4, fg="black", font=(
            'arial', 17,), width=6, text="Reset", command=iReset, padx=12).grid(row=0, column=3, padx=2)
        self.btnExit = Button(ButtonFrame, pady=1, bd=4, fg="black", font=(
            'arial', 17,), width=6, text="Exit", command=iExit, padx=12).grid(row=0, column=4, padx=2)


if __name__ == '__main__':
    root = Tk()
    application = Studio(root)
    root.mainloop()
