import string
import random
import tkinter as tk
import time

def slogan(password):
    topwindow=tk.Toplevel(root)
    topwindow.title('Top')
    info=password
    tk.Label(topwindow,text=info).grid(row=0,column=0)

def password_generator():

    try:
        length=int(entryfield.get())
        print(length)
    except:
        length=5
    mystring=string.ascii_letters
    mystring1=string.digits
    mystring2=string.punctuation
    mylist=[]
    mylist.extend(mystring)
    mylist.extend(mystring1)
    mylist.extend(mystring2)
    if length>len(mylist):
        length=5
    #print(mylist)
    random.shuffle(mylist)
    print(mylist)
    password=''
    updated=mylist[0:length]
    for i in updated:
        password=password+i
    print(password)
    slogan(password)

   
if __name__ == '__main__':
    root=tk.Tk()
    root.title('Generate password')
    root.geometry('300x300')
    message='Password Generator'
    msg=tk.Message(root,text=message)
    msg.config(bg='green',font=('times',24,'italic'))
    msg.pack(side=tk.TOP)
    entryfield=tk.Entry(root,text='')
    entryfield.pack(side=tk.RIGHT)
    password_button=tk.Button(root,text='Generate Password',command=password_generator,fg='blue')
    password_button.pack(side=tk.LEFT)
    root.mainloop()


    
    
