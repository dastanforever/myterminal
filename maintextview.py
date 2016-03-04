

from gi.repository import Gtk, Pango



def create_textview(text):
    scrolledwindow = Gtk.ScrolledWindow()
    scrolledwindow.set_hexpand(True)
    scrolledwindow.set_vexpand(True)
    self.grid.attach(scrolledwindow, 0, 1, 3, 1)

    self.textview = Gtk.TextView()
    self.textview.set_wrap_mode(Gtk.WrapMode.WORD)
    self.textbuffer = self.textview.get_buffer()
    self.textbuffer.set_text(text)

    self.tag_bold = self.textbuffer.create_tag("bold",
        weight=Pango.Weight.BOLD)
    self.tag_italic = self.textbuffer.create_tag("italic",
        style=Pango.Style.ITALIC)
    self.tag_underline = self.textbuffer.create_tag("underline",
        underline=Pango.Underline.SINGLE)
    self.tag_found = self.textbuffer.create_tag("found",
        background="yellow")
    scrolledwindow.add(self.textview)
