# ~ MIT License
# ~ Copyright (c) <2021> <stephen.stengel@cwu.edu>

#This is a test program using glade and gtk through pygobject

import gi
gi.require_version("Gtk", "3.0")
##Gdk is needed to change background color, GLib is for setting a timer
from gi.repository import Gtk, Gdk, GLib 

from os import kill
import random
import subprocess
import signal

class Handler:
	myProcess = None
	currentBrightness = 1.0
	flashCount = 0
	label1Angle = 0
	timeout_id = None
	playButtonPressCounter = 0
	jigglypuffCounter = 0
	whichJigglypuff = 0
	
	def button1_clicked(self, button):
		print("Start music button pressed!")
		if self.myProcess is None:
			self.myProcess = subprocess.Popen(["ogg123", "james-brown-dead.ogg", "-r", "-q"])
			print("Process ID: " + str(self.myProcess.pid))
		# ~ start_button.set_sensitive(False) ##Can use these things to toggle on/off
		if self.playButtonPressCounter <= 10:
			self.playButtonPressCounter += 1
			self.start_timer()
		
	def music_stop_clicked_cb(self, button):
		print("Stop button pressed!")
		if self.myProcess is not None:
			print("Killing this process: " + str(self.myProcess.pid))
			kill(self.myProcess.pid, signal.SIGKILL)
			self.myProcess = None
		self.stop_timer()
		self.playButtonPressCounter = 0
		# ~ jigglypuff.set_from_file("initial-image.png")
		# ~ gtk_image_clear(jigglypuff)
		# ~ Gtk.Image.clear(jigglypuff)
		self.whichJigglypuff += 1
		self.whichJigglypuff %= 5
	
	def rave_button_clicked_cb(self, button):
		print("Rave button clicked!")
		self.changeBackgroundColor()
		# ~ self.start_timer()
		# ~ self.jigglypuff_increment()
		

	def on_timeout(self, *args, **kwargs):
		self.jigglypuff_increment()
		if self.timeout_id is not None:
			self.changeBackgroundColor()
			return True
		else:
			return False


	
	def jigglypuff_increment(self):
		self.jigglypuffCounter += 1
		self.jigglypuffCounter %= 4
		if self.whichJigglypuff == 0:
			pathlol = "jigglypuff-pics/one/"
		elif self.whichJigglypuff == 1:
			pathlol = "jigglypuff-pics/two/"
		elif self.whichJigglypuff == 2:
			pathlol = "jigglypuff-pics/three/"
		elif self.whichJigglypuff == 3:
			pathlol = "jigglypuff-pics/four/"
		elif self.whichJigglypuff == 4:
			pathlol = "jigglypuff-pics/five/"
		self.renderJigglypuffFrame(pathlol)
			
	def renderJigglypuffFrame(self, myPath):
		if self.jigglypuffCounter == 0:
			jigglypuff.set_from_file(myPath + "0.png")
		elif self.jigglypuffCounter == 1:
			jigglypuff.set_from_file(myPath + "1.png")
		elif self.jigglypuffCounter == 2:
			jigglypuff.set_from_file(myPath + "2.png")
		elif self.jigglypuffCounter == 3:
			jigglypuff.set_from_file(myPath + "3.png")
	
	#copied from other thing
	def start_timer(self):
		# ~ self.timeout_id = GLib.timeout_add(100, self.on_timeout, None)
		# ~ self.timeout_id = GLib.timeout_add(500, self.on_timeout, None)
		# ~ self.timeout_id = GLib.timeout_add(455, self.on_timeout, None)
		# ~ self.timeout_id = GLib.timeout_add(227, self.on_timeout, None)
		# ~ self.timeout_id = GLib.timeout_add(152, self.on_timeout, None)
		self.timeout_id = GLib.timeout_add(114, self.on_timeout, None)

	def stop_timer(self):
		if self.timeout_id:
			GLib.source_remove(self.timeout_id)
			self.timeout_id = None
		Gtk.Image.clear(jigglypuff)
		Gtk.Image.clear(jigglypuff)
		Gtk.Image.clear(jigglypuff)
		Gtk.Image.clear(jigglypuff)
		
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
		# ~ self.label1Angle = (self.label1Angle - 22.5) % 360
		self.label1Angle = (self.label1Angle - 6) % 360
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
# ~ label1.set_angle(0)
# ~ label1.set_label("Test label!")

myViewport = builder.get_object("myViewport")

window = builder.get_object("myWindow")
# ~ window.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1)) #depricated call

jigglypuff = builder.get_object("Jigglypuff")


window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
