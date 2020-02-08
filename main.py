import sys
sys.path.append("/".join(x for x in __file__.split("/")[:-1]))
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition

from specialbuttons import ImageButton, LabelButton, ImageButtonSelectable
from functools import partial
from os import walk
from datetime import datetime

import kivy.utils
from kivy.utils import platform
import requests
import json
import traceback
from kivy.graphics import Color, RoundedRectangle





class HomeScreen(Screen):
    pass

class LoginScreen(Screen):
	pass

class MainApp(App):
	def build(self):
		return Builder.load_file("main.kv")
	def change_screen(self,screen_name):
		screen_manager = self.root.ids['screen_manager']
		screen_manager.current = screen_name
		print(self.root.ids)

MainApp().run()
