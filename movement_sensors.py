from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

while True:

    o = sense.get_orientation()

    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]

    print("Pitch: {0} Roll: {1} Yaw: {2}".format(pitch, roll, yaw))