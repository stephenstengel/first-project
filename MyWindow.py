#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  MyWindow.py
#  
#  Copyright 2022 Stephen Stengel <stephen.stengel@cwu.edu>
#  

#The class for creating the window.

import gi
gi.require_version("Gtk", "3.0")
##Gdk is needed to change background color, GLib is for setting a timer
from gi.repository import Gtk

from Handlers import Handlers


class MyWindow(Gtk.Window):
	def __init__(self):
		super().__init__(title = "RAVE TIME!")

		builder = Gtk.Builder()
		builder.add_from_file("glade-button.glade")
		
		#I'm going to make a list of all the objects that Handlers()
		#needs to know about.
		jigglypuff = builder.get_object("Jigglypuff")
		
		start_button = builder.get_object("music_start")
		start_button.set_label("Play the music!")
		
		stop_button = builder.get_object("music_stop")
		stop_button.set_label("Stop the music!")
		stop_button.set_sensitive(False)
		
		rave_button = builder.get_object("rave_button")
		rave_button.set_label("Change color!")
		
		label1 = builder.get_object("label1")
		
		window = builder.get_object("myWindow")
		window.connect("destroy", Gtk.main_quit)
		
		myHandlers = Handlers(jigglypuff, stop_button, label1, window)
		builder.connect_signals(myHandlers)
		
		window.show_all()
