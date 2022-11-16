from tkinter import *
from tkinter.ttk import *


class UI():

	def __init__(self, api):
		self.api = api


		# Window
		self.root = Tk()
		self.root.title('Easy REST Tester')
		#self.root.resizable(False, False)


		# Request Frame -> all the request information.
		self.RequestFrame = Frame(self.root)
		Label(self.RequestFrame, text='REQUEST')

		self.method = StringVar()
		Label(self.RequestFrame, text='Method')
		self.MethodInput = Combobox(self.RequestFrame, textvariable=self.method)
		self.MethodInput['values'] = self.api.get_methods()
		self.MethodInput.state(['readonly'])
		self.MethodInput.current(0)

		self.url = StringVar()
		Label(self.RequestFrame, text='URL')
		self.UrlInput = Entry(self.RequestFrame, textvariable=self.url)

		self.RequestButton = Button(self.RequestFrame, text='Request', command=self.send_request)

		
		self.NotebookRequest = Notebook(self.RequestFrame)

		self.RequestParametersFrame = Frame(self.NotebookRequest)
		self.RequestBodyFrame = Frame(self.NotebookRequest)
		self.RequestHeadersFrame = Frame(self.NotebookRequest)

		self.NotebookRequest.add(self.RequestParametersFrame, text='Parameters')
		self.NotebookRequest.add(self.RequestBodyFrame, text='Body')
		self.NotebookRequest.add(self.RequestHeadersFrame, text='Headers')


		# Response Frame -> all the data from the response.
		self.ResponseFrame = Frame(self.root)
		Label(self.ResponseFrame, text='RESPONSE').grid(column=0, row=0)

		self.NotebookResponse = Notebook(self.ResponseFrame)
		self.NotebookResponse.grid(column=0, row=1)

		self.ResponseBodyFrame = Frame(self.NotebookResponse)
		self.ResponseHeadersFrame = Frame(self.NotebookResponse)

		self.NotebookResponse.add(self.ResponseBodyFrame, text='Body')
		self.NotebookResponse.add(self.ResponseHeadersFrame, text='Headers')

			# Response Body
		self.ResponseBodyText = Text(self.ResponseBodyFrame, wrap='none')
		self.ResponseBodyText.grid(column=0, row=0, sticky='nwes')
		self.ResponseBodyText['state'] = 'disabled'

		self.ysbody = Scrollbar(self.ResponseBodyFrame, orient = 'vertical', command = self.ResponseBodyText.yview)
		self.xsbody = Scrollbar(self.ResponseBodyFrame, orient = 'horizontal', command = self.ResponseBodyText.xview)
		self.ResponseBodyText['yscrollcommand'] = self.ysbody.set
		self.ResponseBodyText['xscrollcommand'] = self.xsbody.set

		self.ysbody.grid(column = 1, row = 0, sticky = 'ns')
		self.xsbody.grid(column = 0, row = 1, sticky = 'we')

		self.RequestFrame.grid_columnconfigure(0, weight = 1)
		self.RequestFrame.grid_rowconfigure(0, weight = 1)

			#Response Headers
		self.ResponseHeadersText = Text(self.ResponseHeadersFrame, wrap='none')
		self.ResponseHeadersText.grid(column=0, row=0, sticky='nwes')
		self.ResponseHeadersText['state'] = 'disabled'

		self.ysheaders = Scrollbar(self.ResponseHeadersFrame, orient = 'vertical', command = self.ResponseHeadersText.yview)
		self.xsheaders = Scrollbar(self.ResponseHeadersFrame, orient = 'horizontal', command = self.ResponseHeadersText.xview)
		self.ResponseHeadersText['yscrollcommand'] = self.ysheaders.set
		self.ResponseHeadersText['xscrollcommand'] = self.xsheaders.set

		self.ysheaders.grid(column = 1, row = 0, sticky = 'ns')
		self.xsheaders.grid(column = 0, row = 1, sticky = 'we')

		self.RequestFrame.grid_columnconfigure(0, weight = 1)
		self.RequestFrame.grid_rowconfigure(0, weight = 1)
		

		# PACK
		self.pack_all()

		# 'Enter' key
		self.UrlInput.bind("<Return>", lambda e: self.RequestButton.invoke())

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
		self.print_body_response(self.api.get_body_response())
		self.print_headers_response(self.api.get_headers_response())


	def print_body_response(self, response):
		self.ResponseBodyText['state'] = 'normal'
		self.ResponseBodyText.replace('1.0', 'end', response)
		self.ResponseBodyText['state'] = 'disabled'


	def print_headers_response(self, response):
		self.ResponseHeadersText['state'] = 'normal'
		self.ResponseHeadersText.replace('1.0', 'end', response)
		self.ResponseHeadersText['state'] = 'disabled'