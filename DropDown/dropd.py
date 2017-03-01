import kivy
kivy.require('1.7.2') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
"""
On initialisation of the three buttons we want to have all of them dropdown
boxes. When the first box has a specific property selected, this property is
removed from the selection options of all the other boxes. We can iterate through
the selection box options to determine which options we want to use.

init = ['Constant', 'Common', 'Variable 1', 'Disabled']
if for the other dropdown boxes variable 1 selected
	init = ['Constant', 'Common', 'Variable 2', 'Disabled']

"""
class HomeScreen(Screen):
	addButton = ObjectProperty(None)
	removeButton = ObjectProperty(None)
	top_layout = ObjectProperty(None)
	def __init__(self, *args, **kwargs):
		super(HomeScreen, self).__init__(*args, **kwargs)
	def resetBoxes(self):
		self.ids.btn_release.text = "Release"
		self.ids.btn_version.text = "Version"
		self.ids.btn_device.text = "Device"
		return
	# def removeButtonPressed(self):
		# # self.dropdown.remove_widget(self)
		# self.dropdown.clear_widgets()
		# btn = Button(text="HAI",size_hint_y=None, height=20)
		# self.dropdown.add_widget(btn)
		# return
	# def addButtonPressed(self):
		# self.dropdown = DropDown()
		# notes = ['Features', 'Suggestions', 'Abreviations', 'Miscellaneous']
		# for note in notes:
			# btn = Button(text=note, size_hint_y=None, height=20)
			# btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
			# self.dropdown.add_widget(btn)
			# self.ids.btn_release.bind(on_release=self.dropdown.open)
		# self.dropdown.bind(on_select=lambda instance, x: setattr(self.ids.btn_release, 'text', x))
		# return
		
	# To debug this code I need to have a status textbox that informs me of
	# The state of each buttons .text state and what this corresponds to
	# I have a sneaking suspicion that I'm not probing them properly.
	def btn_releaseClicked(self):
		self.dropdown = DropDown()
		self.dropdown.clear_widgets()
		if((self.ids.btn_release.text == "Variable 1" or self.ids.btn_version.text=="Variable 1" or self.ids.btn_device=="Variable 1") and self.ids.btn_release.text != "Variable 2" and self.ids.btn_version.text!="Variable 2" and self.ids.btn_device!="Variable 2"):
			notes = ['Disabled', 'Common', 'Constant', 'Variable 2']
		elif(self.ids.btn_release.text == "Variable 2" or self.ids.btn_version.text=="Variable 2" or self.ids.btn_device=="Variable 2"):
			notes = ['Disabled', 'Common', 'Constant']
		else:
			notes = ['Disabled', 'Common', 'Constant', 'Variable 1']
		for note in notes:
			btn = Button(text=note, size_hint_y=None, height=20)
			btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
			self.dropdown.add_widget(btn)
			self.ids.btn_release.bind(on_release=self.dropdown.open)
		self.dropdown.bind(on_select=lambda instance, x: setattr(self.ids.btn_release, 'text', x))
		return
	def btn_versionClicked(self):
		self.dropdown = DropDown()
		self.dropdown.clear_widgets()
		if((self.ids.btn_release.text == "Variable 1" or self.ids.btn_version.text=="Variable 1" or self.ids.btn_device=="Variable 1")
			and self.ids.btn_release.text != "Variable 2" and self.ids.btn_version.text!="Variable 2" and self.ids.btn_device!="Variable 2"):
			notes = ['Disabled', 'Common', 'Constant', 'Variable 2']
		elif(self.ids.btn_release.text == "Variable 2" or self.ids.btn_version.text=="Variable 2" or self.ids.btn_device=="Variable 2"):
			notes = ['Disabled', 'Common', 'Constant']
		else:
			notes = ['Disabled', 'Common', 'Constant', 'Variable 1']
		for note in notes:
			btn = Button(text=note, size_hint_y=None, height=20)
			btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
			self.dropdown.add_widget(btn)
			self.ids.btn_version.bind(on_release=self.dropdown.open)
		self.dropdown.bind(on_select=lambda instance, x: setattr(self.ids.btn_version, 'text', x))
		return
	def btn_deviceClicked(self):
		self.dropdown = DropDown()
		self.dropdown.clear_widgets()
		if((self.ids.btn_release.text == "Variable 1" or self.ids.btn_version.text=="Variable 1" or self.ids.btn_device=="Variable 1")and self.ids.btn_release.text != "Variable 2" and self.ids.btn_version.text!="Variable 2" and self.ids.btn_device!="Variable 2"):
			notes = ['Disabled', 'Common', 'Constant', 'Variable 2']
		elif(self.ids.btn_release.text == "Variable 2" or self.ids.btn_version.text=="Variable 2" or self.ids.btn_device=="Variable 2"):
			notes = ['Disabled', 'Common', 'Constant']
		else:
			notes = ['Disabled', 'Common', 'Constant', 'Variable 1']
		for note in notes:
			btn = Button(text=note, size_hint_y=None, height=20)
			btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
			self.dropdown.add_widget(btn)
			self.ids.btn_device.bind(on_release=self.dropdown.open)
		self.dropdown.bind(on_select=lambda instance, x: setattr(self.ids.btn_device, 'text', x))
		return
class dropdApp(App):
	def build(self):
		return HomeScreen()
if __name__ == '__main__':
	dropdApp().run()