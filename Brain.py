from Mouth import Mouth
from Ears import Ears
import time
import json
import mechanize


class Brain:
    def __init__(self):
        self.mouth = Mouth()
        self.ears = Ears()
        self.current_weather = None
        self.current_temp = None
        self.forecast = {}

    def assess(self, data):
        if 'time' in data:
            self.tell_time()
        elif 'weather' in data:
            self.mouth.speak('what is your zip code')
            self.ears.listen_to()
            self.ears.get_message()
            zip_code = self.ears.message
            self.get_weather(zip_code)
            self.tell_weather()

        elif 'forecast'in data:
            self.mouth.speak('what is your zip code')
            self.ears.listen_to()
            self.ears.get_message()
            zip_code = self.ears.message
            self.get_forecast(zip_code)
            self.tell_forecast

        else:
            self.mouth.speak('I dont understand')
            self.mouth.speak('have a nice day')

    def tell_time(self):
        current_time = "Current time  is %s:%s %s" % (time.strftime("%I"), time.strftime("%M"), time.strftime("%p"))
        self.mouth.speak(current_time)

    def get_weather(self, location):
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
        current_weather = 'weather in %s %s is %s' % (city, state, weather.lower())
        current_temp = 'It is currently %s degrees and it feels like %s' % (temperature, real_feel)
        self.current_weather = current_weather
        self.current_temp = current_temp

    def get_forecast(self, location):
        forecast_url = 'http://api.wunderground.com/api/4e5650239b5d5af8/geolookup/forecast10day/q/' + location + '.json'
        browser = mechanize.Browser()
        w = browser.open(forecast_url)
        json_string = w.read()
        parsed_json = json.loads(json_string)
        for day in parsed_json['forecast']['simpleforecast']['forecastday']:
            self.forecast[day['date']['weekday'] + str(day['date']['day'])] = [str(day['conditions']), str(day['high']['fahrenheit'])]

    def tell_weather(self):
        # wunderground key 4e5650239b5d5af8
        # http://api.wunderground.com/api/4e5650239b5d5af8/conditions/q/10550.json
        if self.current_weather and self.current_temp:
            self.mouth.speak(self.current_weather)
            self.mouth.speak(self.current_temp)
        else:
            self.mouth.speak('Cant find weather')

    def tell_forecast(self):
        if self.forecast:
            for day, forecast in self.forecast.iteritems():
                self.mouth.speak('the forecast for %s is %s degrees' % (day, forecast))


br = Brain()
br.ears.listen_to()
br.ears.get_message()
br.assess(br.ears.message)





