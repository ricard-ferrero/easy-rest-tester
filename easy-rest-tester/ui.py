from tkinter import *
from tkinter import ttk


# Window
root = Tk()
root.title('Easy REST Tester')
root.resizable(False, False)


# Request Frame -> all the request information.
RequestFrame = Frame(root)
RequestFrame.pack(side=LEFT)
Label(RequestFrame, text='Request').pack()



# Response Frame -> all the data from the response.
ResponseFrame = Frame(root)
ResponseFrame.pack(side=RIGHT)
Label(ResponseFrame, text='Response').pack()


if __name__ == '__main__':
	root.mainloop()