#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Handlers.py
#  
#  MIT License
#  Copyright 2022 Stephen Stengel <stephen.stengel@cwu.edu>
#

import gi
gi.require_version("Gtk", "3.0")
##Gdk is needed to change background color, GLib is for setting a timer
from gi.repository import Gtk, Gdk, GLib

from os import kill
import random
import subprocess
import signal

import pygame.mixer as mixer


#exitProcess global variable is used to make sure that the music process gets killed when the window is closed.
#It is set to a value at the same time as self.myProcess.
#It is only read when the exit window button is pressed and the Gtk.main_quit function is about to be called.
#An alternate way would be to save the number to a file.
exitProcess = None

class Handlers():
	myProcess = None
	is_bright_phase = False
	flashCount = 0
	label1Angle = 0
	timeout_id = None
	playButtonPressCounter = 0
	whichJigglypuffGif = 0
	currentPath = ""
	jigglypuff = None
	stop_button = None
	label1 = None
	window = None
	is_deprecated_been_printed = False
	is_playing = False


	#Initialize some fields.
	def __init__(self, jigglypuff, stop_button, label1, window):
		mixer.init()
		mixer.music.load("james-brown-dead.ogg")
		self.whichJigglypuffGif = -1
		self.jigglypuff_increment()

		self.jigglypuff = jigglypuff
		self.stop_button = stop_button
		self.label1 = label1
		self.window = window


	#The event function for the play music button. It creates an ogg123
	#process and saves the ID. Also, it starts playing a jigglypuff gif.
	def button1_clicked(self, button):
		print("Start music button pressed!")
		if self.is_playing is False:
			mixer.music.play(loops = -1)
			self.renderJigglypuffFrame()
			self.jigglypuff_increment()
			self.is_playing = True

		#Increase spinny speed if pressed multiple times. Name change might be prudent.?
		if self.playButtonPressCounter == 0:
			self.start_timer()
		self.playButtonPressCounter += 1
		self.stop_button.set_sensitive(True)


	#The event function for the stop music button. It stops the music
	#and hides jigglypuff.
	def music_stop_clicked_cb(self, button):
		print("Stop button pressed!")
		mixer.music.stop()
		self.stop_timer()
		self.playButtonPressCounter = 0
		Gtk.Image.clear(self.jigglypuff)
		self.stop_button.set_sensitive(False)
		self.is_playing = False


	#This is used to stop the music from playing if the user closes the window during playback.
	def myDestroy(self):
		print("Exit window button pressed!")
		global exitProcess
		if exitProcess is not None:
			print("Killing this process: " + str(exitProcess.pid))
			kill(exitProcess.pid, signal.SIGKILL)


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
		self.jigglypuff.set_from_file(myPath)


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
		if self.is_bright_phase == False:
			#Set the color to be a little darker
			r = r - (r / 2)
			g = g - (g / 2)
			b = b - (b / 2)
			self.is_bright_phase = True
			
		else:
			#set the color to be a little brighter
			r = ((1 - r) / 2) + r
			g = ((1 - g) / 2) + g
			b = ((1 - b) / 2) + b
			self.is_bright_phase = False

		#depricated call
		if not self.is_deprecated_been_printed:
			print("\"override_background_color\" is depricated. " 
					"Try to find the new way to do it.")
			self.is_deprecated_been_printed = True
		self.window.override_background_color(
				Gtk.StateFlags.NORMAL,
				Gdk.RGBA(r, g, b, 1)) #Opacity should never change.


	#This updates the angle of the spinning text.
	def spinText(self):
		adjustedCounter = None
		if self.playButtonPressCounter == 0:
			adjustedCounter = 1
		else:
			adjustedCounter = self.playButtonPressCounter
		angleIncrement = 6 * adjustedCounter
		self.label1Angle = (self.label1Angle - angleIncrement) % 360
		self.label1.set_angle(self.label1Angle)
