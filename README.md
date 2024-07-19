# Majisafi Innovation

## Overview

Majisafi Innovation is an IoT-based water pollution monitoring system that uses the SEN0189 turbidity sensor by DFRobot to measure water purity. The system provides real-time monitoring, data visualization, and alerts for hazardous water conditions.

## Features

- **Real-Time Monitoring:** Continuous measurement of water turbidity.
- **Data Visualization:** Interactive dashboard for viewing real-time and historical data.
- **Alerts and Notifications:** Instant alerts for unsafe water conditions.
- **Data Storage:** Centralized storage and analysis of water quality data.

## Components

- SEN0189 Turbidity Sensor by DFRobot
- Raspberry Pi (or Arduino with ADC)
- MCP3008 ADC (for Raspberry Pi)
- Flask Server for data reception and storage
- Python Libraries: `spidev`, `adafruit-circuitpython-mcp3xxx`, `pandas`, `matplotlib`, `flask`, `requests`

## Getting Started

### Hardware Setup

1. Connect the SEN0189 turbidity sensor to the Raspberry Pi using the provided connections.
2. Connect the MCP3008 ADC to the Raspberry Pi to interface with the sensor.

### Software Setup

1. Install the required Python libraries for sensor data collection and visualization.
2. Set up and run the Flask server to receive and store sensor data.
3. Run the sensor data collection script to start sending data to the server.
4. Use the data visualization script to analyze and view water quality trends.

## Usage

1. Start the Flask server to begin receiving data.
2. Run the sensor data collection script to continuously monitor water turbidity.
3. Use the visualization tools to review and analyze the data collected.

## Contribution

Contributions are welcome! To contribute, please fork the repository, create a new branch for your changes, and submit a pull request.

## Contact

- **Email:** [Your Email]
- **Phone:** [Your Phone Number]
- **Website:** [Your Website]
- **GitHub:** [Your GitHub Repository]

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
