'''
    Lichtmeting in algen reactorfles (c)2024 Effevee
    
    Meten van de lichtsterkte in een algenkweek reactor. Naarmate de algengroei vordert, vermindert de licht doorlaatbaarheid. Op een bepaald punt
    is de algenkweek klaar en moet het reactorvat opnieuw gevuld worden. De lichtsensor metingen worden geupload naar het ThingSpeak IoT platform.
    Daar worden ze gemonitored en een email wordt verstuurd wanneer de kweek klaar is.   
    
    Hardware : - Wemos ESP32-S2 Mini V1.00 dev board
               - BH1750 lichtsensor
 
    Software : MicroPython code
    
    bedrading : ESP32      BH1750 
                Pin          Pin 
                -----      ------
                3V3   <-->   VCC
                GND   <-->   GND
                GPIO9 <-->   SCL
                GPIO8 <-->   SDA
                
    More details on https://github.com/effevee/esp32_lum
    
'''

####################################################################################
# Libraries
####################################################################################

from machine import Pin, SoftI2C, deepsleep
import network
import utime
import config
import sys
import urequests
from bh1750 import BH1750

   

####################################################################################
# Error routine
####################################################################################

def show_error():
    ''' visual display of error condition - flashing onboard LED '''
    
    # led pin object
    led = Pin(config.LED_PIN, Pin.OUT)
    
    # flash 3 times
    for i in range(3):
        led.value(1)
        utime.sleep(0.5)
        led.value(0)
        utime.sleep(0.5)


####################################################################################
# Connect to Wifi
####################################################################################

def connect_wifi():
    ''' connect the microcontroller to the local wifi network '''
    
    # disable AP mode of µcontroller
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)
    
    # enable STAtion mode of microcontroller
    sta_if = network.WLAN(network.STA_IF) 

    # if no wifi connection exist
    if not sta_if.isconnected():
        
        # debug message
        print('connecting to WiFi network...')
        
        # activate wifi station
        sta_if.active(True)
        
        # try to connect to the wifi network
        #sta_if.connect(config.SSID, config.PASS)  
        
        # keep trying for a number of times
        tries = 0
        while not sta_if.isconnected() and tries < config.MAX_TRIES:  
            
            sta_if.connect(config.SSID, config.PASS)  

            # show progress
            print('.', end='')
            
            # wait
            utime.sleep(1)
            
            # update counter
            tries += 1

    # show network status 
    if sta_if.isconnected():
        print('')
        print('connected to {} network with ip address {}' .format(config.SSID, sta_if.ifconfig()[0]))

    else:
        print('')
        print('no connection to {} network' .format(config.SSID))
        raise RuntimeError('WiFi connection failed')


####################################################################################
# Get sensor readings
####################################################################################

def get_sensor_readings():
    ''' get reading from sensor '''
    
    # debug message
    print('Getting sensor readings')
    
    # I2C object
    i2c = SoftI2C(scl=Pin(config.SCL_PIN), sda=Pin(config.SDA_PIN))
    
    # BH1750FVI light sensor
    bh1750 = BH1750(i2c)
    
    # check if BH1750 sensor is detected
    if 35 not in i2c.scan():
        raise RuntimeError('Cannot find BH1750 sensor')
    
    # read BH1750 sensor
    bh1750_lum = bh1750.luminance(BH1750.ONCE_HIRES_1)
    
    if config.DEBUG:
        print('BH1750FVI L: {:.0f} lux' .format(bh1750_lum))

    return [{'bh1750_lum': bh1750_lum}]
    

####################################################################################
# Upload sensor values to ThingSpeak
####################################################################################

def log_sensor_readings(sensor_data):
    ''' upload sensor readings to ThingSpeak '''
    
    # debug message
    print('Invoking ThingSpeak logging webhook')
    
    # extract readings to upload
    luminance = sensor_data[0]['bh1750_lum']
    
    # webhook url
    url = config.THINGSPEAK_URL.format(api=config.THINGSPEAK_WRITE_API, lum=luminance)
    
    # send GET request
    response = urequests.get(url)
    
    # evaluate response
    if response.status_code < 400:
        print('Webhook ThingSpeak success')

    else:
        print('Webhook ThingSpeak failed')
        raise RuntimeError('Webhook ThingSpeak failed')
    

####################################################################################
# deepsleep until next measurement
####################################################################################

def deepsleep_till_next_cycle():
    ''' put the µcontroller into deepsleep to save battery for config.INTERVAL seconds. '''
    
    # debug message
    print('Going into deepsleep for {} seconds...' .format(config.INTERVAL))
    utime.sleep(2)
   
    # goto deepsleep - time in milliseconds !
    deepsleep(config.INTERVAL * 1000)
    
    
####################################################################################
# Main program
####################################################################################

def run():
    ''' main program logic '''
    
    try:
        
        # connect to WiFi network
        connect_wifi()
        
        # get sensor readings
        sensor_data = get_sensor_readings()
        
        # upload sensor readings to ThingSpeak
        log_sensor_readings(sensor_data)

    except Exception as exc:
        sys.print_exception(exc)
        show_error()
    
    # goto deepsleep if not in debugging mode
    if not config.DEBUG:
        deepsleep_till_next_cycle()
        

run()
        
