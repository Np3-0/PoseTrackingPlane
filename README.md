# Pose Tracking Plane
### An Arduino plane that decides the wing's angles from your arm position using mediapipe

## Requirements:
* Arduino
* 4 Servo Motors (This README will state information relating to [this](https://www.amazon.com/Micro-Helicopter-Airplane-Remote-Control/dp/B072V529YD) model)
* Webcam (connected to PC) 

## Setup
1. Install [Arduino IDE](https://www.arduino.cc/en/software) and [Python](https://www.python.org/downloads/) if not done already
2. Clone this repo!
3. Put the Arduino Code inside of its respective IDE, and the Python in one of your choosing (I recommend [VS Code](https://code.visualstudio.com/))
4. Install required dependencies
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**For Arduino**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Press `Ctr + Shift + i` or Go to `Tools` > `Manage Libraries`
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Search for Servo. Install if not installed
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**For Python**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Go to a terminal (integrated with your IDE or `CMD` that is in the directory of the project
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Type these commands:
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`pip install opencv-python`
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`pip install mediapipe`
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`pip install pyserial`

5. Set up Arduino:
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For each servo, Plug in the **BROWN** wire to `GND`, the **RED** to `5V`, and the **ORANGE** to `PIN 3 + 4` (Right arm) and `PIN 5 + 6` (Left arm)

6. Plug in Arduino
7. Click **Verify**, then **Upload** in the Arduino IDE
8. Run `python PlaneProj.py` in Python
9. Enjoy!


---
Made by Np3-0. with the MIT license
