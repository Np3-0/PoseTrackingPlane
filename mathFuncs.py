import math

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