# -*-coding: utf-8 -*-
import time
import multiprocessing as mp
from rpi_ws281x import *
from Led import Led
from servo import Servo

def led_process():
     while True:
         print ("Chaser animation")
         led.colorWipe(led.strip, Color(255,0, 0))  # Red wipe
         led.colorWipe(led.strip, Color(0, 255, 0))  # Green wipe
         led.colorWipe(led.strip, Color(0, 0, 255))  # Blue wipe
         led.theaterChaseRainbow(led.strip)
         print ("Rainbow animation")
         led.rainbow(led.strip)
         led.rainbowCycle(led.strip)
         led.colorWipe(led.strip, Color(0,0,0),10)

def servo_process():
    _0_deg = 90
    _1_deg = 90
    _0_up = True
    _1_up = True
    while True:
        servo.setServoPwm('0',_0_deg)
        servo.setServoPwm('1',_1_deg)
        if _0_up:
            _0_deg = _0_deg + 1
            if _0_deg == 135: _0_up = False
        else:
            _0_deg = _0_deg - 1
            if _0_deg == 45: _0_up = True
        
        if _1_up:
            _1_deg = _1_deg + 2
            if _1_deg == 134: _1_up = False
        else:
            _1_deg = _1_deg - 2
            if _1_deg == 70: _1_up = True
        time.sleep(0.005)

# Main program logic follows:
if __name__ == '__main__':
    print ('Program is starting ... ')
    led=Led()
    servo=Servo()
    try:
        led_ = mp.Process(target=led_process, args=())
        servo_ = mp.Process(target=servo_process, args=())
        led_.start()
        servo_.start()
        led_.join()
        servo_.join()
        
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        led.colorWipe(led.strip, Color(0,0,0),10)

        
            
        
                    




   
