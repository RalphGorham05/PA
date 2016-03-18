import pyttsx


class Mouth:
    def __init__(self):
        self.tongue = pyttsx.init('sapi5')
        # self.tongue = pyttsx.init('espeak') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
        self.tongue.setProperty('rate', 150)

    def speak(self, text):
        self.tongue.say(text)
        self.tongue.runAndWait()






