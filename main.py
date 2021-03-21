import eel
from pyowm.owm import OWM

owm = OWM('dd37507ef449549a2e5579fc1e4f59c5')

@eel.expose
def get_weather(place):

    mgr = owm.weather_manager()
    weather = mgr.weather_at_place(place)
    w = weather.weather
    temp = w.temperature('celsius')['temp']
    return "В городе {} сейчас {} градусов!".format(place, str(temp))

eel.init('web')
eel.start("main.html", size=(600, 600))
