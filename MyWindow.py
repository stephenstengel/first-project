#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  MyWindow.py
#  
#  MIT License
#  Copyright 2022 Stephen Stengel <stephen.stengel@cwu.edu>
#  

#The class for creating the window.

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from Handlers import Handlers


class MyWindow(Gtk.Window):
	def __init__(self):
		super().__init__(title = "RAVE TIME!")

		builder = Gtk.Builder()
		builder.add_from_file("glade-button.glade")
		
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
		window.connect("destroy", Handlers.myDestroy)
		window.connect("destroy", Gtk.main_quit)

		myHandlers = Handlers(jigglypuff, stop_button, label1, window)
		builder.connect_signals(myHandlers)
		
		window.show_all()


#this code taken from here:
# ~ https://stackoverflow.com/questions/29979957/how-to-make-filename-path-from-gtk-python-3-4-filechooserdialog-accessible-gl
#I'll make my own later
class FileChooser():

	def __init__(self):
		#Stores your path
		self.path = None

		dia = Gtk.FileChooserDialog("Please choose a file", None,
			Gtk.FileChooserAction.OPEN,
			(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
			 Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

		self.add_filters(dia)

		response = dia.run()

		if response == Gtk.ResponseType.OK:
			print("Open clicked")
			print("File selected: " + dia.get_filename())
			self.path = dia.get_filename()
		elif response == Gtk.ResponseType.CANCEL:
			print("Cancel clicked")

		dia.destroy()

	def add_filters(self, dia):
		filter_any = Gtk.FileFilter()
		filter_any.set_name("Any files")
		filter_any.add_pattern("*")
		dia.add_filter(filter_any)

		filter_text = Gtk.FileFilter()
		filter_text.set_name('Text files')
		filter_text.add_mime_type('text/plain')
		dia.add_filter(filter_text)

		filter_py = Gtk.FileFilter()
		filter_py.set_name('Python files')
		filter_py.add_mime_type('text/x-python')
		dia.add_filter(filter_py)

		filter_img = Gtk.FileFilter()
		filter_img.set_name('Image')
		filter_img.add_mime_type('image/*')
		dia.add_filter(filter_img)
