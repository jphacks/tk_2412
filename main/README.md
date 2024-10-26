# Hardware Project

## 1. Purpose
The project aims to develop a microcontroller-based hardware system capable of data acquisition and processing via serial communication. The system will connect multiple sensors and enable remote monitoring and control through Wi-Fi.

## 2. Key Technologies
The project primarily utilizes the following technologies:
- **ESP32**: Used as the development platform for the microcontroller, with hardware programming in C++.
- **Wi-Fi Module**: Enables remote data transmission and control functionality.
- **Python**: Used for implementing serial communication and data processing scripts.

## 3. Development Progress
- [X] Basic hardware architecture setup
- [X] Implementation of serial communication module and Wi-Fi management functions
- [ ] Integration of sensor data acquisition functionality
- [ ] Improvement of remote monitoring interface
- [ ] Optimization of serial communication stability
- [ ] Addition of error-handling mechanisms

## 4. Implementation Details
### File Structure
```text
main/
├── main.ino # Main program file for ESP32
├── SerialProxy.cpp # Serial communication implementation
├── SerialProxy.h # Serial communication header file
├── ADCReader.cpp # ADC reading implementation
├── ADCReader.h # ADC reading header file
├── WiFiManager.cpp # Wi-Fi management implementation
├── WiFiManager.h # Wi-Fi management header file
├── serial_ota.py # Serial OTA update script
└── config.h # Configuration file containing constants and settings
```

### Functionality of Each File
- `main.ino`: Arduino main program, containing initialization and main loop logic.
- `SerialProxy.cpp` and `SerialProxy.h`: Class and methods implementing serial communication, responsible for data transmission and reception.
- `ADCReader.cpp` and `ADCReader.h`: Handles reading of analog signals, providing functionality for reading ADC values.
- `WiFiManager.cpp` and `WiFiManager.h`: Manages Wi-Fi connections, handling connection setup and maintenance.
- `serial_ota.py`: Python script for OTA firmware updates via serial communication.
- `config.h`: Stores constants and configuration options used throughout the project.


## Highlights

- Modular Design: Each functional module is independent, ensuring code clarity and maintainability.
- Flexible Communication Methods: Supports both serial communication and Wi-Fi connection, suitable for different use cases.
- Remote Monitoring Capability: Enables remote data monitoring, facilitating real-time monitoring and management for users.
