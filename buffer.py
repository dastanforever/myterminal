



from gi.repository import Gtk, Pango

class textbuffer(Gtk.TextBuffer):
    """Main text buffer for the terminal."""

    def __init__(self):
        Gtk.TextBuffer.__init__(self)

        self.tags_on = {}
        self.begin_position = self.get_iter_at_mark(self.get_insert())

        self.tag_bold = self.create_tag("bold",
            weight=Pango.Weight.BOLD)
        self.tag_italic = self.create_tag("italic",
            style=Pango.Style.ITALIC)
        self.tag_underline = self.create_tag("underline",
            underline=Pango.Underline.SINGLE)
        self.tag_found = self.create_tag("found",
            background="yellow")
        self.tag_cmdline = self.create_tag("main_cmdline",
            editable=False)

    def get_iter_position(self):
        return self.get_iter_at_mark(self.get_insert())

    def insert_cmdline(self, text):
        length = len(text)
        self.insert(self.get_end_iter(), text)
        iter = self.get_iter_position()
        iter.backward_chars(length)
        # And this applies tag from iter to end of buffer
        self.apply_tag_by_name('main_cmdline', self.get_iter_position(), iter)
