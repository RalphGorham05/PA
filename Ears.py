import speech_recognition as sr


class Ears:
    def __init__(self):
        self.r = sr.Recognizer()
        self.audio = None
        self.message = None

    def listen_to(self):
        with sr.Microphone() as source:
            print 'Start speaking'
            self.audio = self.r.listen(source)
            self.r.duration = 4

    def get_message(self):
        try:
            self.message = self.r.recognize_google(self.audio)
            print("you said %s " % self.message)
        except sr.UnknownValueError:
            print("could not understand audio")
        except sr.RequestError as ex:
            print("Could not request results from Google Speech Recognition service; {0}".format(ex))
        

    def eardrum(self):
        self.listen_to()