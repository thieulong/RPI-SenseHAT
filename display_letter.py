from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

while True:
    sense.show_letter("P", text_colour=(255, 0, 0), back_colour=(255, 255, 255))
    sleep(1)
    sense.show_letter("A", text_colour=(255, 0, 0), back_colour=(255, 255, 255))
    sleep(1)
    sense.show_letter("U", text_colour=(255, 0, 0), back_colour=(255, 255, 255))
    sleep(1)
    sense.show_letter("L", text_colour=(255, 0, 0), back_colour=(255, 255, 255))
    sleep(1)