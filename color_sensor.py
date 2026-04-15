#IMPORTANT!!! HOW TO RUN:
# source venv/bin/activate
# pip install adafruit-circuitpython-tcs34725
# python3 color_sensor.py

#based on example code from https://learn.adafruit.com/adafruit-color-sensors/python-circuitpython


import time
import sys
import board
import adafruit_tcs34725

i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)


while True:
    #there are also temperature and lux readings if we end up needing them
    color_rgb = sensor.color_rgb_bytes
    print(f"RGB: {color_rgb}", file=sys.stderr)

    #MY LINE TESTING
    if color_rgb[0] >= 70 and color_rgb[1] <= 5 and color_rgb[2] <=5 :
        print("RED!")

    elif color_rgb[0] >= 40 and color_rgb[1] == 0 and color_rgb[2] == 0:
        print("RED!")
    
    elif color_rgb[0] >= 100 and color_rgb[1] <= 10 and color_rgb[2] <= 10:
        print("RED!")

    elif color_rgb[0] == 45 and color_rgb[1] == 45 and color_rgb[2] <= 20:
        print("GREEN!")

    elif color_rgb[0] == color_rgb[1] and color_rgb[2] <= color_rgb[1] - 5:
        print("GREEN!")
    
    elif color_rgb[0] != 0 and color_rgb[0] == color_rgb[1] and color_rgb[0] == color_rgb[2]:
        print("BLUE!")
    
    elif color_rgb[0] != 0 and color_rgb[1] != 0:
        print("YELLOW!")
    else:
        print("idk...???")


    time.sleep(1.0)
