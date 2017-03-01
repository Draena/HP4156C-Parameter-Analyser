# HP4156C-Parameter-Analyser
Python scripts and control software for the HP4156C Parameter Analyser


# hp4156c.py

This is the class for controlling the hp4156c parameter analyser.
It utilises pyvisa for GPIB control, and is implemented using the 
hp4156 ASCII SCPI command set. This allows simple control using
text based commands that mimic the HP4156C control panel.
refer to the Agilent 4155B/4156B GPIB Command reference, Edition 4.

_initialise
	the initialise object runs through all visa devices detected
	on the system. It searches for _deviceName which is the gpib
	id of the parameter analyser. This code should be modified to
	allow input of the parameter analyser id in code if required.
	It exits the script if no parameter analyser id is found.
	It relays this to the command prompt.
# main.py

Main python script for creating a gui to control the hp4156c parameter
analyser.

# hp4156c.kv

Kivy code for setting up the gui

# parameter_analyser.py

Test script for controlling the hp4156c using the hp4156c.py class.
Eventually this should be expanded to cover all test conditions,
and enable the hp4156c.py class to operate without producing 
device errors.

# graphtest.py

code for testing graphical output of data results. This is a problem
as the main.py code does not update the graphical output correctly.
At the moment my theory on this is that the graph is updated in the
background and is overlayed by the refresh of the ui.
