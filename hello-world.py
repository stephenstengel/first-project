# ~ MIT License
# ~ Copyright (c) <2021> <stephen.stengel@cwu.edu>

#This is a test program using glade and gtk through pygobject

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk ##Gdk is needed to change background color?

from os import kill
import random
import subprocess
import signal

class Handler:
	myProcess = None
	currentBrightness = 1.0
	flashCount = 0
	label1Angle = 45
	
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
		self.changeBackgroundColor()
		
	def myWindow_key_press_event(self, a, b):
		# ~ print("a: " + str(a))
		# ~ print("b: " + str(b))
		# ~ print("window: " + str(window))
		# ~ a: <Gtk.Window object at 0x7f69c57c1f30 (GtkWindow at 0x2564280)>
		# ~ b: <Gdk.EventKey object at 0x7f69c57bdef8 (void at 0x277c460)>
		# ~ window: <Gtk.Window object at 0x7f69c57c1f30 (GtkWindow at 0x2564280)>

		print("key-press-event has happened!")
		self.changeBackgroundColor()


	def changeBackgroundColor(self):
		r, g, b = random.random(), random.random(), random.random()
		if self.currentBrightness == 1.0:
			self.currentBrightness = 0.5
		else:
			self.currentBrightness = 1.0
		
		#change angle too lol
		self.label1Angle = (self.label1Angle - 22.5) % 360
		label1.set_angle(self.label1Angle)

		##Need to get window or builder better.
		theWindowLol = builder.get_object("myWindow")
		# ~ print(dir(theWindowLol.props))
		
		theWindowLol.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(r, g, b, self.currentBrightness)) #depricated call
		# ~ window.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(r, g, b, self.currentBrightness)) #depricated call
		# ~ print("currentBrightness: " + str(self.currentBrightness))
		
		
		
		

# ~ widget = Gtk.Box()
# ~ print(dir(widget.props))

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
label1.set_angle(45)
# ~ label1.set_label("Test label!")

myViewport = builder.get_object("myViewport")

window = builder.get_object("myWindow")
# ~ window.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1)) #depricated call


window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
