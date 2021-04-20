# johnny-django-docker

johnny-django-docker is a django application created by Paul Lunn for the Johnny project at the Open University, Milton Keynes, UK.

URL for johnny-django-docker - https://stem-ts-gitlab.open.ac.uk/pl4742/johnny-django-docker
URL for johnny-code-logger - https://stem-ts-gitlab.open.ac.uk/pl4742/johnny-code-logger

# Set up

This plug in works in tandem with johnny-code-logger which sends REST API requests to this data base.
Most actions related to django and docker can be implemented by using the python extension doit.py, please see dodo.py for all commands available. A dummy set of data can be created by using the "doit dummy" command.

# How this works

This extension will receive the following data and stores it in a table:

* Copy of any python source file that is saved
* The contents of the clipboard when ever a paste occurs
* A copy of the users firefox browser history

When a python file is received the contents are stored and several static analysis tools (Bandit, Prospector, radon) are run on the code and saved to the data base.

# Future work

It was intended to create a machine laerning interface which takes the static anaysis tools, clipboard contents, and website history as inputs to the learning set.