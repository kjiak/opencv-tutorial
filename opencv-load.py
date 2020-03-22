#importing the opencv module  
import cv2 as cv  
import numpy as np

# using imread('path') and 0 denotes read as  grayscale image  
img = cv.imread(r'cat.jpeg',1)  
       
edges = cv.Canny(img, 100, 200)  
  
cv.imshow("Edge Detected Image", edges)  
cv.imshow("Original Image", img)  
cv.waitKey(0)  # waits until a key is pressed  
cv.destroyAllWindows()  # destroys the window showing image  
