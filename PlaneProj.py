from poseEstimation import poseEstimationModule as pem
import mathFuncs as mf
import cv2
import serial
import time
import threading

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=0.1)
cap = cv2.VideoCapture(0)
pose = pem.poseDetector()

angles = [0, 0]
# points that are needed for the calculations
points = [[12, 14, 24], [11, 13, 23]]

def writeToArduino(x):
    arduino.write(bytes(str(x), 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

# method for thread
def processFrame():
    global angles
    while True:
        ret, img = cap.read()
        if not ret:
            break
        
        img = pose.findPose(img)
        poseLms = pose.getPos(img)
        if not poseLms:
            continue
        
        for i in range(2):  
            midpoint = mf.getMidPoint(poseLms[points[i][0]], poseLms[points[i][2]])
        
            # Draw the midpoint and the third line to make it easier to visualize
            cv2.circle(img, (midpoint[0], midpoint[1]), 5, (0, 0, 255), 3)
            cv2.line(img, (poseLms[points[i][1]][1], poseLms[points[i][1]][2]), (midpoint[0], midpoint[1]), (0, 0, 255), 5)
        
            # Get the lengths of each line
            distances = mf.getDistances([poseLms[points[i][0]][1], poseLms[points[i][0]][2]], [poseLms[points[i][1]][1], poseLms[points[i][1]][2]], [midpoint[0], midpoint[1]])
        
            # Get the angle in degrees of the armpit (line a and c)
            angle = mf.getAngles(distances[0], distances[1], distances[2])
            angles[i] = angle
        
        cv2.putText(img, f"Left Angle: {angles[1]}", (10, 140), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        cv2.putText(img, f"Right Angle: {angles[0]}", (10, 210), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        cv2.putText(img, str(int(pose.getFps())), (10, 70), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 255), 3)
        cv2.imshow("Image", img)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

def sendToArduino():
    while True:
        # loop to send both over
        for angle in angles:
            val = writeToArduino(angle)
            print(val)
            time.sleep(0.1)  # slow down sending so the program isnt slow

# uhhhh it runs at 5 fps without threading
frameThread = threading.Thread(target=processFrame)
frameThread.start()

arduinoThread = threading.Thread(target=sendToArduino)
arduinoThread.start()

frameThread.join()
arduinoThread.join()

cap.release()
cv2.destroyAllWindows()