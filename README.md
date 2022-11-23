# Easy REST Tester

_version: MVP_

Test your REST API with an easy app.

Made in Python3 with TKinter.

## How to install

There isn't a way to install (at the moment). You'll need to clone this repository and use the Python interpreter, opening the _'main.py'_ file.

## How to use it?

The objective of **ERT** (Easy REST Tester) is to be simple, intuitive and really fast to use.

The UI is divided in two sections: the **'REQUEST'** (left part) and the **'RESPONSE'** (right part).

### REQUEST

- **Method**: select one of the HTTP verbs.
- **URL**: write the correct URL. You don't need to add any parameter for the instance, **ERT** will do it for you.
- **Request** button: click when you have typed the URL.
- **Parameters** & **Body**: you can add some parameters or body-data more clearly.

#### Parameters

If you want to send some parameters on the URL don't write them by the _URL entry input_: use the **Parameters** list inputs.

You can add all the parameters you need and can activate or deactivate by the adjacently checbox.

ERT will prepare the new URL with all the parameters correctly. Just click _'Request'_.

#### Body

It's the same way as _'Parameters'_. If you need to send body-data (as a _HTML form_) use these inputs and activate them by the adjacently checbox.

### RESPONSE

When the _'Request'_ button is clicked, **ERT** will send the request and show the response divided in two parts:

- **Body**: all the HTML or JSON content.
- **Headers**: the _headers_ of the response.

## You wanna help?

I'll be glad to recive all advices, tips and any corrections of this project.

I really hope it can be useful for our REST projects.