import kivy

kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout


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
		item.add_widget(Label(text='Very big content\n' * 10))
		menu.add_widget(item)
		## The second accordion tab graphs data and saves to excel
		item = AccordionItem(title='Results')
		item.add_widget(Label(text='Very big content\n' * 10))
		menu.add_widget(item)
		## Add the accordion to the main screen
		root.add_widget(menu)
		
		return root

if __name__ == "__main__":
	hp4156cApp().run()
