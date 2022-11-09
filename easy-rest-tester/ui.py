from tkinter import *
from tkinter import ttk
from api import API

class UI(API):

	def __init__(self):
		# Window
		self.root = Tk()
		self.root.title('Easy REST Tester')
		self.root.resizable(False, False)


		# Request Frame -> all the request information.
		self.RequestFrame = Frame(self.root)
		self.RequestFrame.pack(side=LEFT)
		Label(self.RequestFrame, text='Request').pack()

		self.method = StringVar()
		Label(self.RequestFrame, text='Method').pack()
		self.MethodEntry = Entry(self.RequestFrame, textvariable=self.method).pack()

		self.url = StringVar()
		Label(self.RequestFrame, text='URL').pack()
		self.UrlEntry = Entry(self.RequestFrame, textvariable=self.url).pack()

		self.button = Button(self.RequestFrame, text='Request', command=self.cosadexa).pack()


		# Response Frame -> all the data from the response.
		self.ResponseFrame = Frame(self.root)
		self.ResponseFrame.pack(side=RIGHT)
		Label(self.ResponseFrame, text='Response').pack()


if __name__ == '__main__':
	ui = UI()
	ui.root.mainloop()