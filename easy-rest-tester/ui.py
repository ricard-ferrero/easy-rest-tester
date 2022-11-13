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
		Label(self.RequestFrame, text='Request')

		"""
		self.method = StringVar()
		Label(self.RequestFrame, text='Method')
		self.MethodEntry = Entry(self.RequestFrame, textvariable=self.method)
		"""

		self.method = StringVar()
		Label(self.RequestFrame, text='Method')
		self.MethodInput = Combobox(self.RequestFrame, textvariable=self.method)
		self.MethodInput['values'] = self.api.get_methods()
		self.MethodInput.state(['readonly'])
		self.MethodInput.current(0)

		self.url = StringVar()
		Label(self.RequestFrame, text='URL')
		self.UrlInput = Entry(self.RequestFrame, textvariable=self.url)

		self.button = Button(self.RequestFrame, text='Request', command=self.send_request)


		# Response Frame -> all the data from the response.
		self.ResponseFrame = Frame(self.root)
		Label(self.ResponseFrame, text='Response').grid(column=0, row=0)

		self.ResponseText = Text(self.ResponseFrame, wrap='none')
		self.ResponseText.grid(column=0, row=1, sticky='nwes')
		self.ResponseText['state'] = 'disabled'

		#t = Text(root, width = 40, height = 5, wrap = "none")
		self.ys = Scrollbar(self.ResponseFrame, orient = 'vertical', command = self.ResponseText.yview)
		self.xs = Scrollbar(self.ResponseFrame, orient = 'horizontal', command = self.ResponseText.xview)
		self.ResponseText['yscrollcommand'] = self.ys.set
		self.ResponseText['xscrollcommand'] = self.xs.set

		self.ys.grid(column = 1, row = 1, sticky = 'ns')
		self.xs.grid(column = 0, row = 2, sticky = 'we')

		self.RequestFrame.grid_columnconfigure(0, weight = 1)
		self.RequestFrame.grid_rowconfigure(0, weight = 1)
		

		# PACK
		self.pack_all()

		# Loop
		self.root.mainloop()


	def pack_all(self):
		self.RequestFrame.pack(side=LEFT)
		self.ResponseFrame.pack(side=RIGHT)

		for child in self.RequestFrame.winfo_children():
			child.pack()

		#for child in self.ResponseFrame.winfo_children():
		#	child.pack()


	def send_request(self):
		self.api.set_method(self.method.get())
		self.api.set_url(self.url.get())
		response = self.api.request()
		self.print_response(response)


	def print_response(self, response):
		self.ResponseText['state'] = 'normal'

		if type(response) == str:
			self.ResponseText.replace('1.0', 'end', response)
		else:
			self.ResponseText.replace('1.0', 'end', response.text)
		self.ResponseText['state'] = 'disabled'