from tkinter import *
import smtplib

# Main Screen
root = Tk()
root.geometry("600x650")
root.title("Mail Application")

# Functions
def send():
    try:
        username = temp_username.get()
        password = temp_password.get()
        body = temp_body.get()
        to = temp_receiver.get()
        subject = temp_subject.get()
        if username =="" or password =="" or to == "" or subject=="" or body =="":
            notif.config(Text="All fields required!",fg="red")
            return
        else:
            finalMessage = "Subject: {}\n\n{}".format(subject,body)
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(user = username,password = password)
            server.sendmail(username,to,finalMessage)
            notif.config(text = 'Email has been sent',fg='green')


    except:
        notif.config(text="Error sending email",fg='red')
        




def reset():
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    receiverEntry.delete(0,END)
    subjectEntry.delete(0,END)
    bodyEntry.delete("1.0", "end")
    pass

# Graphics
Label(root,text="Mail Application",font=("Calibri",15)).grid(row=0,column=1,sticky=N)
Label(root,text="Use the form below to send an email",
      font=('Calibri',11)).grid(row=1,column=1,sticky=N,padx=15,pady=10)

# Form Details
Label(root,text="Email",font=('Calibri',11)).grid(row=2,sticky=W,padx=7,pady=5)
Label(root,text="Password",font=('Calibri',11)).grid(row=3,sticky=W,padx=7,pady=5)
Label(root,text="To",font=('Calibri',11)).grid(row=4,sticky=W,padx=7,pady=5)
Label(root,text="Subject",font=('Calibri',11)).grid(row=5,sticky=W,padx=7,pady=5)
Label(root,text="Body",font=('Calibri',11)).grid(row=6,sticky=W,padx=7,pady=5)

notif = Label(root,text="",font=('Calibri',11))
notif.grid(row=8,column=1,sticky=S,padx=5)

#storage
temp_username = StringVar()
temp_password = StringVar()
temp_receiver = StringVar()
temp_subject = StringVar()
temp_body = StringVar()

# Entries
usernameEntry = Entry(root,
                      textvariable=temp_username,
                      width=53,
                      font=('Calibri',12))
usernameEntry.grid(row=2,column=1,padx=7)
passwordEntry = Entry(root,
                      show="* ",
                      textvariable=temp_password,
                      width=53,
                      font=('Calibri',12))
passwordEntry.grid(row=3,column=1,padx=7)
receiverEntry = Entry(root,
                      textvariable=temp_receiver,
                      width=53,
                      font=('Calibri',12))
receiverEntry.grid(row=4,column=1)
subjectEntry = Entry(root,textvariable=temp_subject,width=53,font=('Calibri',12))
subjectEntry.grid(row=5,column=1)
bodyEntry = Text(root,width=51,height=15,padx=10,pady=10)
bodyEntry.grid(row=6,column=1)

#Buttons
Button(root , 
       padx=5,
       pady=5,
       text="Send",
       command = send).grid(row=7,column=1,sticky=S,padx=5,pady=15)
Button(root , 
       padx=5,
       pady=5,
       text="Reset",
       command = reset).grid(row=7,column=1,sticky=S,padx=45,pady=45)
root.mainloop()