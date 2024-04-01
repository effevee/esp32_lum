# esp32_lum

Meten van de lichtsterkte in een algen reactorvat. Naarmate de algengroei vordert, vermindert de licht doorlaatbaarheid van het reactorvat. Op een bepaald punt
is de algenkweek klaar en moet het reactorvat opnieuw gevuld worden. De lichtsterkte metingen worden geupload naar het ThingSpeak IoT platform.
Daar worden ze gemonitored en een email wordt verstuurd wanneer de kweek klaar is.   

## Hardware

#### DOIT ESP32 V1 Microcontroller

![We gebruiken als microprocessor een DOIT ESP32 V1 dev bord](images/doit_esp32_v1_pins.jpg)

#### BH1750 licht sensor
![Voor de lichtmeting gebruiken we een BH1750 sensor](images/bh1750_light_sensor_pins.jpg)

## Bedrading
ESP32 Pin|DH1750 Pin
:--:|:--:|
|3V3||VCC|
|GND||GND|
|D22|SCL|
|D21|SDA|
|D5*|GND*|
*Debug ON

## MicroPython software

#### [code](sourcecode/micropython/esp32_lum.py)
#### [config](sourcecode/micropython/config.py)
#### [BH1750 bibliotheek](sourcecode/micropython/bh1750.py)

## ThingSpeak IoT platform

De sensor metingen worden upgeload naar het ThingSpeak IoT platform.
![ThingSpeak Dashboard](images/thingspeak_dashboard.jpg)