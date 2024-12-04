from os import listdir
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import SaveFileDialog

root=Tk()
root.title("data entry software")
root.geometry("1000x1000")

def savedata():
    fp=open("D:\data\data.xlsx", "a+")
    fm=txtm.get()
    fn=txtf.get()
    ln=txtl.get()
    a=txta.get()
    da=txtd.get()
    sc=txte.get()
    fp.write(fm)
    fp.write(" \n")
    fp.write(fn)
    fp.write(" \n")
    fp.write(ln)
    fp.write(" \n")
    fp.write(a)
    fp.write(" \n")
    fp.write(da)
    fp.write(" \n")
    fp.write(sc)
    fp.write(" \n")
    fp.close()
    messagebox.showinfo("Save", "Data Entered Sucessfully")
    txtm.delete(0, END)
    txtf.delete(0, END)
    txtl.delete(0, END)
    txta.delete(0, END)
    txtd.delete(0, END)
    txte.delete(0, END)

lblh=Label(root, text="DATA ENTRY SOFTWARE", font="lucida 17 bold")
lblh.grid(row=0, column=0, padx=15, pady=15, ipady=15, ipadx=15)

lblj=Label(root, text=">>-Data Entry-<<", font="lucida 20 bold")
lblj.grid(row=0, column=1, padx=15, pady=15, ipady=15, ipadx=15)

lblm=Label(root, text="Entry Number", font="lucida 17 bold")
lblf=Label(root, text="Enter Customers Name", font="lucida 17 bold")
lbll=Label(root, text="Enter The Service", font="lucida 17 bold")
lbla=Label(root, text="enter PMjay Id", font="lucida 17 bold")
lbld=Label(root, text="Issue Date", font="lucida 17 bold")
lble=Label(root, text="Mo. Number", font="lucida 17 bold")

lbln=Label(root, text="developed by Aagam sanghavi", font="lucida 12 bold")
lbln.grid(row=9, column=0, padx=15, pady=15, ipady=15, ipadx=15)

txtm=Entry(root, font="lucida 15 bold")
txtf=Entry(root, font="lucida 15 bold")
txtl=Entry(root, font="lucida 15 bold")
txta=Entry(root, font="lucida 15 bold")
txtd=Entry(root, font="lucida 15 bold")
txte=Entry(root, font="lucida 15 bold")

lblm.grid(row=3, column=0, padx=15, pady=15, ipady=15, ipadx=15)
txtm.grid(row=3, column=1, padx=15, pady=15, ipady=15, ipadx=15)

lblf.grid(row=4, column=0, padx=15, pady=15, ipady=15, ipadx=15)
txtf.grid(row=4, column=1, padx=15, pady=15, ipady=15, ipadx=15)

lbll.grid(row=5, column=0, padx=15, pady=15, ipady=15, ipadx=15)
txtl.grid(row=5, column=1, padx=15, pady=15, ipady=15, ipadx=15)

lbla.grid(row=6, column=0, padx=15, pady=15, ipady=15, ipadx=15)
txta.grid(row=6, column=1, padx=15, pady=15, ipady=15, ipadx=15)

lbld.grid(row=7, column=0, padx=15, pady=15, ipady=15, ipadx=15)
txtd.grid(row=7, column=1, padx=15, pady=15, ipady=15, ipadx=15)

lble.grid(row=8, column=0, padx=15, pady=15, ipady=15, ipadx=15)
txte.grid(row=8, column=1, padx=15, pady=15, ipady=15, ipadx=15)

btnsave=Button(root, text="Save", font="lucida 13 bold", bg="sky blue", command=savedata)
btnsave.grid(row=8, column=2, padx=15, pady=15, ipady=15, ipadx=15)


root.mainloop()