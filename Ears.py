import speech_recognition as sr


class Ears:
    def __init__(self):
        self.r = sr.Recognizer()
        self.audio = None
        self.message = None

    def listen_to(self):
        with sr.Microphone() as source:
            print 'listening'
            self.audio = self.r.listen(source)
            self.r.duration = 5

    def get_message(self):
        if self.audio:
            self.message = self.r.recognize_google(self.audio)
        else:
            self.message = 'didnt hear'

    def voice_test(self):
        try:
            print("Google Speech Recognition thinks you said " + self.r.recognize_google(self.audio))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as ex:
            print("Could not request results from Google Speech Recognition service; {0}".format(ex))

    def eardrum(self):
        self.listen_to()
        self.voice_test()


