# 🛠️ Hardware Setup Guide

This document provides a step-by-step guide to setting up the hardware components used in the **Solar Panel Protection System**.

## 🔧 Required Components

| Component | Quantity | Notes |
|----------|----------|-------|
| Raspberry Pi 3 | 1 | Main controller |
| Grove HAT | 1 | For connecting sensors via I²C |
| Adafruit Servo Motor HAT | 1 | For controlling servo motor |
| Grove Luminance Sensor | 2 | Measures ambient light intensity |
| Grove Infrared Proximity Sensor | 1 | Detects nearby objects (theft) |
| DC Motors (Generic) | 2 | Controls panel covers |
| LCD RGB Display | 1 | Shows system status |
| Push Button Breakout Board | 1 | Manual override control |
| Servo Motor | 1 | Locking mechanism |
| Wires (male-to-female, male-to-male) | Several | For connections |
| Power Supply (5V–6V) | 1 | For Raspberry Pi and motors |

---

## ⚙️ Step-by-Step Setup Instructions

### 1. **Raspberry Pi Setup**
- Insert SD card with Raspbian OS.
- Connect power via Micro USB port.
- Enable I²C communication:
  - Run `sudo raspi-config`
  - Go to `Interfacing Options > I2C > Enable`

### 2. **Grove HAT Installation**
- Stack the Grove HAT on top of the Raspberry Pi GPIO pins.
- This board supports multiple interfaces: Digital, Analog, PWM, UART, and I²C.

### 3. **Adafruit Servo Motor HAT**
- Connect this HAT to the same I²C bus (stackable or use separate I²C address).
- Connect the Servo Motor to **Servo 0** port.
- Use the separate 5V–6V power connector for the servo.

### 4. **Luminance Sensors**
- Connect the first sensor to **AD0** on the Grove HAT.
- Connect the second sensor to **AD1** on the Grove HAT.

### 5. **Infrared Proximity Sensor**
- Connect to **AD2** on the Grove HAT.

### 6. **LCD RGB Display**
- Connect using I²C interface (SCL and SDA pins).

### 7. **DC Motors**
- Connect Motor 1 to **PWMA (GPIO4), DIRA (GPIO5), BRAKE-A (GPIO6)**  
- Connect Motor 2 to **PWMB (GPIO20), DIRB (GPIO21), BRAKE-B (GPIO22)**  
- Also connect **SNSA (GPIO17)** and **SNSB (GPIO18)** for current sensing.

### 8. **Push Button Breakout Board**
- Connect to **GPIO25**

### 9. **Final Checks**
- Ensure all connections are secure.
- Double-check power supply ratings.
- Test sensors individually before running full system code.