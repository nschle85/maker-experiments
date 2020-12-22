from machine import Pin, I2C
import dht
import time
import ssd1306

led = Pin(2, Pin.OUT)
d = dht.DHT22(Pin(4))
i2c = I2C(-1, scl=Pin(22), sda=Pin(21))
scan = i2c.scan()
print(scan)
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)
    try:
        d.measure()
        temp = d.temperature()
        hum = d.humidity()
        stemp = ('Temp: %3.1f C' %temp)
        shumidy = ('Humidity: %3.1f %%' %hum)
        oled.fill(0)
        oled.text(stemp, 0, 0)
        oled.text(shumidy, 0, 10)
        oled.show()
    except OSError as e:
        print('Failed to read sensor.')
