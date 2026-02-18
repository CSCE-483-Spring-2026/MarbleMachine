import RPi.GPIO as GPIO
import time

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
    setAngle(60, pin)

def move_closed(pin):
    #90 might be closed position for 3d print setup
    setAngle(90, pin)

#testing
try:
    while True:
        move_open(SERVO_RED)
        time.sleep(2)
        move_closed(SERVO_RED)
        time.sleep(5)

except KeyboardInterrupt:
    print('key board interupt')

#i dont think this is working ?
for i in pwm:
    i.stop()
GPIO.cleanup()

