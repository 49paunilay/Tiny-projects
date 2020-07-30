import time
import tkinter as tk
import pyautogui
import random

def screenshot():
    time.sleep(3)
    name=random.randint(99,1001)
    img=pyautogui.screenshot('{}.png'.format(name))
    print(f'{name} is captured at ',time.time())

root=tk.Tk()
root.geometry("300x50")
root.title('My screenshot app')
frame=tk.Frame(root)
frame.pack()
record=tk.Button(frame,text='Capture',command=screenshot)
record.pack(side=tk.RIGHT)
quitbutton=tk.Button(frame,text='Close',command=quit)
quitbutton.pack(side=tk.LEFT)
try:
    root.mainloop()
except:
    print('Closing')
