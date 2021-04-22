# johnny-django-docker

johnny-django-docker is a django application created by Paul Lunn for the Johnny project at the Open University, Milton Keynes, UK.

URL for johnny-django-docker - https://github.com/open-university-rse/johnny-django-docker
URL for johnny-code-logger - https://github.com/open-university-rse/johnny-code-logger


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

# Images from demo

![vscode](https://user-images.githubusercontent.com/72147267/115699141-4af83a80-a35d-11eb-9f84-8b99264fd18c.png)
![slack_integration](https://user-images.githubusercontent.com/72147267/115699165-52b7df00-a35d-11eb-8666-d0b659449df2.png)
![django_metrics_display](https://user-images.githubusercontent.com/72147267/115699193-58adc000-a35d-11eb-9690-b859dcb9460d.png)
![django_user_history](https://user-images.githubusercontent.com/72147267/115699220-5d727400-a35d-11eb-8381-dbe05cc41469.png)
![django_database_dashboard](https://user-images.githubusercontent.com/72147267/115699240-619e9180-a35d-11eb-81de-8b3dded974c0.png)
