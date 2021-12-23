# ~ MIT License
# ~ Copyright (c) <2021> <stephen.stengel@cwu.edu>

#This is a test program using glade and gtk through pygobject

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk ##Gdk is needed to change background color?
from os import system
from os import kill
from time import sleep
import random

import subprocess
import signal

class Handler:
	myProcess = None
	currentBrightness = 1.0
	flashCount = 0
	
	def button1_clicked(self, button):
		print("Start music button pressed!")
		if self.myProcess is None:
			self.myProcess = subprocess.Popen(["ogg123", "james-brown-dead.ogg", "-r", "-q"])
			print("Process ID: " + str(self.myProcess.pid))
		
	def music_stop_clicked_cb(self, button):
		print("Stop button pressed!")
		if self.myProcess is not None:
			print("Killing this process: " + str(self.myProcess.pid))
			kill(self.myProcess.pid, signal.SIGKILL)
			self.myProcess = None
	
	def rave_button_clicked_cb(self, button):
		print("Rave button clicked!")
		r, g, b = random.random(), random.random(), random.random()
		if self.currentBrightness == 1.0:
			self.currentBrightness = 0.5
		else:
			self.currentBrightness = 1.0

		##window just hangin there is not great. depends on script.
		##I think I saw a tutorial that used a class to contain the window setup.
		window.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(r, g, b, self.currentBrightness)) #depricated call
		print("currentBrightness: " + str(self.currentBrightness))
		
		
builder = Gtk.Builder()
builder.add_from_file("glade-button.glade")
builder.connect_signals(Handler())

start_button = builder.get_object("music_start")
start_button.set_label("Play the music!")

stop_button = builder.get_object("music_stop")
stop_button.set_label("Stop the music!")

rave_button = builder.get_object("rave_button")
rave_button.set_label("Change color!")

# ~ draw_area = builder.get_object("draw_area")
vol_slider = builder.get_object("volume_slider")
# ~ vol_slider.set_label("Volume! It isn't connected to anything yet.")

label1 = builder.get_object("label1")
# ~ label1.set_label("Test label!")

myViewport = builder.get_object("myViewport")

window = builder.get_object("myWindow")
# ~ window.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1)) #depricated call


window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
