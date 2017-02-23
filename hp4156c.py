#!/var/run/python
# Agilent Parameter Analyser Sweep function script.


# Import the HP4156C class

# The HP4156C class includes the metaclass visa

# This allows the HP4156C to wrap the visa class
# When wrapped the HP4156C class takes care of all the visa syntax
# and translates parameter analyser settings into visa commands
import sys,io,visa
deviceName = "HEWLETT-PACKARD,4156C,0,03.04:04.05:01.00"
_id = ""
class hp4156c(object):
       	def __init__(self):
		self._initialise()
	
	def _initialise(self):
		print("HP4156C Initialisation")
		_devices = visa.get_instruments_list()
		for _x in range(0,len(_devices)):
			try:
				self.pa = visa.instrument(_devices[_x])
				_id = self.pa.ask("*IDN?")
				if(_id == deviceName):
					print("Found device %s"%_id)
					break
			except:
				print("Could not connect to device %s"%_devices[_x])
		if(_id != deviceName):
			print("Could not find the parameter analyser.")
			print("Exiting.")
			sys.exit()
		else:
                        self.pa.write("*rst")
	def reset(self):
		self.pa.write("*rst")
		
	def measurementMode(self, mode, intTime):
		if(mode == "SWEEP" or mode == "SAMPLE" or mode == "QSCV") and (intTime == "SHORT" or intTime == "MEDIUM" or intTime == "LONG"):
			self.pa.write(":PAGE:CHAN:MODE " + mode)
			self.pa.write(":PAGE:MEAS:MSET:ITIM " + intTime)
		else:
			print("Invalid measurement mode or integration time. Exiting.")
			sys.exit()
        def _stringSmuMod(self,arg):
                arg[0] = "'" + arg[0] + "'"
                arg[2] = "'" + arg[2] + "'"
                return arg

        def smu(self, arg1, arg2):
                self.arg2 = self._stringSmuMod(arg2)
                self.smuSetup = [":PAGE:CHAN:"+arg1+":VNAME %s",":PAGE:CHAN:"+arg1+":FUNC %s",":PAGE:CHAN:"+arg1+":INAME %s",":PAGE:CHAN:"+arg1+":MODE %s",":PAGE:MEAS:CONS:"+arg1+" %s",":PAGE:MEAS:CONS:"+arg1+":COMP %s"]
                self.pa.write(self.smuSetup[0] %self.arg2[0])
                self.pa.write(self.smuSetup[1] %self.arg2[1])
                self.pa.write(self.smuSetup[2] %self.arg2[2])
                self.pa.write(":PAGE:DISP:LIST %s" % self.arg2[2])
                self.pa.write(self.smuSetup[3] %self.arg2[3])
                if arg2[1] != "VAR1" and arg2[1] != "VAR2" and arg2[3] != "COMM" and arg2[1] != "VAR1\'":
                        self.pa.write(self.smuSetup[4] % arg2[4])
                        self.pa.write(self.smuSetup[5] % arg2[5])

        def disableSmu(self,arg):
                for i in arg:
                        self.pa.write(":PAGE:CHAN:" + i + ":DIS")

        def _varStringMod(self, arg):
                arg[0] = "'" + arg[0] + "'"
                return arg
		## arg1 is the smu number
		## arg2 is the parameters for a sweep. [LIN:LOG SING:DOUB STAR STEP STOP COMP]
        def var(self, arg1, arg2):
                self.arg2 = self._varStringMod(arg2)
                self.string = ":PAGE:MEAS:" + arg1 + ":"
                if arg1 == "VAR1":
			self.pa.write(self.string + "SPAC %s" % self.arg2[0])
			self.pa.write(self.string + "MODE %s" % self.arg2[1])
			self.pa.write(self.string + "STAR %s" % self.arg2[2])
			self.pa.write(self.string + "STEP %s" % self.arg2[3])
			self.pa.write(self.string + "STOP %s" % self.arg2[4])
			self.pa.write(self.string + "COMP %s" % self.arg2[5])
			
		elif arg1 == "VAR2":
			self.pa.write(self.string + "SPAC %s" % self.arg2[0])
			self.pa.write(self.string + "MODE %s" % self.arg2[1])
			self.pa.write(self.string + "STAR %s" % self.arg2[2])
			self.pa.write(self.string + "POIN %s" % self.arg2[4])
			self.pa.write(self.string + "STEP %s" % self.arg2[3])
			self.pa.write(self.string + "COMP %s" % self.arg2[5])
        def _daqStringMod(self,arg):
                self.stuff = []
                for i in arg:
                        self.stuff.append("\'"+i+"\'")
                return self.stuff
