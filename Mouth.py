import pyttsx


class Mouth:
    def __init__(self):
        # self.tongue = pyttsx.init('sapi5')
        self.tongue = pyttsx.init('espeak') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
        self.tongue.setProperty('rate', 150)
        self.voices = self.tongue.getProperty('voices')

    def close_mouth(self):
   		self.tongue.runAndWait()

    def speak(self, text):
        self.tongue.say(text)
        self.close_mouth()
     
   	
'''
m = Mouth()
m.speak('test')
print ''
j = 'joe'
m.speak('another one')
m.speak(j)
m.another()
m.close_mouth()
'''





