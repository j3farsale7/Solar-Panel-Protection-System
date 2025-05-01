# 🛡️ Solar Panel Protection System

**Project by:** Jaafar Ali Saleh  
**GitHub:** [@j3farsale7](https://github.com/j3farsale7)  
**Email:** j3farsale7@outlook.com  
**Year:** 2024  
**License:** [Creative Commons Attribution-NonCommercial 4.0 International License](LICENSE)

---

## 📌 Overview

This is a **hardware-based solar panel protection system** using **Raspberry Pi**, designed to:
- Detect theft using an **infrared proximity sensor**
- Protect panels from overheating using **luminance sensors**
- Automatically cover/uncover panels using **DC motors**
- Provide real-time feedback via **LCD display**
- Support manual override using a **push-button**

---

## ✨ Features

- Theft detection and prevention  
- Brightness-based panel coverage  
- Manual control with LCD messages  
- Modular logic design  
- Non-commercial use only (license included)

---

## 🧩 Hardware Used

| COMPONENT      | DESCRIPTION |
|----------------|-------|
| Raspberry Pi 3 | Main controller |
| Grove Luminance Sensor x2 | Measures light intensity |
| Grove Infrared Proximity Sensor | Detects nearby objects (possible theft) |
| DC Motors x2 | Control panel covers |
| Adafruit Servo Motor HAT | Controls locking mechanism |
| LCD RGB Display | Provides visual feedback |
| Button Breakout Board | Manual input for covering/uncovering |

---

## 🐍 Software Stack

- **Language:** Python  
- **Libraries Used:** goto, stddef, var, pio, resource, cpu, FileStore, timer, VFP, Grove, Generic, AdafruitHATs  
- **Logic Style:** State-based decision making  

---

## 🧠 How It Works

### 🔍 Theft Detection
If an object comes within ~80cm of the panel:  
- The system locks the cover  
- Displays `"Caution! Please Check"` on the LCD  

### ☀️ Brightness Protection
When luminance > 900 Lux:  
- Panels are automatically covered to prevent overheating  
- Message displayed: `"Covering P1 TOO HOT weather"`  

### ❓ Why luminance?
- Because of the urge of making something authentic using only default Proteus library
- Same princible and idea of a heat sensor

### 🖐️ Manual Override
Press the button:
- While unlocked → lock and cover panels  
- While locked → unlock and uncover panels  

---

## 📝 Notes

This project is licensed under **CC BY-NC 4.0** — you may share and adapt it, but **not for commercial purposes** without permission.

For commercial licensing or collaboration, contact:  
📧 Email: j3farsale7@outlook.com  
🐱 GitHub: @j3farsale7  

---

## 🎓 Acknowledgments

- Supervised by Engineer Ali Rustom  
- Developed at Tartous University – Faculty of Information Technology and Communications Engineering  

---

## 📬 Feedback / Contributions

Suggestions, improvements, and bug reports are welcome!  
Feel free to open an issue or submit a pull request.