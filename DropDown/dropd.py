import kivy
kivy.require('1.7.2') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

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
	def removeButtonPressed(self):
		self.dropdown.remove_widget(self)
		self.dropdown.clear_widgets()
		return
	def addButtonPressed(self):
		self.dropdown = DropDown()
		notes = ['Features', 'Suggestions', 'Abreviations', 'Miscellaneous']
		for note in notes:
			btn = Button(text=note, size_hint_y=None, height=20)
			btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
			self.dropdown.add_widget(btn)
			self.ids.btn_release.bind(on_release=self.dropdown.open)
		self.dropdown.bind(on_select=lambda instance, x: setattr(self.ids.btn_release, 'text', x))
		return
	def btn_releaseClicked(self):
		self.ids.btn_release.text="clicked"
	def btn_versionClicked(self):
		self.ids.btn_version.text="clicked"
	def btn_deviceClicked(self):
		self.ids.btn_device.text="clicked"
class dropdApp(App):
	def build(self):
		return HomeScreen()
if __name__ == '__main__':
	dropdApp().run()