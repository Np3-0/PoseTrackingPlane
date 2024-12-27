from poseEstimation import poseEstimationModule as pem
import cv2
import mediapipe as mp
import math

cap = cv2.VideoCapture(0)
pose = pem.poseDetector()
#https://en.wikipedia.org/wiki/Law_of_cosines

angles = [0, 0]

# points that are needed for the calculations
points = [[12, 14, 24], [11, 13, 23]]

def clamp(value, minV, maxV):
    return max(minV, min(value, maxV))

def getMidPoint(shoulder, waist) -> list:
    midpoint = [int((shoulder[1] + waist[1]) / 2), int((shoulder[2] + waist[2]) / 2)]
    return midpoint

def getDistances(pointA, pointB, pointC) -> list:
    # index 0 is shoulder - elbow, 1 is elbow to midpoint, 2 is shoulder to midpoint
    return [math.dist(pointA, pointB), math.dist(pointB, pointC), math.dist(pointA, pointC)]

def getAngles(a, b, c) -> int:
    return clamp(round(math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))), 0, 180)

while 1:
    ret, img = cap.read()
    if not ret: break
    
    img = pose.findPose(img)
    poseLms = pose.getPos(img)
    if not poseLms: continue
    
    for i in range(2):  
        midpoint = getMidPoint(poseLms[points[i][0]], poseLms[points[i][2]])
    
        # draws the midpoint and the third line to make it easier to visualize
        cv2.circle(img, (midpoint[0], midpoint[1]), 5, (0, 0, 255), 3)
        cv2.line(img, (poseLms[points[i][1]][1], poseLms[points[i][1]][2]), (midpoint[0], midpoint[1]), (0, 0, 255), 5)
    
        # gets the lengths of each line
        distances = getDistances([poseLms[points[i][0]][1], poseLms[points[i][0]][2]], [poseLms[points[i][1]][1], poseLms[points[i][1]][2]], [midpoint[0], midpoint[1]])
    
        # gets the angle in deg of the armpit (line a and c)
        angle = getAngles(distances[0], distances[1], distances[2])
        angles[i] = angle
    
    fps = pose.getFps()
    cv2.putText(img, f"Left Angle: {angles[1]}", (10, 140), cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 255), 3)
    cv2.putText(img, f"Right Angle: {angles[0]}", (10, 210), cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 255), 3)
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break