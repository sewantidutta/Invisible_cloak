import cv2 # for image processing
import numpy as np #mathematical library for image handling

capture = cv2.VideoCapture(0)
bgm = cv2.imread('./image.jpg')

while capture.isOpened():
    #caturing the live frame
    ret, current_frame = capture.read()
    if ret:
        #converting from rgb to hsv color space
        hsv_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)

        #range for lower red
        low_red = np.array([0,120,170])
        up_red = np.array([10,255,255])
        mask1 = cv2.inRange(hsv_frame, low_red, up_red)

        #range for upper red
        low_red = np.array([170,120,70])
        up_red = np.array([180,255,255])
        mask2 = cv2.inRange(hsv_frame, low_red, up_red)

        #generating the final red mask
        red_mask = mask1 + mask2

        red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations = 10) 
        red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_DILATE, np.ones((3,3), np.uint8), iterations = 1)  

        #subsituting the red portion with backgrpound image
        part1 = cv2.bitwise_and(bgm, bgm, mask= red_mask)
        
        # detecting things which are not red
        red_free = cv2.bitwise_not(red_mask)

        # if cloak is not present show the current image
        part2 = cv2.bitwise_and(current_frame, current_frame, mask= red_free)


        #final output
        cv2.imshow("cloak", part1 + part2)
        if cv2.waitKey(5) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()