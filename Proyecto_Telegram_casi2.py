from machine import Pin, SPI
import max7219
import urequests
from time import sleep

# Configuración de la matriz de LED
spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(18), mosi=Pin(23))
ss = Pin(5, Pin.OUT)
matrix = max7219.Matrix8x8(spi, ss, 5)

# Configuración del bot de Telegram
BOT_TOKEN = '6988544341:AAHDYI9rvIh24QovC1AGQ4u094GmQJkJzSQ'
CHAT_ID = '1678153643'

def obtener_mensaje_de_telegram():
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates'
    response = urequests.get(url)
    data = response.json()
    if 'result' in data and data['result']:
        mensaje = data['result'][0]['message']['text']
        return mensaje
    return None

def mostrar_en_matriz(texto):
    matrix.brightness(5)
    matrix.fill(0)
    matrix.show()
    sleep(0.3)

while True:
    # Obtener mensajes de Telegram
    mensaje_recibido = obtener_mensaje_de_telegram()

    if mensaje_recibido:
        # Mostrar el mensaje en la matriz de LED
        longitud = len(mensaje_recibido) * 8  # Ancho total en píxeles del mensaje
        for x in range(30, -longitud, -3):
            matrix.text(mensaje_recibido, x, 0, 1)
            matrix.show()
            sleep(0.10)
            matrix.fill(0)

        mostrar_en_matriz(mensaje_recibido)
while True:
    # Obtener mensajes de Telegram
    mensaje_recibido = obtener_mensaje_de_telegram()

    if mensaje_recibido:
        # Mostrar el mensaje en la matriz de LED
        longitud = len(mensaje_recibido) * 8  # Ancho total en píxeles del mensaje
        for x in range(30, -longitud, -3):
            matrix.text(mensaje_recibido, x, 0, 1)
            matrix.show()
            sleep(0.10)
            matrix.fill(0)

        mostrar_en_matriz(mensaje_recibido)