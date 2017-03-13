import kivy

kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

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
	# http://stackoverflow.com/questions/38234848/kivy-dynamically-add-and-remove-dropdown-entries
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
			# Two variable commands, different input variations.
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
	def addButtonPressed(self):
		# If none of the variable buttons are selected then add them to the menu
		pass
	def removeButtonPressed(self):
		# If e
		self.dropdown.remove_widget(self)
		self.dropdown.clear_widgets()

#class ConfigurationHeader(tabbedpanel):

# There also would be room in here for an accordion tab that allows automation of multiple
# test routines to allow the device to constantly measure various parameters over an
# extended time period. This could be very powerful for device analysis without being
# stuck on the parameter analyser.


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

		## The first accordion tab has three buttons
		item = AccordionItem(title='Configuration')
		item.add_widget(Configuration())
		menu.add_widget(item)
		#the above section can be repeated to add more accordion items

		## Add the accordion to the main screen
		root.add_widget(menu)
		return root


## Main program execution here
if __name__ == "__main__":
	hp4156cApp().run()
