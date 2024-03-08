import RPi.GPIO as GPIO
import time

SDI = 11
RCLK = 12
SRCLK = 13
SDI2 = 26
RCLK2 = 15
SRCLK2 = 16

segCode = [0x7f,0x79,0x24]
segCode2 = [0x40,0x79,0x24,0x30,0x19,0x12,0x02,0x78,0x00,0x10]
segCode3 = [0x7f,0x08,0x03,0x27,0x21,0x06,0x0e,0x10,0x0b,0x6f,0x71,0x0f,0x67,0x36,0x2b,0x23,0x0c,0x18,0x2f,0x12,0x07,0x63,0x1d,0x49,0x2d,0x0d,0x3c]
segCode4 = [0x79,0x24,0x30,0x19,0x12,0x02,0x78,0x00,0x10]
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
    GPIO.setup(SDI2, GPIO.OUT)
    GPIO.setup(RCLK2, GPIO.OUT)
    GPIO.setup(SRCLK2, GPIO.OUT)
    GPIO.output(SDI2, GPIO.HIGH)
    GPIO.output(RCLK2, GPIO.HIGH)
    GPIO.output(SRCLK2, GPIO.HIGH)
    

def hc595_shift(dat):
    for bit in range(0,8):
        GPIO.output(SDI, 0x80 & (dat << bit))
        GPIO.output(SRCLK, GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(SRCLK, GPIO.HIGH)
    GPIO.output(RCLK, GPIO.LOW)
    time.sleep(0.001)
    GPIO.output(RCLK, GPIO.HIGH)

def hc595_shift2(dat):
    for bit in range(0,8):
        GPIO.output(SDI2, 0x80 & (dat << bit))
        GPIO.output(SRCLK2, GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(SRCLK2, GPIO.HIGH)
    GPIO.output(RCLK2, GPIO.LOW)
    time.sleep(0.001)
    GPIO.output(RCLK2, GPIO.HIGH)

def loop():
    
    while True:
        for q in range(0,1):
            for s in range(0,1):
                hc595_shift(segCode3[q])
                hc595_shift2(segCode3[s])
                time.sleep(1)
        d = 2
        for i in range(0, 3):
            d += 1
            if d == 5:
                for j in range(0,6):
                    hc595_shift(segCode[i])
                    hc595_shift2(segCode2[j])
                    time.sleep(1)
            elif d == 3:
                for t in range(0,len(segCode4)):
                    hc595_shift(segCode[i])
                    hc595_shift2(segCode4[t])
                    time.sleep(1)
                
            else:
                for k in range(0,len(segCode2)):
                    hc595_shift(segCode[i])
                    hc595_shift2(segCode2[k])
                    time.sleep(1)
        for q in range(0,1):
            for s in range(0,len(segCode3)):
                hc595_shift(segCode3[q])
                hc595_shift2(segCode3[s])
                time.sleep(1)

def destroy():
    GPIO.cleanup()

print_msg()
setup()
try:
    loop()
except KeyboardInterrupt:
    destroy()
