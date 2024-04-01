# I2C pins
SCL_PIN = 22   # D22
SDA_PIN = 21   # D21

# Error led pin
LED_PIN = 2   # onboard led
LED_ON = 0    # inverse logic     
LED_OFF = 1

# Debug (LOW for debugging)
DEBUG_PIN = 5  # D5

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
