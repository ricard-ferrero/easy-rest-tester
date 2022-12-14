from tkinter import *
from tkinter.ttk import *

BIG_PAD=10
SMALL_PAD=5

class ParametersInput():

	def __init__(self, frame, row):
		PAD = 3
		self.check = BooleanVar()
		self.key = StringVar()
		self.value = StringVar()

		self.check_input = Checkbutton(frame, variable=self.check, onvalue=True, offvalue=False)
		self.check_input.grid(column=0, row=row, padx=PAD, pady=PAD)
		self.key_input = Entry(frame, textvariable=self.key)
		self.key_input.grid(column=1, row=row, padx=PAD, pady=PAD)
		self.value_input = Entry(frame, textvariable=self.value)
		self.value_input.grid(column=2, row=row, padx=PAD, pady=PAD)


	def get_parameters(self):
		if self.check.get():
			return (self.key.get(), self.value.get())
		return None


class UI():

	def __init__(self, api):
		self.api = api


		# WINDOW
		self.root = Tk()
		self.root.title('Easy REST Tester')
		self.root.resizable(False,False)


		# REQUEST FRAME -> all the request information.
			# Title
		self.RequestFrame = Frame(self.root)
		Label(self.RequestFrame, text='REQUEST')

			# Basic Inputs
		self.BasicInputsFrame = Frame(self.RequestFrame)
		self.method = StringVar()
		self.MethodLabel = Label(self.BasicInputsFrame, text='Method')
		self.MethodInput = Combobox(self.BasicInputsFrame, textvariable=self.method, width=7)
		self.MethodInput['values'] = self.api.get_methods()
		self.MethodInput.state(['readonly'])
		self.MethodInput.current(0)

		self.url = StringVar()
		self.UrlLabel = Label(self.BasicInputsFrame, text='URL')
		self.UrlInput = Entry(self.BasicInputsFrame, textvariable=self.url, width=40)

		self.RequestButton = Button(self.BasicInputsFrame, text='Request', command=self.send_request)

			# Data Inputs
		self.NotebookRequest = Notebook(self.RequestFrame)

		self.RequestParametersFrame = Frame(self.NotebookRequest)
		self.RequestBodyFrame = Frame(self.NotebookRequest)
		#self.RequestHeadersFrame = Frame(self.NotebookRequest)

		self.NotebookRequest.add(self.RequestParametersFrame, text='Parameters')
		self.NotebookRequest.add(self.RequestBodyFrame, text='Body')
		#self.NotebookRequest.add(self.RequestHeadersFrame, text='Headers')

				# Request Parameters
		self.ParametersInputsFrame = Frame(self.RequestParametersFrame)
		self.ParametersButtonFrame = Frame(self.RequestParametersFrame)

		self.ParametersList = [ParametersInput(self.ParametersInputsFrame, 0),]

		self.AddParametersButton = Button(self.ParametersButtonFrame, text='+ Add', command=self.add_parameters_input)
			
				# Request Body
		self.BodyInputsFrame = Frame(self.RequestBodyFrame)
		self.BodyButtonFrame = Frame(self.RequestBodyFrame)

		self.BodyList = [ParametersInput(self.BodyInputsFrame, 0),]
		
		self.AddBodyButton = Button(self.BodyButtonFrame, text='+ Add', command=self.add_body_input)

				# Request Headers
		#

		# RESPONSE FRAME -> all the data from the response.
		self.ResponseFrame = Frame(self.root)
		self.ResponseLabel = Label(self.ResponseFrame, text='RESPONSE')

		self.NotebookResponse = Notebook(self.ResponseFrame)
		self.ResponseBodyFrame = Frame(self.NotebookResponse)
		self.ResponseHeadersFrame = Frame(self.NotebookResponse)
		self.NotebookResponse.add(self.ResponseBodyFrame, text='Body')
		self.NotebookResponse.add(self.ResponseHeadersFrame, text='Headers')

			# Response Body
		self.ResponseBodyText = Text(self.ResponseBodyFrame, wrap='none')

		self.ysbody = Scrollbar(self.ResponseBodyFrame, orient = 'vertical', command = self.ResponseBodyText.yview)
		self.xsbody = Scrollbar(self.ResponseBodyFrame, orient = 'horizontal', command = self.ResponseBodyText.xview)
		self.ResponseBodyText['yscrollcommand'] = self.ysbody.set
		self.ResponseBodyText['xscrollcommand'] = self.xsbody.set

			# Response Headers
		self.ResponseHeadersText = Text(self.ResponseHeadersFrame, wrap='none')

		self.ysheaders = Scrollbar(self.ResponseHeadersFrame, orient = 'vertical', command = self.ResponseHeadersText.yview)
		self.xsheaders = Scrollbar(self.ResponseHeadersFrame, orient = 'horizontal', command = self.ResponseHeadersText.xview)
		self.ResponseHeadersText['yscrollcommand'] = self.ysheaders.set
		self.ResponseHeadersText['xscrollcommand'] = self.xsheaders.set


		# PLACE ALL WIDGETS
		self.geometry()


		# Loop
		self.root.mainloop()


	def geometry(self):
		"""
		To place all widgets in a structure
		"""
		# Prepare the root's grid
		self.root.columnconfigure(0, weight=1)
		self.root.columnconfigure(1, weight=1)
		self.root.rowconfigure(0, weight=1)

		# All Request widgets
		self.RequestFrame.grid(column=0, row=0, sticky=NS, padx=BIG_PAD, pady=BIG_PAD)
		self.pack_in(self.RequestFrame) # 3 childs: title, frame, notebook
		self.NotebookRequest.pack_configure(fill=BOTH, expand=True)
		self.BasicInputsFrame.columnconfigure(0, weight=1)
		self.BasicInputsFrame.columnconfigure(1, weight=3)
		self.BasicInputsFrame.rowconfigure(0, weight=1)
		self.BasicInputsFrame.rowconfigure(1, weight=1)
		self.BasicInputsFrame.rowconfigure(2, weight=1)
		self.MethodLabel.grid(column=0, row=0, sticky=W, padx=SMALL_PAD)
		self.UrlLabel.grid(column=1, row=0, sticky=W, padx=SMALL_PAD)
		self.MethodInput.grid(column=0, row=1, padx=SMALL_PAD)
		self.UrlInput.grid(column=1, row=1, padx=SMALL_PAD)
		self.RequestButton.grid(column=0, row=2, columnspan=3, padx=SMALL_PAD, pady=SMALL_PAD)
		self.pack_in(self.RequestParametersFrame)
		self.AddParametersButton.pack()
		self.pack_in(self.RequestBodyFrame)
		self.AddBodyButton.pack()

		# All Response widgets
		self.ResponseFrame.grid(column=1, row=0, sticky=NS, padx=BIG_PAD, pady=BIG_PAD)
		self.pack_in(self.ResponseFrame) # 2 childs: title, notebook
		self.NotebookResponse.pack_configure(fill=Y, expand=True)
		self.ResponseBodyText.grid(column=0, row=0, sticky='nwes')
		self.ysbody.grid(column = 1, row = 0, sticky = 'ns')
		self.xsbody.grid(column = 0, row = 1, sticky = 'we')
		self.ResponseHeadersText.grid(column=0, row=0, sticky='nwes')
		self.ysheaders.grid(column = 1, row = 0, sticky = 'ns')
		self.xsheaders.grid(column = 0, row = 1, sticky = 'we')


	def pack_in(self, frame):
		"""
		To place the widgets inside the 'frame' using .pack()
		"""
		for child in frame.winfo_children():
			child.pack(padx=BIG_PAD, pady=BIG_PAD)


	def add_parameters_input(self):
		self.ParametersList.append(ParametersInput(self.ParametersInputsFrame, len(self.ParametersList)))


	def add_body_input(self):
		self.BodyList.append(ParametersInput(self.BodyInputsFrame, len(self.BodyList)))


	def send_request(self):
		# Prepare the Request
		self.api.set_method(self.method.get())
		self.api.set_url(self.url.get())
		
		parameters = {}
		for parameter in self.ParametersList:
			values = parameter.get_parameters()
			if values:
				parameters[values[0]] = values[1]
		self.api.set_parameters(parameters)

		data = {}
		for body_data in self.BodyList:
			values = body_data.get_parameters()
			if values:
				data[values[0]] = values[1]
		self.api.set_data(data)

		# Send the Request and catch the response
		self.api.send_request()
		self.print_body_response(self.api.get_body_response())
		self.print_headers_response(self.api.get_headers_response())
		self.url.set(self.api.get_url())


	def print_body_response(self, response):
		self.ResponseBodyText['state'] = 'normal'
		self.ResponseBodyText.replace('1.0', 'end', response)
		self.ResponseBodyText['state'] = 'disabled'


	def print_headers_response(self, response):
		self.ResponseHeadersText['state'] = 'normal'
		self.ResponseHeadersText.replace('1.0', 'end', response)
		self.ResponseHeadersText['state'] = 'disabled'