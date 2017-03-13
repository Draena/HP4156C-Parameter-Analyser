#!/var/run/python
# Agilent Parameter Analyser Sweep function script.
import sys
import io
import visa
###############################################
## Class definitions and defines
###############################################
from hp4156c import hp4156c
###############################################
## Code starts here
###############################################
##devices = visa.get_instruments_list() # load all gpib devices into a list
##for x in range(0,len(devices)):
##        # Iterate through devices
##        # If the parameter analyser is found stop iterating
##        # If the parameter analyser is not found exit script
##	try:
##		pa = visa.instrument(devices[x])
##		name = pa.ask("*IDN?")
##		if(name == "HEWLETT-PACKARD,4156C,0,03.04:04.05:01.00"):
##			print("Found Device %s"% name)
##			break
##	except:
##		print("Could not connect to device %s"%devices[x])
##if(name != "HEWLETT-PACKARD,4156C,0,03.04:04.05:01.00"):
##	print("Could not find the parameter analyser.")
##	print("Exiting.")
##	sys.exit()
##else:
##        print("Connected.")
##pa.write("*RST") #reset

# Variables
paMode = "SAMPLE"
paIntTime = "SHORT"
# Start of Code
# Initialise the device
device = hp4156c()
print(device.error())
device.reset()
print(device.error())
## Setup the device for a Diode Measurement
device.measurementMode("SWEEP","SHORT")
print(device.error())
device.smu("SMU1",["VF","VAR1","IF","V"])
print(device.error())
device.smu("SMU3",["V","CONS","I","COMM"])
print(device.error())
device.disableSmu(["SMU2","SMU4"])
print(device.error())
device.var("VAR1",["LIN","DOUB","-1","0.1","1.0","100e-3"])
print(device.error())
device.visualise(["Voltage","1","-1","1"], ["Current","1","-0.1","0.1"])
print(device.error())
device.single()
print(device.error())
dataReturned = device.daq(["VF","IF"])
print(device.error())
print(device.data)
print(device.error())
device.save_data()
