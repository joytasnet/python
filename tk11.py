import tkinter as tk
def check():
    if cval.get()==True:
        print('チェックされています')
    else:
        print('チェックされていません')

root=tk.Tk()
root.title('My Window')
root.geometry('400x200')
cval=tk.BooleanVar()
cval.set(False)
cbtn=tk.Checkbutton(text='チェックボタン',command=check,variable=cval)
cbtn.pack()
root.mainloop()
