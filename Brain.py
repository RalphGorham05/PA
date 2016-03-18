from Mouth import Mouth
import time

class Brain:
	def __init__(self):
		self.mouth = Mouth()

	def assess(self, input):
		if input == 'what time is it':
			self.tell_time()
		elif input == 'what is the weather':
			self.tell_weather()
		else:
			self.mouth.speak('I dont understand')

	def tell_time(self):
		current_time = "Current time  is %s:%s %s" % (time.strftime("%I"), time.strftime("%M"), time.strftime("%p"))
		self.mouth.speak(current_time)

	def tell_weather(self):
		self.mouth.speak('i dont know weather yet')


said = 'what is the weather'
br = Brain()
br.assess(said)
