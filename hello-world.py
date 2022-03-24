#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  hello-world.py

# MIT License
# Copyright (c) <2021> <stephen.stengel@cwu.edu>

# This is a test program using glade and gtk through pygobject

#TODO: Figure out why it goes transparent every two color flashes.
#	I've found that this error only occurs when I use gnome-terminal to run hello-world.py


import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from MyWindow import MyWindow


def main(args):
	theWindow = MyWindow()
	Gtk.main()
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
	
