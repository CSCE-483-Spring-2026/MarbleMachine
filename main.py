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
    pwm_i = GPIO.PWM(pin, 50)
    pwm_i.start(0)
    pwm[pin] = pwm_i


def setAngle(angle, pin):
    # frequency = 50 # 50 Hz for standard servos
    # high_time = (angle / 180) * .002 + .0005
    # GPIO.output(pin, GPIO.HIGH)
    # time.sleep(high_time)
    # GPIO.output(pin, GPIO.LOW)
    # time.sleep(1/frequency - high_time)

    duty = 2.5 + (angle / 180.0) * 10
    pwm[pin].ChangeDutyCycle(duty)
    time.sleep(0.5)
    pwm[pin].ChangeDutyCycle(0)


def move_open(pin):
    setAngle(0, pin)

def move_closed(pin):
    setAngle(180, pin)

#testing
try:
    while True:
        move_open(SERVO_RED)
        time.sleep(2)
        move_closed(SERVO_RED)
        time.sleep(2)

except KeyboardInterrupt:
    print('key board interupt')

finally:
    for i in pwm:
        i.stop()
    GPIO.cleanup()

