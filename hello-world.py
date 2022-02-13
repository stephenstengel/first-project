#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  hello-world.py

# MIT License
# Copyright (c) <2021> <stephen.stengel@cwu.edu>

# This is a test program using glade and gtk through pygobject

import gi
gi.require_version("Gtk", "3.0")
##Gdk is needed to change background color, GLib is for setting a timer
from gi.repository import Gtk, Gdk, GLib #, GdkPixbuf#GdkPixbuff is not needed now?! im confused!

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
	whichJigglypuffGif = 0
	currentPath = ""


	#Initialize fields.
	def __init__(self):
		self.whichJigglypuffGif = -1
		self.jigglypuff_increment()


	#The event function for the play music button. It creates an ogg123
	#process and saves the ID. Also, it starts playing a jigglypuff gif.
	def button1_clicked(self, button):
		print("Start music button pressed!")
		if self.myProcess is None:
			self.myProcess = subprocess.Popen(["ogg123", "james-brown-dead.ogg", "-r", "-q"])
			print("Process ID: " + str(self.myProcess.pid))
			self.renderJigglypuffFrame()
			self.jigglypuff_increment()

		#Increase spinny speed if pressed multiple times. Name change might be prudent.?
		if self.playButtonPressCounter == 0:
			self.start_timer()
		self.playButtonPressCounter += 1
		stop_button.set_sensitive(True)


	#The event function for the stop music button. It stops the music
	#and hides jigglypuff.
	def music_stop_clicked_cb(self, button):
		print("Stop button pressed!")
		if self.myProcess is not None:
			print("Killing this process: " + str(self.myProcess.pid))
			kill(self.myProcess.pid, signal.SIGKILL)
			self.myProcess = None
		self.stop_timer()
		self.playButtonPressCounter = 0
		Gtk.Image.clear(jigglypuff)
		stop_button.set_sensitive(False)


	#The rave button!!!!!!!1 WOOOOOOOOOO!!!1!+shift1!!!
	def rave_button_clicked_cb(self, button):
		print("Rave button clicked!")
		self.changeBackgroundColor()
		self.spinText()
		

	#The function that is called when the timer times out.
	def on_timeout(self, *args, **kwargs):
		if self.timeout_id is not None:
			self.changeBackgroundColor()
			self.spinText()
			return True
		else:
			return False


	#Increments the jigglypuff gif that will be played.
	def jigglypuff_increment(self):
		self.whichJigglypuffGif += 1
		self.whichJigglypuffGif %= 5
		self.currentPath = "jigglypuff-gifs/" + str(self.whichJigglypuffGif + 1) + ".gif"


	#Play the current jigglypuff gif.
	def renderJigglypuffFrame(self):
		myPath = self.currentPath
		jigglypuff.set_from_file(myPath)


	#Starts the rave color changing timer. I used 114ms because it
	#matches up with the music.
	def start_timer(self):
		self.timeout_id = GLib.timeout_add(114, self.on_timeout, None)


	#Stops the rave timer. Called from music_stop_clicked_cb()
	def stop_timer(self):
		if self.timeout_id:
			GLib.source_remove(self.timeout_id)
			self.timeout_id = None


	#Changes the background color whenever you type on the keyboard.
	def myWindow_key_press_event(self, a, b):
		print("key-press-event has happened!")
		self.changeBackgroundColor()
		self.spinText()


	#This function picks a random background color to change to and
	#changes to it. I made sure to alternate between light and dark with
	#every call to give more strobe effect.
	def changeBackgroundColor(self):
		r, g, b = random.random(), random.random(), random.random()
		if self.currentBrightness == 1.0:
			self.currentBrightness = 0.5
		else:
			self.currentBrightness = 1.0

		theWindowLol = builder.get_object("myWindow")
		theWindowLol.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(r, g, b, self.currentBrightness)) #depricated call
		# ~ print(dir(theWindowLol.props))


	#This updates the angle of the spinning text.
	def spinText(self):
		adjustedCounter = None
		if self.playButtonPressCounter == 0:
			adjustedCounter = 1
		else:
			adjustedCounter = self.playButtonPressCounter
		angleIncrement = 6 * adjustedCounter
		self.label1Angle = (self.label1Angle - angleIncrement) % 360
		label1.set_angle(self.label1Angle)


#The main startup bit. I don't know how to put it into a function yet.
#The call to Handler() keeps being recursive.
builder = Gtk.Builder()
builder.add_from_file("glade-button.glade")
builder.connect_signals(Handler())

start_button = builder.get_object("music_start")
start_button.set_label("Play the music!")

stop_button = builder.get_object("music_stop")
stop_button.set_label("Stop the music!")
stop_button.set_sensitive(False)

rave_button = builder.get_object("rave_button")
rave_button.set_label("Change color!")

label1 = builder.get_object("label1")

window = builder.get_object("myWindow")

jigglypuff = builder.get_object("Jigglypuff")

window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()
