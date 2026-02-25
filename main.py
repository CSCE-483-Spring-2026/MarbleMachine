import RPi.GPIO as GPIO
import time
import yaml
import datetime
import threading

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

def moving_servos(pin, delay):
    while True:
        move_open(pin)
        time.sleep(0.5) #need to test this value
        move_closed(pin)
        time.sleep(delay - 0.5*3) 

def readYaml(filename):
    with open(filename, 'r') as file:
        return yaml.safe_load(file)
    #should return with format {marbleColor: {'Start': startTime, 'Period': PeriodSet}}

def interpretYaml(str):
    li = [[]]
    byMarble = str.split('}}')
    for i in byMarble:
        broken = i.split()
        li.append(broken)
    return li
    #would have format [['{marbleColor:', '{'Start':', 'startTime,', ''Period':', 'PeriodSet'][...][...][...]]

#this is temporary, we can change to user input/ reading from the json eventually or whatever
servo_delays = [2, 5, 10, 4]

threads = []

for i in range(4):
    thread_i = threading.Thread(target=moving_servos, args=(SERVOS[i], servo_delays[i]))
    thread_i.daemon = True #this is important apparently, kills threads because they'll never end
    threads.append(thread_i)

for i in range(4):
    threads[i].start()



#testing
try:
    while True:
        time.sleep(1) 

    # move_open(SERVO_RED)
    # move_open(SERVO_YELLOW)
    # move_open(SERVO_GREEN)
    # move_open(SERVO_BLUE)
    # time.sleep(2)
    # move_closed(SERVO_RED)
    # time.sleep(2)

    # #move_open(SERVO_YELLOW)
    # time.sleep(2)
    # move_closed(SERVO_YELLOW)
    # time.sleep(2)

    # #move_open(SERVO_GREEN)
    # time.sleep(2)
    # move_closed(SERVO_GREEN)
    # time.sleep(2)

    # #move_open(SERVO_BLUE)
    # time.sleep(2)
    # move_closed(SERVO_BLUE)
    # time.sleep(2)

        


except KeyboardInterrupt:
    print('key board interupt')
    for i in pwm.values(): 
        i.stop()
    GPIO.cleanup()

#i dont think this is working ?
for i in pwm.values(): 
    i.stop()
GPIO.cleanup()
