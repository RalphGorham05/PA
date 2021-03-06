from Mouth import Mouth
from Ears import Ears
import time
import json
import mechanize
import webbrowser
import vtest
from vtest import Auto_NAT
from bs4 import BeautifulSoup

from phue import Bridge


class Brain:
    def __init__(self):
        self.mouth = Mouth()
        self.ears = Ears()
        self.va = Auto_NAT()
        self.current_weather = None
        self.current_temp = None
        self.forecast = {}

    def assess(self, data):
        if 'Emma' in data:
            self.mouth.speak('Hello Lovely')
            self.ears.listen_to()
            self.ears.get_message()
            self.assess(self.ears.message)

        if 'time' in data:
            self.tell_time()
        elif 'weather' in data:
           self.mouth.speak('what is your zip code')
           self.ears.listen_to()
           self.ears.get_message()
           zip_code = self.ears.message
           self.get_weather(zip_code)
           self.mouth.speak(self.current_weather)
           self.mouth.speak(self.current_temp)
           self.mouth.close_mouth()

        elif 'forecast'in data:
            self.mouth.speak('what is your zip code')
            self.ears.listen_to()
            self.ears.get_message()
            zip_code = self.ears.message
            self.get_forecast(zip_code)

        elif 'open' in data:
            self.open_page()

        elif 'light' in data:
            self.lights()

        elif 'assistant' in data:
            self.va()

        else:
            self.mouth.speak('I dont understand')
            self.mouth.speak('have a nice day')
            self.mouth.close_mouth()


    def tell_time(self):
        current_time = "Current time  is %s:%s %s" % (time.strftime("%I"), time.strftime("%M"), time.strftime("%p"))
        self.mouth.speak(current_time)
        self.mouth.close_mouth()

    def get_weather(self, location):
        # wunderground key 4e5650239b5d5af8
        # http://api.wunderground.com/api/4e5650239b5d5af8/conditions/q/10550.json
        try:
           weather_url = 'http://api.wunderground.com/api/4e5650239b5d5af8/geolookup/conditions/q/PA/' + location + '.json'
           browser = mechanize.Browser()
           w = browser.open(weather_url)
           json_string = w.read()
           parsed_json = json.loads(json_string)
           city = parsed_json['location']['city']
           state = parsed_json['location']['state']
           weather = parsed_json['current_observation']['weather']
           temperature = parsed_json['current_observation']['temp_f']
           real_feel = parsed_json['current_observation']['feelslike_f']
           self.current_weather = 'weather in %s %s is %s' % (city, state, weather.lower())
           self.current_temp = 'It is currently %s degrees and it feels like %s' % (temperature, real_feel)

        except KeyError, ke:
           self.mouth.speak('Cant find weather for that %s' % ke)

    def get_forecast(self, location):
        forecast_url = 'http://api.wunderground.com/api/4e5650239b5d5af8/geolookup/forecast10day/q/' + location + '.json'
        browser = mechanize.Browser()
        w = browser.open(forecast_url)
        json_string = w.read()
        parsed_json = json.loads(json_string)
        for day in parsed_json['forecast']['simpleforecast']['forecastday']:
            self.forecast[day['date']['weekday'] + str(day['date']['day'])] = [str(day['conditions']), str(day['high']['fahrenheit'])]
        for day, forecast in self.forecast.iteritems():
            self.mouth.speak('the forecast for %s is %s degrees' % (day, forecast))


    def open_page(self):
        webbrowser.open('www.ign.com')

    def lights(self):
        b = Bridge('192.168.0.5')
        b.set_light('Bedroom','on', True)
        b.set_light('Bedroom', 'bri', 127)

    def get_showtime(self):
        movie_url = 'http://www.google.com/movies?hl=en&near=10550&dq=movie+times+10550&sa=X&oi=showtimes&ct=title&cd=1'
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        m = browser.open(movie_url)
        soup = BeautifulSoup(m)
        # s = soup.find_all(class = 'theater')
        # print s

    def va(self):
        va = self.va
        va.run()
        




br = Brain()
br.ears.eardrum()
br.assess(br.ears.message)
#br.get_showtime()
