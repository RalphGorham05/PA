from phue import Bridge

b = Bridge('192.168.0.5')
# b.get_api()

b.set_light('Bedroom','on', False)
