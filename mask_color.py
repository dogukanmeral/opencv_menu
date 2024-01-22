import cv2
import numpy as np  

def mask_color(cv2_image, lower_value, upper_value):
	image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2HSV)

	lower_hsv = np.array([lower_value, 100, 20])
	upper_hsv = np.array([upper_value, 255, 255])

	return cv2.inRange(image, lower_hsv, upper_hsv)