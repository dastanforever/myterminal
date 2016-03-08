


class Reader:
    """docstring for Reader"""
    def __init__(self):
        self.commands = []

    def read(self, start, end, buffer):
        command = buffer.get_text(start, end, include_hidden_chars = True)
        self.commands.append(command)
        return command
