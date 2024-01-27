from machine import Pin, SPI
from config import utelegram_config
from config import wifi_config

import max7219
import utelegram
import network
import utime


debug = True

# Configuración de la matriz de LED
spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(18), mosi=Pin(23))
ss = Pin(5, Pin.OUT)
matrix = max7219.Matrix8x8(spi, ss, 5)

matrix.fill(0)
matrix.show()

# Configuración del pin del LED en el ESP32
p2 = Pin(2, Pin.OUT)


sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.scan()
sta_if.connect(wifi_config['ssid'], wifi_config['password'])

if debug: print('WAITING FOR NETWORK - sleep 20')
utime.sleep(20)

def get_message(message):
    bot.send(message['message']['chat']['id'], message['message']['text'].upper())

def reply_ping(message):
    print(message)
    bot.send(message['message']['chat']['id'], 'pong')

if sta_if.isconnected():
    bot = utelegram.ubot(utelegram_config['token'])
    bot.register('/ping', reply_ping)
    bot.set_default_handler(get_message)

    print('BOT LISTENING')
    p2.on()
    bot.listen()
    
    
else:
    p2.off()
    print('NOT CONNECTED - aborting')
    
    


