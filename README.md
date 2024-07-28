The program captures live video from a webcam and replaces the red regions in the video with a predefined background image,
creating an "invisibility cloak" effect (inspired by Harry Potter). It is mainly coded in python and also uses numpy for
array manupulation and OpenCV for real-time computer vision.The key steps are:

Initialize Webcam and Load Background: Sets up the webcam and reads the background image.
Capture Frames: Continuously captures frames from the webcam.
Create Red Mask: Converts frames to HSV color space and creates masks to detect red regions.
Morphological Operations: Cleans up the mask to reduce noise.
Image Substitution: Replaces red regions in the frame with the background image and keeps non-red regions from the current frame.
Display Output: Shows the combined result in real-time.
Exit on 'q': Stops the program when the 'q' key is pressed.
