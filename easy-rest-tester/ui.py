from tkinter import *
from tkinter.ttk import *


class ParametersInput():

	def __init__(self, frame, row):
		self.check = BooleanVar()
		self.key = StringVar()
		self.value = StringVar()
		self.check_input = Checkbutton(frame, variable=self.check, onvalue=True, offvalue=False)
		self.check_input.grid(column=0, row=row)
		self.key_input = Entry(frame, textvariable=self.key)
		self.key_input.grid(column=1, row=row)
		self.value_input = Entry(frame, textvariable=self.value)
		self.value_input.grid(column=2, row=row)


	def get_parameters(self):
		if self.check.get():
			return (self.key.get(), self.value.get())
		return None



class UI():

	def __init__(self, api):
		self.api = api


		# Window
		self.root = Tk()
		self.root.title('Easy REST Tester')
		#self.root.resizable(False, False)


		# REQUEST FRAME -> all the request information.
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
		#self.RequestHeadersFrame = Frame(self.NotebookRequest)

		self.NotebookRequest.add(self.RequestParametersFrame, text='Parameters')
		self.NotebookRequest.add(self.RequestBodyFrame, text='Body')
		#self.NotebookRequest.add(self.RequestHeadersFrame, text='Headers')

			# Request Parameters
		self.ParametersInputsFrame = Frame(self.RequestParametersFrame)
		self.ParametersInputsFrame.pack()
		self.ParametersButtonFrame = Frame(self.RequestParametersFrame)
		self.ParametersButtonFrame.pack()

		self.ParametersList = [ParametersInput(self.ParametersInputsFrame, 0),]

		self.AddParametersButton = Button(self.ParametersButtonFrame, text='+ Add', command=self.add_parameters_input)
		self.AddParametersButton.pack()
			
			# Request Body
		self.BodyInputsFrame = Frame(self.RequestBodyFrame)
		self.BodyInputsFrame.pack()
		self.BodyButtonFrame = Frame(self.RequestBodyFrame)
		self.BodyButtonFrame.pack()

		self.BodyList = [ParametersInput(self.BodyInputsFrame, 0),]
		
		self.AddBodyButton = Button(self.BodyButtonFrame, text='+ Add', command=self.add_body_input)
		self.AddBodyButton.pack()

			# Request Headers
		#

		# RESPONSE FRAME -> all the data from the response.
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
		#self.UrlInput.bind("<Return>", lambda e: self.RequestButton.invoke())

		# Loop
		self.root.mainloop()


	def pack_all(self):
		self.RequestFrame.pack(side=LEFT)
		self.ResponseFrame.pack(side=RIGHT)

		for child in self.RequestFrame.winfo_children():
			child.pack()

		#for child in self.ResponseFrame.winfo_children():
		#	child.pack()


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