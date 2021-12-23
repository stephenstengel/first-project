import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from os import system
from os import kill

import subprocess
import signal

# ~ window = Gtk.Window(title="Hello World!")
# ~ window.connect("destroy", Gtk.main_quit)
# ~ window.show()
# ~ Gtk.main()


##Bug: When start button is pressed multiple times, the pid gets updated
##so the stop button will have the wrong id to kill
##The music continues to run under the first pid.

class Handler:
	myProcess = None
	
	def button1_clicked(self, button):
		print("Start music button pressed!")
		if self.myProcess is None:
			self.myProcess = subprocess.Popen(["ogg123", "james-brown-dead.ogg", "-r"])
			print("Process ID: " + str(self.myProcess.pid))
		
	def music_stop_clicked_cb(self, button):
		print("Stop button pressed!")
		print("Killing this process: " + str(self.myProcess.pid))
		kill(self.myProcess.pid, signal.SIGKILL)
		self.myProcess = None

builder = Gtk.Builder()
builder.add_from_file("glade-button.glade")
builder.connect_signals(Handler())

start_button = builder.get_object("music_start")
start_button.set_label("Play the music!")

stop_button = builder.get_object("music_stop")
stop_button.set_label("Stop the music!")

window = builder.get_object("myWindow")

window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
