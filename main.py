# from tkinter import*
# from tkinter import messagebox

# root=Tk()
# root.geometry("400x400")

# def msg():
#     messagebox.showwarning("Alert","STOP! virus found!")

# button=Button(root, text="Scan for virus", command=msg)
# button.place(x=208, y=200)


# root.mainloop()



from tkinter import*
root=Tk()
root.geometry("400x300")
def topwin():
    top=Toplevel()
    top.geometry("180x100")
    top.title("toplevel")

    top.configure(bg="cyan")
    l2=Label(top, text="this is toplevel window")
    l2.pack()

    top.mainloop()

l=Label(root, text="this is root window")

btn=Button(root, text="click here to open another window", command=topwin)

l.pack()
btn.pack()
root.mainloop()
             