##        def daq(self,arg):
##                self.argData = []
##                self.stuff = self._daqStringMod(arg)
##                for i in self.stuff:
##                        self.pa.write(":DATA? %s" %i)
##                        self.fluff = self.pa.read()
##                        self.argData.append(self.fluff[2:])
##                self.tempList=[]
##                for i in self.argData:
##                        self.t=i[0].split("\n")[0]
##                        self.temp=self.t.split(",")
##                        self.tempList.append(self.temp)
##                self.fluff = self.merger(self.tempList)
##                return self.fluff
        def daq(self, values):
                #self.data = self._daqStringMod(arg)
                self.data = []
                for x in range(0,len(values)):
                        try:
                                print("Obtaining %s data values" % values[x])
                                self.pa.write(":DATA? %s"%values[x])
                        except:
                                print("Command Timeout!")
                        _tempData = self.pa.read_values()
                        print("Obtained %d data values!"%len(_tempData))
                        _tempData.insert(0,"%s"%values[x])
                        if(self.data == []):
                                for i in xrange(len(_tempData)):
                                        self.data.append
                        self.data.append(_tempData)
                self.data = zip(*(self.data))
        def single(self):
                self.pa.write(":PAGE:SCON:SING")
                self.pa.write("*WAI")

        def visualiseTwoYs(self, x, y1, y2):
                self.x = self._varStringMod(x)
		self.y1 = self._varStringMod(y1)
		self.y2 = self._varStringMod(y2)
		self.pa.write(":PAGE:DISP:GRAP:GRID ON")
		self.pa.write(":PAGE:DISP:GRAP:X:NAME %s" % self.x[0])
		self.pa.write(":PAGE:DISP:GRAP:Y1:NAME %s" % self.y1[0])
		self.pa.write(":PAGE:DISP:GRAP:Y2:NAME %s" % self.y2[0])
		self.pa.write(":PAGE:DISP:GRAP:X:SCAL %s" % self.x[1])
		self.pa.write(":PAGE:DISP:GRAP:Y1:SCAL %s" % self.y1[1])
		self.pa.write(":PAGE:DISP:GRAP:Y2:SCAL %s" % self.y2[1])
		self.pa.write(":PAGE:DISP:GRAP:X:MIN %s" % self.x[2])
		self.pa.write(":PAGE:DISP:GRAP:Y1:MIN %s" % self.y1[2])
		self.pa.write(":PAGE:DISP:GRAP:Y2:MIN %s" % self.y2[2])
		self.pa.write(":PAGE:DISP:GRAP:X:MAX %s" % self.x[3])
		self.pa.write(":PAGE:DISP:GRAP:Y1:MAX %s" % self.y1[3])
		self.pa.write(":PAGE:DISP:GRAP:Y2:MAX %s" % self.y2[3])
		
        def visualise(self, x ,y1):
               	self.x = self._varStringMod(x)
		self.y1 = self._varStringMod(y1)
		self.pa.write(":PAGE:DISP:GRAP:GRID ON")
		self.pa.write(":PAGE:DISP:GRAP:X:NAME %s" % self.x[0])
		self.pa.write(":PAGE:DISP:GRAP:Y1:NAME %s" % self.y1[0])
		self.pa.write(":PAGE:DISP:GRAP:X:SCAL %s" % self.x[1])
		self.pa.write(":PAGE:DISP:GRAP:Y1:SCAL %s" % self.y1[1])
		self.pa.write(":PAGE:DISP:GRAP:X:MIN %s" % self.x[2])
		self.pa.write(":PAGE:DISP:GRAP:Y1:MIN %s" % self.y1[2])
		self.pa.write(":PAGE:DISP:GRAP:X:MAX %s" % self.x[3])
		self.pa.write(":PAGE:DISP:GRAP:Y1:MAX %s" % self.y1[3])
	def abort(self):
                pass
        def stress(self, term, func, mode, name, value=0.0, duration=0):
		"""
		Sets up the stress conditions for the 4156.
		Default duration is free-run, no time limit to applied stress.
		"""
		self.name=self._varStringMod(name)
		self.pa.write(":PAGE:STR:SET:DUR %s" % duration)
		self.pa.write(":PAGE:STR:%s:NAME %s" % (term,self.name))
		self.pa.write(":PAGE:STR:%s:FUNC %s" % (term,func))
		self.pa.write(":PAGE:STR:%s:MODE %s" % (term,mode))
		self.pa.write(":PAGE:STR:SET:CONS:%s %s" % (term,value))
		pass
	
	def merger(self, *lists):
		"""Combines any number of lists of equal length."""
		self.merged=[]
		for i in range(len(lists[0][0])):
			self.temp=[]
			for j in range(len(lists[0])):
				self.temp.append(lists[0][j][i])
			self.merged.append(self.temp)
		return self.merged
	def error(self):
                return self.pa.ask(":SYST:ERR?")
	# def smuSetup(self, arg1, arg2):
        #	def __init__(self): # device_name="HEWLETT-PACKARD,4156C,0,03.04:04.05:01.00"):
        #        self.device = self.visa.instrument("GPIB::02")
                # visa.instrument(self, "GPIB::02")
                #devices = visa.get_instruments_list() # load all gpib devices into a list
                #for x in range(0,len(devices)):
                        # Iterate through devices
                        # If the parameter analyser is found stop iterating
                        # If the parameter analyser is not found exit script
                #        try:
                #                pa = visa.instrument(devices[x])
                #                name = pa.ask("*IDN?")
                #                if(name == device_name):
                #                        print("Found Device %s"% name)
                #                        break
                #        except:
                #                print("Could not connect to device %s"%devices[x])
                #if(name != device_name):
                #        print("Could not find the parameter analyser.")
                #        print("Exiting.")
                #        sys.exit()
                #else:
                #        print("Connected.")
                # What do I want returned. I want to return the device connection
                # pa.write(":FORM:DATA ASCii")
                # pass
        #def idn(self):
        #       return self.visa.instrument("GPIB::02").ask("*IDN?") 
