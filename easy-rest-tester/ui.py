from tkinter import *
from tkinter.ttk import *


class UI():

	def __init__(self, api):
		self.api = api


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

		self.button = Button(self.RequestFrame, text='Request', command=self.send_request).pack()


		# Response Frame -> all the data from the response.
		self.ResponseFrame = Frame(self.root)
		self.ResponseFrame.pack(side=RIGHT)
		Label(self.ResponseFrame, text='Response').pack()

		self.ResponseText = Text(self.ResponseFrame)
		self.ResponseText.pack()
		self.ResponseText.insert('1.0', 'DFNAJDSBABDHAS')
		self.ResponseText['state'] = 'disabled'

		# Loop
		self.root.mainloop()


	def send_request(self):
		self.api.set_method(self.method.get())
		self.api.set_url(self.url.get())
		response = self.api.request()
		print(response.headers)