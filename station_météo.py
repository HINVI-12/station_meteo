import dht
from utime import sleep_ms

from machine import I2C,Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from time import sleep

##configuration de l'écran lcd##
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

#######configuration du dht11#######
#vcc = 3.3 volts
dht_pin = Pin(2,Pin.IN,Pin.PULL_UP)
dht_sensor = dht.DHT11(dht_pin)

while True:
    try :
        
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        
        sleep(1)
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr("Station Meteo:")
        lcd.move_to(0,1)
        lcd.putstr("Maison HINVI")
        #lcd.clear()
        sleep(3)
        
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr(f"Temperature: {temperature :2d}C")
        lcd.move_to(0,1)
        lcd.putstr(f"Humidity: {humidity :2d}%")
        print(f"Température:{temperature} °C| Humidité:{humidity} %")
        sleep_ms(5000)

    except Exception as e:
        print(f"Veuillez verifier le circuit de votre capteur DHT11{str(e)}")
        sleep_ms(1000)