#       def rst(self):
#		pa.write("*RST")
#		pass
	
##	def measurementMode(self, arg1, arg2):
##		"""
##		arg1 is the measurement mode. Valid arguements are Sweep = SWE, Sampling = SAMP, Quasi-static CV measurement = QSCV.
##		
##		arg2 is the integration time. Valid arguments are short = SHOR, medium = MED, long = LONG.
##		"""
##		if (arg1 == "SWE" or arg1 == "SAMP" or arg1 == "QSCV") and (arg2 == "SHOR" or arg2 == "LONG" or arg2 == "MED"):
##			self.write(":PAGE:CHAN:MODE " + arg1)
##			self.write(":PAGE:MEAS:MSET:ITIM " + arg2)
##		else:
##			print "Invalid measurement mode or integration time. Exiting."
##			sys.exit()
##		pass
##
##	def stringSmuMod(self, arg):
##		"""
##		Method only called when appropriate, users don't need to modify their input. Generally I will know when it is appropriate to do this and do so accordingly.
##		"""
##		arg[0] = "'" + arg[0] + "'"
##		arg[2] = "'" + arg[2] + "'"
##		return arg
##			
##	
##	def smu(self, SMUnum, SMUparam):
##		# SMUnum is the desired SMU, ie SMU1, SMU2, etc, entered as a string variable. 
##		# SMUparam is the parameters for that SMU.
##		# ie smu1 = ['VD','CONS','ID','V','0.1','3mA']
##		# [Variable NAME, Variable FUNCtion(var, cons), INAME, MODE (V, I or COMMon)]
##		# if the variable is constant this requires a value CONStant ,COMPliance for the variable.
##		# Where each element is described after the [].
##		
##		self.arg2 = self.stringSmuMod(arg2)
##		self.smuSetup = [":PAGE:CHAN:"+arg1+":VNAME %s",":PAGE:CHAN:"+arg1+":FUNC %s",":PAGE:CHAN:"+arg1+":INAME %s", ":PAGE:CHAN:"+arg1+":MODE %s", ":PAGE:MEAS:CONS:"+ arg1 + " %s",":PAGE:MEAS:CONS:" + arg1 + ":COMP %s"]
##		self.write(self.smuSetup[0] % self.arg2[0])
##		self.write(self.smuSetup[1] % self.arg2[1])
##		self.write(self.smuSetup[2] % self.arg2[2])
##		self.write(":PAGE:DISP:LIST %s" % self.arg2[2])
##		self.write(self.smuSetup[3] % self.arg2[3])
##		if arg2[1] != "VAR1" and arg2[1] != "VAR2" and arg2[3] != "COMM" and arg2[1] != "VAR1\'":
##			self.write(self.smuSetup[4] % arg2[4])
##			self.write(self.smuSetup[5] % arg2[5])
##		pass
##
##	def disableSmu(self, SMUnum):
##		# Disables the specified unit:
##		# valid arguments are: VSU1, VSU2, VMU1, VMU2, SMU1, SMU2, SMU3, SMU4.
##		# Parameter SMUnum is a list of valid arguements.
##		for i in arg:
##			self.write(":PAGE:CHAN:" + i + ":DIS")
##		pass	
##
##        def varStringMod(self, arg):
##		# Method only called when appropriate, users don't need to modify their input. Generally I will know when it is appropriate to do this and do so accordingly.
##
##		arg[0] = "'" + arg[0] + "'"
##		return arg
##		
##	def var(self, arg1, arg2):
##		"""
##		Describes the measurement parameters for an independent variable, arg1, and its specifications arg2. 
##		
##		Similar to smu(), we have arg1 as the desired VAR, ie VAR1, VAR2, as a string input. If using VAR2, stop is replaced by number of points.
##		
##		arg2 describes several critical values of the VAR, ie var1 = ['\'LIN\'','-0.1','0.01','1.5','1nA']	# SPACing (LINear or LOGarithmic), STARting value, STEP size, STOPing value, COMPliance limit.
##		"""
##		self.arg2 = self.varStringMod(arg2)
##		self.string = ":PAGE:MEAS:" + arg1 + ":"
##		if arg1 == "VAR1":
##			self.write(self.string + "SPAC %s" % self.arg2[0])
##			self.write(self.string + "STAR %s" % self.arg2[1])
##			self.write(self.string + "STEP %s" % self.arg2[2])
##			self.write(self.string + "STOP %s" % self.arg2[3])
##			self.write(self.string + "COMP %s" % self.arg2[4])
##			
##		elif arg1 == "VAR2":
##			self.write(self.string + "SPAC %s" % self.arg2[0])
##			self.write(self.string + "STAR %s" % self.arg2[1])
##			self.write(self.string + "POIN %s" % self.arg2[3])
##			self.write(self.string + "STEP %s" % self.arg2[2])
##			self.write(self.string + "COMP %s" % self.arg2[4])
##		pass
##	
##	def daqStringMod(self, arg):
##		"""
##		Method only called when appropriate, users don't need to modify their input. Generally I will know when it is appropriate to do this and do so accordingly.
##		"""
##		self.stuff = []
##		for i in arg:
##			self.stuff.append("\'" + i + "\'")
##		return self.stuff
##	
##	def daq(self, arg):
##		"""
##		Queries the HP 4156A for data for specified data, and returns the data to an object.	
##		
##		arg is intended to be a object (tuple/list) of strings containing data of interest to the operator. example usage:
##		arg = ('VD','VS','VG','ID','IS','IG')
##		myData = daq(arg)
##		myData is then in a nice CSV accessible format.
##		"""
##		self.argData = []
##		self.stuff = self.daqStringMod(arg) # Fix this
##		for i in self.stuff:
##			self.write(":DATA? %s" % i)
##			self.fluff = self.read()
##			self.argData.append(self.fluff[2:])
##		self.tempList=[]
##		for i in self.argData:
##			self.t=i[0].split('\n')[0]
##			self.temp=self.t.split(',')
##			self.tempList.append(self.temp)
##		self.fluff = self.merger(self.tempList)
##		return self.fluff
##	
##	def single(self):
##		"""Performs a single sweep/measurement/thing."""
##		self.write(":PAGE:SCON:SING")
##		self.write("*WAI")
##		pass
##	
##	def visualizeTwoYs(self, x, y1, y2):
##		"""
##		Takes three list arguments ie:
##		
##		#x = ['XVAR','LIN',"XMIN","XMAX"]
##		#y1 = ['Y1VAR','LOG',"Y1MIN","Y1MAX"]
##		#y2 = ['Y2VAR','LOG',"Y2MIN","Y2MAX"]
##		
##		Visualizes two sets of data, y1 and y2.
##		"""
##		self.x = self.varStringMod(x)
##		self.y1 = self.varStringMod(y1)
##		self.y2 = self.varStringMod(y2)
##		self.write(":PAGE:DISP:GRAP:GRID ON")
##		self.write(":PAGE:DISP:GRAP:X:NAME %s" % self.x[0])
##		self.write(":PAGE:DISP:GRAP:Y1:NAME %s" % self.y1[0])
##		self.write(":PAGE:DISP:GRAP:Y2:NAME %s" % self.y2[0])
##		self.write(":PAGE:DISP:GRAP:X:SCAL %s" % self.x[1])
##		self.write(":PAGE:DISP:GRAP:Y1:SCAL %s" % self.y1[1])
##		self.write(":PAGE:DISP:GRAP:Y2:SCAL %s" % self.y2[1])
##		self.write(":PAGE:DISP:GRAP:X:MIN %s" % self.x[2])
##		self.write(":PAGE:DISP:GRAP:Y1:MIN %s" % self.y1[2])
##		self.write(":PAGE:DISP:GRAP:Y2:MIN %s" % self.y2[2])
##		self.write(":PAGE:DISP:GRAP:X:MAX %s" % self.x[3])
##		self.write(":PAGE:DISP:GRAP:Y1:MAX %s" % self.y1[3])
##		self.write(":PAGE:DISP:GRAP:Y2:MAX %s" % self.y2[3])
##		pass
##	
##	def visualize(self, x, y1):
##		"""
##		Takes two list arguments ie:
##		
##		x = ['XVAR','LIN',"XMIN","XMAX"]
##		y1 = ['Y1VAR','LOG',"Y1MIN","Y1MAX"]
##		
##		Visualizes a set of data, y1.
##		"""
##		self.x = self.varStringMod(x)
##		self.y1 = self.varStringMod(y1)
##		self.write(":PAGE:DISP:GRAP:GRID ON")
##		self.write(":PAGE:DISP:GRAP:X:NAME %s" % self.x[0])
##		self.write(":PAGE:DISP:GRAP:Y1:NAME %s" % self.y1[0])
##		self.write(":PAGE:DISP:GRAP:X:SCAL %s" % self.x[1])
##		self.write(":PAGE:DISP:GRAP:Y1:SCAL %s" % self.y1[1])
##		self.write(":PAGE:DISP:GRAP:X:MIN %s" % self.x[2])
##		self.write(":PAGE:DISP:GRAP:Y1:MIN %s" % self.y1[2])
##		self.write(":PAGE:DISP:GRAP:X:MAX %s" % self.x[3])
##		self.write(":PAGE:DISP:GRAP:Y1:MAX %s" % self.y1[3])
##		pass
##	
##	def abort(self):
##		pass
##	
##	def stress(self, term, func, mode, name, value=0.0, duration=0):
##		"""
##		Sets up the stress conditions for the 4156.
##		Default duration is free-run, no time limit to applied stress.
##		"""
##		self.name=self.varStringMod(name)
##		self.write(":PAGE:STR:SET:DUR %s" % duration)
##		self.write(":PAGE:STR:%s:NAME %s" % (term,self.name))
##		self.write(":PAGE:STR:%s:FUNC %s" % (term,func))
##		self.write(":PAGE:STR:%s:MODE %s" % (term,mode))
##		self.write(":PAGE:STR:SET:CONS:%s %s" % (term,value))
##		pass
##	
##	def merger(self, *lists):
##		"""Combines any number of lists of equal length."""
##		self.merged=[]
##		for i in range(len(lists[0][0])):
##			self.temp=[]
##			for j in range(len(lists[0])):
##				self.temp.append(lists[0][j][i])
##			self.merged.append(self.temp)
##		return self.merged
##	
##	# Check if the device has an error and report the error.
##	# An improvement on this could be to report the error in english
##	def errchk():
##		self.write(":SYST:ERR?")
##		errchk = self.read()
##	
##
##	
