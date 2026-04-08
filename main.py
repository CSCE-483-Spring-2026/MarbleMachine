import RPi.GPIO as GPIO
import time
import json
import datetime
import threading
import yaml
import board
import adafruit_tcs34725

i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)

GPIO.setmode(GPIO.BCM)

#Pin Assignments (see wiring diagram):
SERVO_RED = 17
SERVO_YELLOW = 27
SERVO_GREEN = 22
SERVO_BLUE = 5
SERVO_SORT = 6


SERVOS = [SERVO_RED, SERVO_YELLOW, SERVO_GREEN, SERVO_BLUE, SERVO_SORT] #later add additional 'sorting' servos

# INITIALIZATION:

#servo init
# for pin in SERVOS:
#     GPIO.setup(pin, GPIO.OUT)

#software pmw
pwm = {}

for pin in SERVOS:
    GPIO.setup(pin, GPIO.OUT)
    #this makes a 'pwm instance'
    p_i = GPIO.PWM(pin, 50) # 50 hz frequency
    p_i.start(0)
    pwm[pin] = p_i


def setAngle(angle, pin):
    #angle to duty cycle
    duty = (angle / 18) + 2.5 #this equation converts angle to duty cycle for 50hz
    pwm[pin].ChangeDutyCycle(duty)
    time.sleep(0.5)
    pwm[pin].ChangeDutyCycle(0)

def move_open(pin):
    setAngle(125, pin)

def move_closed(pin):
    #90 might be closed position for 3d print setup
    setAngle(90, pin)

def moving_servos(pin, frequency, start_day, start_time):

    next_trigger = calculate_next_trigger(start_day, start_time)

    while True:
        now = datetime.datetime.now()
        delay = (next_trigger - now).total_seconds()

        if delay > 0:
            time.sleep(delay)
        
        #open
        move_open(pin)
        time.sleep(0.1)
        move_closed(pin)

        #reset delays:
        if frequency == "Daily" or "daily":
            next_trigger += datetime.timedelta(days=1)
        
        if frequency == "Weekly" or "weekly":
            next_trigger += datetime.timedelta(days=7)


DaysOfWeek = {
    "Monday" : 0,
    "Tuesday" : 1,
    "Wednesday" : 2,
    "Thursday" : 3,
    "Friday" : 4,
    "Saturday" : 5,
    "Sunday" : 6
}

def calculate_next_trigger(start_day, start_time):

    now = datetime.datetime.now() #gets current time
    weekday_number = DaysOfWeek[start_day] 

    #given time = 12:26, hour = 12, min=26
    hour,minute = map(int, start_time.split(":"))
 
    remaing_days = weekday_number - now.weekday()
    if remaing_days < 0:
        remaing_days += 7

    next_trigger = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    next_trigger += datetime.timedelta(days=remaing_days)
    if next_trigger <=now:
        next_trigger += datetime.timedelta(days=7)

    return next_trigger

def color_sensor():
    while True:
        #there are also temperature and lux readings if we end up needing them
        color_rgb = sensor.color_rgb_bytes
        print(f"RGB: {color_rgb}")

        #MY LINE TESTING
        if color_rgb[0] >= 70 and color_rgb[1] <= 5 and color_rgb[2] <=5 :
            print("RED!")
            setAngle(180, SERVO_SORT) #NEED TO DETERMINE NUMBERS FOR EACH COLOR
            time.sleep(2)

        elif color_rgb[0] >= 40 and color_rgb[1] == 0 and color_rgb[2] == 0:
            print("RED!")
            setAngle(180, SERVO_SORT)
            time.sleep(2)
        
        elif color_rgb[0] >= 100 and color_rgb[1] <= 10 and color_rgb[2] <= 10:
            print("RED!")
            setAngle(180, SERVO_SORT)
            time.sleep(2)

        elif color_rgb[0] == 45 and color_rgb[1] == 45 and color_rgb[2] <= 20:
            print("GREEN!")
            setAngle(42, SERVO_SORT)
            time.sleep(2)

        elif color_rgb[0] == color_rgb[1] and color_rgb[2] <= 7:
            print("GREEN!")
            setAngle(42, SERVO_SORT)
            time.sleep(2)
        
        elif color_rgb[0] > 10 and color_rgb[0] <20 and color_rgb[2] <= color_rgb[1] - 5:
            print("GREEN!")
            setAngle(42, SERVO_SORT)
            time.sleep(2)
        
        elif color_rgb[0] != 0 and color_rgb[0] == color_rgb[1] and color_rgb[0] >=25:
            print("BLUE!")
            setAngle(0, SERVO_SORT)
            time.sleep(2)
        
        elif color_rgb[0] != 0 and color_rgb[1] != 0:
            print("YELLOW!")
            setAngle(138, SERVO_SORT)
            time.sleep(2)
        else:
            print("idk...???")


        time.sleep(1.0)



def readYaml(filename):
    with open(filename, 'r') as file:
        return yaml.safe_load(file)
    #should return with format {marbleColor: {'Start': startTime, 'Period': PeriodSet}}


yaml_data = readYaml('kamrynsFake.json')

#format like this maybe?
#!!! note capitaliation
#{"redFreq":"Daily", "redStartDay":"Monday", "redStartTime":"12:26","yellowFreq":"Weekly" ...,"greenFreq":"Weekly" ...,"blueFreq":"Daily" ...}

# should be daily or weekly
red_delay = (yaml_data['redFreq'])
yellow_delay = (yaml_data['yellowFreq'])
green_delay = (yaml_data['greenFreq'])
blue_delay = (yaml_data['blueFreq'])


# should be input as days of the week
red_start_day = (yaml_data['redStartDay'])
yellow_start_day = (yaml_data['yellowStartDay'])
green_start_day = (yaml_data['greenStartDay'])
blue_start_day = (yaml_data['blueStartDay'])

red_start_time = (yaml_data['redStartTime'])
yellow_start_time = (yaml_data['yellowStartTime'])
green_start_time = (yaml_data['greenStartTime'])
blue_start_time = (yaml_data['blueStartTime'])

servo_delays = [red_delay, yellow_delay, green_delay, blue_delay]
start_days = [red_start_day, yellow_start_day, green_start_day, blue_start_day]
start_times = [red_start_time, yellow_start_time, green_start_time, blue_start_time]

threads = []

for i in range(4):
    thread_i = threading.Thread(target=moving_servos, args=(SERVOS[i], servo_delays[i], start_days[i], start_times[i])) #add start time to args
    thread_i.daemon = True #this is important apparently, kills threads because they'll never end
    threads.append(thread_i)

threads_color = threading.Thread(target=color_sensor)
threads_color.daemon = True
threads_color.start()

for i in range(4):
    threads[i].start()



#testing
try:
    while True:
        time.sleep(1) 
 

except KeyboardInterrupt:
    print('key board interupt')
    for i in pwm.values(): 
        i.stop()
    GPIO.cleanup()

#i dont think this is working ?
# for i in pwm.values(): 
#     i.stop()
# GPIO.cleanup()

#data = readFile('marbles')
#print(data)
