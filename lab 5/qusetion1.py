import RPi.GPIO as GPIO
import time

SDI = 11
RCLK = 12
SRCLK = 13

segCode = [0x40,0x79,0x24,0x30,0x19,0x12,0x02,0x78,0x00,0x10,0x08,0x03,0x27,0x21,0x06,0x0e,0x10,0x7f]

def print_msg():
    print ("Program is running...")
    print("please press ctrl + c to end the program...")

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SDI, GPIO.OUT)
    GPIO.setup(RCLK, GPIO.OUT)
    GPIO.setup(SRCLK, GPIO.OUT)
    GPIO.output(SDI, GPIO.HIGH)
    GPIO.output(RCLK, GPIO.HIGH)
    GPIO.output(SRCLK, GPIO.HIGH)

def hc595_shift(dat):
    for bit in range(0,8):
        GPIO.output(SDI, 0x80 & (dat << bit))
        GPIO.output(SRCLK, GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(SRCLK, GPIO.HIGH)
    GPIO.output(RCLK, GPIO.LOW)
    time.sleep(0.001)
    GPIO.output(RCLK, GPIO.HIGH)

def loop():
    while True:
        for i in range(0, len(segCode)):
            hc595_shift(segCode[i])
            time.sleep(1)

def destroy():
    GPIO.cleanup()

print_msg()
setup()
try:
    loop()
except KeyboardInterrupt:
    destroy()
