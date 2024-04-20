# esp32_lum

Meten van de lichtsterkte in een algenkweek reactor. Naarmate de algengroei vordert, vermindert de licht doorlaatbaarheid. Op een bepaald punt is de algenkweek klaar en moet het reactorvat opnieuw gevuld worden. De lichtsensor metingen worden geupload naar het ThingSpeak IoT platform.
Daar worden ze gemonitored en een email wordt verstuurd wanneer de kweek klaar is.   
  
## Hardware

#### Wemos ESP32-S2 Mini Microcontroller

[datasheet](resources/esp32-s2_datasheet_en.pdf)

![We gebruiken als microprocessor een Wemos ESP32-S2 Mini dev bord](images/wemos_esp32_s2_mini.jpg)

#### BH1750 licht sensor

[datasheet](resources/Rohm-BH1750FVI-TR-datasheet.pdf)

![Voor de lichtmeting gebruiken we een BH1750 sensor](images/bh1750_light_sensor_pins.jpg)

## Bedrading
![Bedrading schema](images/wiring_esp32_s2_bh1750.jpg)

ESP32 Pin|DH1750 Pin
:--:|:--:|
|3V3|VCC|
|GND|GND|
|GPIO9|SCL|
|GPIO8|SDA|

## Behuizing

![Algemeen zicht behuizing](images/case_box_top.jpg)

#### [STL behuizing box](case/lichtmeter_box.stl)
#### [STL behuizing top](case/lichtmeter_top.stl)
#### ![montage lichtsensor](images/case_1.jpg)
#### ![montage microcontroller](images/case_2.jpg)
#### ![zicht bovenaan](images/case_3.jpg)
#### ![zicht onderaan met opening lichtsensor](images/case_4.jpg)
## MicroPython software

#### [code](sourcecode/micropython/esp32_lum.py)
#### [config](sourcecode/micropython/config.py)
#### [BH1750 bibliotheek](sourcecode/micropython/bh1750.py)

## ThingSpeak IoT platform

De sensor metingen worden upgeload naar het ThingSpeak IoT platform.

![ThingSpeak Dashboard](images/thingspeak_dashboard.jpg)

