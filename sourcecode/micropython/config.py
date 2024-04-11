# I2C pins
SCL_PIN = 9   # GPIO9
SDA_PIN = 8   # GPIO8

# Error led pin
LED_PIN = 15  # onboard led

# Debug
DEBUG = True  # True/False

# interval between measurements (seconds)
INTERVAL = 15*60

# wifi credentials
SSID = "<your wifi ssid>"
PASS = "<your wifi password>"
MAX_TRIES = 20

# ThingSpeak service
THINGSPEAK_WRITE_API = "<Your ThingSpeak Write API key>"
THINGSPEAK_READ_API = "<Your ThingSpeak Read API key>"
THINGSPEAK_URL = "https://api.thingspeak.com/update?api_key={api}&field1={lum}"
