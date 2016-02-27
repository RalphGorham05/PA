import speech_recognition as sr

class Ears:
	def __init__(self):
		self.r = sr.Recognizer()
		
	def listen_to(self):
		with sr.Microphone() as source:
			audio = self.r.listen(source)
	
	def voiceTest(self):
		try:
			print("Google Speech Recognition thinks you said " + self.r.recognize_google(audio))
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))
			
	def eardrum(self):
		self.listen_to()
		#self.voiceTest()
		
e = Ears()
e.eardrum()
		
