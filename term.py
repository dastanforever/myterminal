#! /usr/bin/python
# -*- coding: utf-8 -*-

from gi.repository import Gtk, Pango
import lib, buffer
import readcommand as readin

class MainWindow(Gtk.Window):
    """docstring for Main Terminal Window"""
    def __init__(self):
        self.username = lib.getusername()
        self.start_read_index = 0
        Gtk.Window.__init__(self, title=self.username)
        Gtk.Window.set_default_size(self, 700, 500)
        Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)

        self.grid = Gtk.Grid()
        self.add(self.grid)
        self.buffer = buffer.textbuffer()
        self.tv = self.create_textview(buffer = self.buffer)

    def create_textview(self, buffer):
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        self.grid.attach(scrolledwindow, 0, 1, 3, 1)

        self.textview = Gtk.TextView(buffer = buffer)
        self.textview.set_wrap_mode(Gtk.WrapMode.WORD)
        self.textbuffer = self.textview.get_buffer()
        self.reset_start()
        self.set_text(self.username + " $ " + str(self.get_start_pos()))
        scrolledwindow.add(self.textview)
        return self.textview

    def set_text(self, text=None):
        if text is None:
            text = "\n" + self.username + " $ "
        self.buffer.insert_cmdline(text)

    def reset_start(self):
        self.start_read_index = self.buffer.get_curr_pos()

    def get_start_pos(self):
        return self.start_read_index

    def get_c_pos(self):
        return self.buffer.get_curr_pos()

    def read(self):
        reader = readin.Reader()
        return reader.read(self.get_start_pos(), self.get_c_pos(), self.textbuffer)


# Maqin Window.
termwindow = MainWindow()

def keyPress(widget, event):
    if event.keyval == 65293:
        # Read the command.
        # insert the main type of text into the buffer.
        command = termwindow.read()
        # Set the input main text again.
        termwindow.set_text(command)
        termwindow.reset_start()
        return True
    return False


def main():
    termwindow.connect("delete-event", Gtk.main_quit)
    termwindow.tv.connect('key-press-event', keyPress)
    termwindow.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
