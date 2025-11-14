# Mars Rover Power Management Simulator & Edge AI Embedded Workflow

## Overview
This project simulates the power management system of NASA's Mars Perseverance Rover and demonstrates how to deploy a machine learning model on embedded hardware (Arduino/AVR) using a real workflow. It is part of a 4-week rotation to master hardware engineering and AI/ML integration.

## Features
- **Mars Rover Power Simulator**: Python simulation of RTG power, battery cycling, and thermal constraints over a Martian sol (24.6 hours).
- **Edge AI Workflow**: Train a RandomForest model in Python, export to C with micromlgen, and integrate into an Arduino project (PlatformIO).
- **Portfolio-Ready**: Designed for computer engineering students and professionals targeting AI hardware, embedded systems, or robotics roles.

## Project Structure
```
.
├── MarsRoverPowerSim.py         # Python: Mars rover power simulation & visualization
├── train_and_export_model.py    # Python: Train ML model and export to C header
├── sensor_data.csv              # Example sensor data for ML model
├── include/
│   └── model.h                  # Exported C model for Arduino
├── src/
│   └── main.cpp                 # Arduino code using the ML model
├── platformio.ini               # PlatformIO config for Arduino build
└── ...
```

## How to Use
### 1. Simulate Mars Rover Power
```sh
python3 MarsRoverPowerSim.py
```
- Visualizes power usage, battery state, and temperature over a Martian day.

### 2. Train & Export ML Model
- Edit `sensor_data.csv` with your own data (features + label column).
- Run:
```sh
python3 train_and_export_model.py
```
- This generates `include/model.h` for Arduino.

### 3. Build Embedded Project (Optional)
- Requires PlatformIO and Arduino toolchain.
```sh
pio run -t upload
```
- (No hardware required to build/test logic.)

## Learning Outcomes
- Power budgeting and thermal management for embedded/space systems
- ML model deployment on microcontrollers
- Full-stack workflow: Python → C → Embedded
- Portfolio and interview-ready documentation

## Author
[Your Name]

## License
MIT
