from machine import Pin, PWM, I2C
import time 
from pico_i2c_lcd import I2cLcd
open_button = Pin(1, Pin.IN, Pin.PULL_UP)
gas_sensor_out = Pin(0, Pin.IN)
red_led = Pin(20, Pin.OUT)
buzzer = Pin(11, Pin.OUT)
servo = PWM(Pin(15))
servo.freq(50) 
i2c = I2C(1, sda=Pin(18), scl=Pin(19), freq=400000)
my_lcd = I2cLcd(i2c, 0x27, 2, 16)

def set_angle(angle):
    duty = int(1638 + (angle / 180) * (8192 - 1638))
    servo.duty_u16(duty)

def reset ():
  set_angle(0)
  buzzer.value(0)
  red_led.value(0)
  my_lcd.clear()

reset()

while True:
    if gas_sensor_out.value() == 1:
        buzzer.value(1)
        red_led.value(1)
        my_lcd.clear()
        my_lcd.putstr("Gas Leakage!")
        if open_button.value() == 0:
            set_angle(90)
            time.sleep(0.5)
            set_angle(-90)
            reset()
        time.sleep(0.5)
    else:
        buzzer.value(0)
        red_led.value(0)
        set_angle(0)
        my_lcd.clear()
        my_lcd.putstr("No Gas Leakage")
        time.sleep(1)

