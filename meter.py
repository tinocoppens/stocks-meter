import finnhub
import unicornhat
unicornhat.set_layout(unicornhat.PHAT)
unicornhat.brightness(0.25)
finnhub_client = finnhub.Client(api_key="Place token here")
def linksgroenrechtsgroen():
    unicornhat.clear()
    unicornhat.set_layout(unicornhat.PHAT)
    unicornhat.brightness(0.25)
    unicornhat.set_pixel(6, 0, 0, 255, 0)
    unicornhat.set_pixel(6, 1, 0, 255, 0)
    unicornhat.set_pixel(6, 2, 0, 255, 0)
    unicornhat.set_pixel(6, 3, 0, 255, 0)
    unicornhat.set_pixel(5, 1, 0, 255, 0)
    unicornhat.set_pixel(7, 1, 0, 255, 0)
    unicornhat.set_pixel(1, 0, 0, 255, 0)
    unicornhat.set_pixel(1, 1, 0, 255, 0)
    unicornhat.set_pixel(1, 2, 0, 255, 0)
    unicornhat.set_pixel(1, 3, 0, 255, 0)
    unicornhat.set_pixel(0, 1, 0, 255, 0)
    unicornhat.set_pixel(2, 1, 0, 255, 0)
    unicornhat.show()
def linksgroenrechtsrood():
    unicornhat.clear()
    unicornhat.set_layout(unicornhat.PHAT)
    unicornhat.brightness(0.25)
    unicornhat.set_pixel(1, 0, 0, 255, 0)
    unicornhat.set_pixel(1, 1, 0, 255, 0)
    unicornhat.set_pixel(1, 2, 0, 255, 0)
    unicornhat.set_pixel(1, 3, 0, 255, 0)
    unicornhat.set_pixel(0, 1, 0, 255, 0)
    unicornhat.set_pixel(2, 1, 0, 255, 0)
    unicornhat.set_pixel(6, 0, 255, 0, 0)
    unicornhat.set_pixel(6, 1, 255, 0, 0)
    unicornhat.set_pixel(6, 2, 255, 0, 0)
    unicornhat.set_pixel(6, 3, 255, 0, 0)
    unicornhat.set_pixel(5, 2, 255, 0, 0)
    unicornhat.set_pixel(7, 2, 255, 0, 0)
    unicornhat.show()
def linksroodrechtsgroen():
    unicornhat.clear()
    unicornhat.set_layout(unicornhat.PHAT)
    unicornhat.brightness(0.25)
    unicornhat.set_pixel(1, 0, 255, 0, 0)
    unicornhat.set_pixel(1, 1, 255, 0, 0)
    unicornhat.set_pixel(1, 2, 255, 0, 0)
    unicornhat.set_pixel(1, 3, 255, 0, 0)
    unicornhat.set_pixel(0, 2, 255, 0, 0)
    unicornhat.set_pixel(2, 2, 255, 0, 0)
    unicornhat.set_pixel(6, 0, 0, 255, 0)
    unicornhat.set_pixel(6, 1, 0, 255, 0)
    unicornhat.set_pixel(6, 2, 0, 255, 0)
    unicornhat.set_pixel(6, 3, 0, 255, 0)
    unicornhat.set_pixel(5, 1, 0, 255, 0)
    unicornhat.set_pixel(7, 1, 0, 255, 0)
    unicornhat.show()
def linksroodrechtsrood():
    unicornhat.clear()
    unicornhat.set_layout(unicornhat.PHAT)
    unicornhat.brightness(0.25)
    unicornhat.set_pixel(1, 0, 255, 0, 0)
    unicornhat.set_pixel(1, 1, 255, 0, 0)
    unicornhat.set_pixel(1, 2, 255, 0, 0)
    unicornhat.set_pixel(1, 3, 255, 0, 0)
    unicornhat.set_pixel(0, 2, 255, 0, 0)
    unicornhat.set_pixel(2, 2, 255, 0, 0)
    unicornhat.set_pixel(6, 0, 255, 0, 0)
    unicornhat.set_pixel(6, 1, 255, 0, 0)
    unicornhat.set_pixel(6, 2, 255, 0, 0)
    unicornhat.set_pixel(6, 3, 255, 0, 0)
    unicornhat.set_pixel(5, 2, 255, 0, 0)
    unicornhat.set_pixel(7, 2, 255, 0, 0)
    unicornhat.show()

import time
import json
while True:
    time.sleep(5)
    aankoopprijs = "Buy price"
    lasttime = aankoopprijs
    ALL = finnhub_client.quote('STOCK')
    ABG = str(ALL)
    mytext = ABG
    mytext = mytext.replace("'", '"')
    ALL = json.loads(mytext)
    c = ALL["c"]
    dp = ALL["dp"]
    int(c)
    int(dp)
    float(lasttime)
    if c >= float(lasttime) and dp > 0:
        linksgroenrechtsgroen()
    if c >= float(lasttime) and dp < 0:
        linksgroenrechtsrood()
    if c <= float(lasttime) and dp > 0:
        linksroodrechtsgroen()
    if c <= float(lasttime) and dp < 0:
        linksroodrechtsrood()
