#! /usr/bin/python
# -*- coding: utf-8 -*-

from gi.repository import Gtk, Pango
import lib, buffer

class MainWindow(Gtk.Window):
    """docstring for Main Terminal Window"""
    def __init__(self):
        self.username = lib.getusername()
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
        self.set_text(self.username + " $ ")
        scrolledwindow.add(self.textview)
        return self.textview

    def set_text(self, text=None):
        if text is None:
            text = "\n" + self.username + " $ "
        self.buffer.insert_cmdline(text)

termwindow = MainWindow()

def keyPress(widget, event):
    if event.keyval == 65293:
        termwindow.set_text()
        return True
    return False


def main():
    termwindow.connect("delete-event", Gtk.main_quit)
    termwindow.tv.connect('key-press-event', keyPress)
    termwindow.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
