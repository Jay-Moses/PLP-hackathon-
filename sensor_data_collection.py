import time
import board
import busio
import digitalio
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import requests

# SPI setup for MCP3008
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP.MCP3008(spi, cs)

# Define the channel for the SEN0189 sensor
chan = AnalogIn(mcp, MCP.P0)

# Server URL to send data
SERVER_URL = "http://your_server_address/api/data"

def read_turbidity():
    return chan.value

def send_data(turbidity):
    data = {'turbidity': turbidity}
    response = requests.post(SERVER_URL, json=data)
    return response.status_code

def main():
    while True:
        turbidity = read_turbidity()
        if turbidity is not None:
            status = send_data(turbidity)
            print(f"Turbidity: {turbidity}, Data sent. Status code: {status}")
        else:
            print("Failed to retrieve data from the sensor")
        time.sleep(60)  # Adjust the sleep time as needed

if __name__ == "__main__":
    main()
