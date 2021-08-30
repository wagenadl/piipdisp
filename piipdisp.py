#!/usr/bin/python3

import time
import socket
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306 

def get_ip():
    '''get_ip() returns our IP address as a string, or "127.0.0.1" if not
    connected.'''
    # This code from stackexchange
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def get_time():
    '''get_time() returns local time as a string in M/D/Y HH:MM:SS format.'''
    y,m,d, H,M,S, _,_,_ = time.localtime()
    return f"{m}/{d}/{y} {H}:{M:02}:{S:02}"


disp = adafruit_ssd1306.SSD1306_128_32(rst=None)
disp.begin()

image = Image.new('1', (disp.width, disp.height))
draw = ImageDraw.Draw(image)

while True:
    ip = get_ip()
    t = get_time()

    draw.rectangle((0,0,disp.width, disp.height), outline=0, fill=0)
    
    font = ImageFont.truetype("Ubuntu-B.ttf", 16)
    draw.text((0, 0), ip, font=font, fill=255)

    font = ImageFont.truetype("Ubuntu-B.ttf", 12)
    draw.text((0,18), t, font=font, fill=255)

    disp.image(image)
    disp.display()

    time.sleep(1)
    
