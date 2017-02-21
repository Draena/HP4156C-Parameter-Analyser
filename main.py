import kivy

kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.graph import Graph, MeshLinePlot
from kivy.properties import ObjectProperty, StringProperty
from math import sin

class Configuration(TabbedPanel):
	# The configuration accordion tab needs the following
	# Three tab options to select between sample sweep and qscv
	# A list of pre defined configuration options for Vds Vg and Id measurements
	# The ability to perform Hannah's long term time measurements (hack version)
	# 
	# To achieve these things we need to have the ability to setup SMU and VDU.
	# We need the ability to program the graphical display, which also will provide
	# input into our graphical results screen.
	
	# SMU setup passes parameters based on if the unit is a constant / variable or common connection
	# Therefore this setting is very important, drop down box recommended.
	# SMU #X [Cons/Var/Comm/Disabled] -> Populate rest of line based on selection
	# Const -> Voltage value and compliance value
	# Variable -> Start Step End compliance
	# Comm -> compliance value
	# disabled don't enable SMU
	#smu_dropdown = ObjectProperty(None)
	smu1_select = ObjectProperty(None)
	# If one of smu1 to smu 4 has variable 1 selected, then remove from menu
	# If one of smu1 to smu 4 has variable 1 selected, then add variable 2 to menu
	# For sweep mode need at least one variable before can continue.
	def smu1_text_update(self, text):
		self.smu1_select.text = '%s' % text 
		if text == "Disabled":
			#self.smu1_text1.readonly = True
			self.smu1_text1.disabled = True
			self.smu1_text2.disabled = True
			self.smu1_text3.disabled = True
			self.smu1_text4.disabled = True
			self.smu1_text5.disabled = True
			self.smu1_text6.disabled = True
			# Import visa command disablesmu()
		if text == "Constant":
			self.smu1_text1.disabled = True
			self.smu1_text2.disabled = True
			self.smu1_text3.disabled = True
			self.smu1_text4.disabled = False
			self.smu1_text4.text = "Value"
			self.smu1_text5.disabled = False
			self.smu1_text5.text = "Compliance"
			self.smu1_text6.disabled = True
			# Import visa command smu()
		if text == "Variable":
			self.smu1_text1.disabled = True
			self.smu1_text1.text = "Vname"
			self.smu1_text2.disabled = True
			self.smu1_text2.text = ""
			self.smu1_text3.disabled = True
			self.smu1_text4.disabled = True
			self.smu1_text4.text = "Value"
			self.smu1_text5.disabled = True
			self.smu1_text5.text = "Compliance"
			self.smu1_text6.disabled = True
		if text == "Common":
			self.smu1_text1.disabled = True
			self.smu1_text2.disabled = True
			self.smu1_text3.disabled = True
			self.smu1_text4.disabled = True
			self.smu1_text4.text = "0"
			self.smu1_text5.disabled = True
			self.smu1_text5.text = "Compliance"
			self.smu1_text6.disabled = True

	pass
	# This window also could have a write to excel with a directory box, and check or uncheck
	# If the graphical functionality is required. I.E all measurements could be conducted
	# without transitioning to the results accordion if required.

	
#class ConfigurationHeader(tabbedpanel):
	
# There also would be room in here for an accordion tab that allows automation of multiple
# test routines to allow the device to constantly measure various parameters over an
# extended time period. This could be very powerful for device analysis without being
# stuck on the parameter analyser.
class Results(BoxLayout):
	# This results accordion tab needs to graphically display the results of measurements
	# It passes this information from the result of a parameter analyser test run
	# Using numpy and scipy it is possible to graphically display the returned values
	# Saving them to an excel file and also downloading them from the device.
	graph = ObjectProperty(None)
	# graph.add_plot()
	#plot = MeshLinePlot(color=[1,0,0,1])
	#plot.points = [(x,sin(x/10.)) for x in range(0,101)]
	#graph.add_plot(plot)
	def plot_data(self):
		plot = MeshLinePlot(color=[1,1,0,1])
		self.plot.points = [(x,sin(x/10.)) for x in range(0,101)]
		self.graph.add_plot(plot)
	pass
	
class hp4156cApp(App):
	def build(self):
		self.title = "HP4156C Parameter Analyser"
		## Main screen has a title and two accordions
		root = BoxLayout(orientation='vertical')
		## Add a title header to the window
		header = Label(text="HP4156C Parameter Analyser", font_size=20, size_hint_y=None, height=25)
		root.add_widget(header)
		## The main Accordion menu
		menu = Accordion()
		## The second accordion tab graphs data and saves to excel
		item = AccordionItem(title='Results')
		results = BoxLayout(orientation='vertical')
		# results.add_widget(Label(text="Graphical Results Display"))
		## Add a title header to the window
		#graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5, x_ticks_major=25, y_ticks_major=1,y_grid_label=True, x_grid_label=True, padding=5, x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)
		#plot = MeshLinePlot(color=[1, 0, 0, 1])
		#plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
		#graph.add_plot(plot)
		#results.add_widget(graph)
		item.add_widget(Results())
		#item.add_widget(graph)
		menu.add_widget(item)
		## The first accordion tab has three buttons
		item = AccordionItem(title='Configuration')
		item.add_widget(Configuration())
		menu.add_widget(item)
		## Add the accordion to the main screen
		root.add_widget(menu)
		return root
	

## Main program execution here
if __name__ == "__main__":
	hp4156cApp().run()
