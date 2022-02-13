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

from MyWindow import MyWindow



def main(args):
	theWindow = MyWindow()
	Gtk.main()
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
	
