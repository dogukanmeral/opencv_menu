import cv2
import numpy as np

def find_shapes(cv2_image, minimum_area):
    
    gray = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 30, 150)

    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    vertices_of_shapes = []

    for contour in contours:
        area = cv2.contourArea(contour)
        if area < minimum_area:
            continue

        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        num_of_vertices = len(approx)
        vertices_of_shapes.append(num_of_vertices)

    return vertices_of_shapes