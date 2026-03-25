import RPi.GPIO as GPIO
import time
import json
import datetime
import threading
import yaml

GPIO.setmode(GPIO.BCM)

#Pin Assignments (see wiring diagram):
SERVO_RED = 17
SERVO_YELLOW = 27
SERVO_GREEN = 22
SERVO_BLUE = 5


SERVOS = [SERVO_RED, SERVO_YELLOW, SERVO_GREEN, SERVO_BLUE] #later add additional 'sorting' servos

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
    weekday_number = DaysOfWeek[day] 

    #given time = 12:26, hour = 12, min=26
    hour,minute = map(int, time.split(":"))

    remaing_days = weekday_number - now.weekday()
    if remaing_days < 0:
        remaing_days += 7

    next_trigger = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    next_trigger += datetime.timedelta(days=remaing_days)
    if next_trigger <=now:
        next_trigger += datetime.timedelta(days=7)

    return next_trigger


def readYaml(filename):
    with open(filename, 'r') as file:
        return yaml.safe_load(file)
    #should return with format {marbleColor: {'Start': startTime, 'Period': PeriodSet}}


yaml_data = readYaml('test.json')

#format like this maybe?
#!!! note capitaliation
#{"redFreq":"Daily", "redStartDay":"Monday", "redStartTime":"12:26","yellowFreq":"Weekly" ...,"greenFreq":"Weekly" ...,"blueFreq":"Daily" ...}

# should be daily or weekly
red_delay = int(yaml_data['redFreq'])
yellow_delay = int(yaml_data['yellowFreq'])
green_delay = int(yaml_data['greenFreq'])
blue_delay = int(yaml_data['blueFreq'])


# should be input as days of the week
red_start_day = int(yaml_data['redStartDay'])
yellow_start_day = int(yaml_data['yellowStartDay'])
green_start_day = int(yaml_data['greenStartDay'])
blue_start_day = int(yaml_data['blueStartDay'])

red_start_time = int(yaml_data['redStartTime'])
yellow_start_time = int(yaml_data['yellowStartTime'])
green_start_time = int(yaml_data['greenStartTime'])
blue_start_time = int(yaml_data['blueStartTime'])

servo_delays = [red_delay, yellow_delay, green_delay, blue_delay]
start_days = [red_start_day, yellow_start_day, green_start_day, blue_start_day]
start_times = [red_start_time, yellow_start_time, green_start_time, blue_start_time]

threads = []

for i in range(4):
    thread_i = threading.Thread(target=moving_servos, args=(SERVOS[i], servo_delays[i], start_days[i], start_times[i])) #add start time to args
    thread_i.daemon = True #this is important apparently, kills threads because they'll never end
    threads.append(thread_i)

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
