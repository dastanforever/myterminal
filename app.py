

import kivy
import os
from command import Commands
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

CH = Commands()

def getdir():
    return os.getcwd()

introlabel = Label(text = getdir(), size_hint=(1, 0.1))
textInput = TextInput(multiline=False,size_hint=(1,0.1))
resultLabel = Label(text = "Output", size_hint=(1,1))

def makefocus():
    textInput = TextInput(focus = True)

def on_enter(*kw):
    # Get results.
    out = CH.run_command(textInput.text)
    # Put result into the below label.
    resultLabel.text = out
    # Clear the TextView.
    textInput.text = ""
    introlabel.text = getdir()
    makefocus()

def on_focus(instance, value):
    if not value:
        textInput.focus = True


class MainInterface(BoxLayout):
    """docstring for MainInterface"""

    def __init__(self, **kw):
        super(MainInterface, self).__init__(**kw)

        self.orientation = 'vertical'

        #btn1 = Button(text='Hello', size_hint=(1,0.5))
        #btn2 = Button(text='World')
        #self.add_widget(btn1)
        #self.add_widget(btn2)


        self.add_widget(introlabel)
        textInput.focus = True
        textInput.bind(on_text_validate=on_enter)
        textInput.bind(focus = on_focus)
        self.add_widget(textInput)
        self.add_widget(resultLabel)
        #
        #self.cols = 1
        #self.CommandPromt =  TextInput(multiline = False)
        #self.add_widget(self.CommandPromt)



class RootTerminal(App):

    def build(self):
        return MainInterface()





if __name__ == '__main__':
    RootTerminal().run()
