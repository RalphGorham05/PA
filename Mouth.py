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

    def test(self):
        a = 5
        b = 3
        t = a -b
        self.t = t

    def another(self):
        print 'give me'
        f = 5/4
        y = 5 +9
        self.u = f + y
     
   	
'''
m = Mouth()
m.speak('test')
print ''
j = 'joe'
m.speak('another one')
m.speak(j)
m.test()
m.another()
m.speak(m.t)
m.speak(m.u)
m.close_mouth()
'''




