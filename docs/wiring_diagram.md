# 📐 Wiring Diagram Description

Below is a textual description of how to wire the components. This helps when creating a visual diagram or replicating the setup.

## 🔌 Connection Summary

| Component | Connected To | Pin/Port |
|----------|--------------|----------|
| Grove HAT | Raspberry Pi | Stacked on GPIO |
| Adafruit Servo HAT | Raspberry Pi | I²C (SCL, SDA) |
| Servo Motor | Adafruit Servo HAT | Servo 0 |
| Luminance Sensor 1 | Grove HAT | AD0 |
| Luminance Sensor 2 | Grove HAT | AD1 |
| Infrared Sensor | Grove HAT | AD2 |
| LCD RGB Display | Raspberry Pi | I²C (SCL, SDA) |
| DC Motor 1 | Motor Shield | PWMA, DIRA, BRAKE-A |
| DC Motor 2 | Motor Shield | PWMB, DIRB, BRAKE-B |
| Push Button | Raspberry Pi | GPIO25 |
| Motor Shield | Raspberry Pi | Multiple GPIO (see list below) |

## 📝 Motor Shield Connections

| Function | GPIO Pin |
|---------|----------|
| PWMA | GPIO4 |
| PWMB | GPIO20 |
| DIRA | GPIO5 |
| DIRB | GPIO21 |
| BRAKE-A | GPIO6 |
| BRAKE-B | GPIO22 |
| SNSA | GPIO17 |
| SNSB | GPIO18 |