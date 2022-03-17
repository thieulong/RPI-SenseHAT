from sense_hat import SenseHat

red = (255,0,0)
green = (0,255,0)

sense = SenseHat()
sense.clear()

pressure = round(sense.get_pressure(),1)
temp = round(sense.get_temperature(),1)
humidity = round(sense.get_humidity(),1)

# print("Pressure: {}".format(pressure))
# print("Temparature: {}".format(temp))
# print("Humidity: {}".format(humidity))

if temp > 37: text = red
elif temp <= 37: text = green

message = "Pressure : {p}, Temparature: {t}, Humidity: {h}".format(p=pressure, t=temp, h=humidity)
sense.show_message(message, scroll_speed=0.1, text_colour=text)