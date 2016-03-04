#! /usr/bin/python
# -*- coding: utf-8 -*-

from gi.repository import Gtk, Pango
import lib

class MainWindow(Gtk.Window):
    """docstring for Main Terminal Window"""
    def __init__(self):
        self.username = lib.getusername()
        Gtk.Window.__init__(self, title=self.username)
        Gtk.Window.set_default_size(self, 700, 500)
        Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)

        self.grid = Gtk.Grid()
        self.add(self.grid)
        self.tv = self.create_textview()

    def create_textview(self):
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        self.grid.attach(scrolledwindow, 0, 1, 3, 1)

        self.textview = Gtk.TextView()
        self.textview.set_wrap_mode(Gtk.WrapMode.WORD)
        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.set_text(self.username + " $ ")
        scrolledwindow.add(self.textview)

        self.tag_bold = self.textbuffer.create_tag("bold",
            weight=Pango.Weight.BOLD)
        self.tag_italic = self.textbuffer.create_tag("italic",
            style=Pango.Style.ITALIC)
        self.tag_underline = self.textbuffer.create_tag("underline",
            underline=Pango.Underline.SINGLE)
        self.tag_found = self.textbuffer.create_tag("found",
            background="yellow")
        return self.textview

    def set_text(self, text="\n" + self.username + " $ "):
        self.textbuffer = self.tv.get_buffer()
        end_iter = self.textbuffer.get_end_iter()
        self.textbuffer.insert(end_iter, text)

termwindow = MainWindow()

def keyPress(widget, event):
    if event.keyval == 65293:
        termwindow.set_text()
        return True
    if event.keyval == :

    return False


def main():
    termwindow.connect("delete-event", Gtk.main_quit)
    termwindow.tv.connect('key-press-event', keyPress)
    termwindow.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
