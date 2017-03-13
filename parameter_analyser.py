#!/var/run/python
# Agilent Parameter Analyser Sweep function script.
import sys
import io
import visa
import os
###############################################
## Class definitions and defines
###############################################
from hp4156c import hp4156c
###############################################
## Code starts here
###############################################

def fetsweep(fname="test.csv",savedir=""):

    # Initialise the device
    device = hp4156c()
    print(device.error())
    device.reset()
    print(device.error())
    ## Setup the device for a Diode Measurement
    device.measurementMode("SWEEP","MEDIUM")
    print(device.error())
    device.smu("SMU1",["VS","CONS","IS","COMM"])
    print(device.error())
    device.smu("SMU2",["VDS","VAR2","ID","V"])
    print(device.error())
    device.smu("SMU3",["VG","VAR1","IG","V"])
    print(device.error())
    device.disableSmu(["SMU4"])
    print(device.error())
    device.var("VAR1",["LIN","DOUB","-10","0.1","10.0","1e-3"])
    print(device.error())
    device.var("VAR2",["LIN","SING","0.1","0","1","1e-3"])
    print(device.error())
    device.visualiseTwoYs(["VG","1","-10","10"], ["IDS","1","-1e-8","1e-8"],["IG","1","-1e-8","1e-8"])
    print(device.error())
    device.single()

    dataReturned = device.daq(['VG', 'VDS', 'ID', 'IG'])
    print(device.error())
    print(device.data)
    print(device.error())
    device.save_data(fname=os.path.join(savedir,fname))

def diodesweep():
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
    #for saving
    #device.save_data(fname='test.csv')



if __name__ == "__main__":
    diodesweep()
