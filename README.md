#Majisafi Innovation
#Overview
Majisafi Innovation is an IoT-based water pollution monitoring system designed to measure the purity of water using the SEN0189 turbidity sensor by DFRobot. The system provides real-time data on water turbidity, which is visualized through a user-friendly dashboard and can trigger alerts for hazardous conditions.

Features
Real-Time Monitoring: Continuous measurement of water turbidity.
Data Visualization: Interactive dashboard for real-time and historical data analysis.
Alerts and Notifications: Instant notifications for hazardous water conditions.
Data Storage: Centralized storage and analysis of water quality data.
Components
SEN0189 Turbidity Sensor by DFRobot
Raspberry Pi (or Arduino with ADC)
MCP3008 ADC (for Raspberry Pi)
Flask Server for data reception and storage
Python Libraries: spidev, adafruit-circuitpython-mcp3xxx, pandas, matplotlib, flask, requests
Getting Started
Hardware Setup
Connect the SEN0189 Sensor:

VCC: Connect to 5V on the Raspberry Pi.
GND: Connect to GND on the Raspberry Pi.
A0: Connect to the MCP3008 ADC.
D0: Digital output (not used).
Connect the MCP3008 ADC:

VDD: Connect to 3.3V.
VREF: Connect to 3.3V.
AGND: Connect to GND.
DGND: Connect to GND.
CLK: Connect to SPI Clock (SCK).
DOUT: Connect to SPI MISO.
DIN: Connect to SPI MOSI.
CS/SHDN: Connect to SPI CS
