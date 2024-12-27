import cv2
import mediapipe as mp
import time

class poseDetector:
    
    def __init__(self, mode=False, complexity=1, smoothLms=True, enableSeg=False, smoothSeg=True, detectionCon = 0.5, trackCon = 0.5) -> None:
        self.mode = mode
        self.complexity = complexity
        self.smoothLms = smoothLms
        self.enableSeg = enableSeg
        self.smoothSeg = smoothSeg
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.pTime = 0

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.complexity, self.smoothLms, self.enableSeg, self.smoothSeg, self.detectionCon, self.trackCon)

    def findPose(self, img, draw=True):
        imgRgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRgb)
        if draw and self.results.pose_landmarks:
            self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img
    
    def getPos(self, img, draw=True) -> list:
        lms = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lms.append([id, cx, cy])
                if draw: cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        return lms
    
    def getFps(self):
        cTime = time.time()
        fps = 1 / (cTime - self.pTime)
        self.pTime = cTime
        return fps
    
def main():
    cap = cv2.VideoCapture(0)
    detector = poseDetector()
    
    while 1:
        ret, img = cap.read()
        if not ret:
            break
        
        img = detector.findPose(img)
        lms = detector.getPos(img)
        print(lms)
        fps = detector.getFps()
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 255), 5)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()