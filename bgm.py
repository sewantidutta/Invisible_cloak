import cv2
capture = cv2.VideoCapture(0) #this is my webcam

#getting the background image
while capture.isOpened():
    ret, bgm = capture.read() #simply reading from the web cam
    if ret:
        cv2.imshow("image", bgm)
        if cv2.waitKey(5) == ord('q'):
            #save the background image
            cv2.imwrite("image.jpg", bgm)
            break
cap.release()
cv2.destroyAllWindows()