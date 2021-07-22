'''
      Image to Pencil Sketch with Python
      The only library we need for converting an image into a pencil sketch with Python is an OpenCV library 
      Command to install CV: pip install opencv-python
'''

import cv2


'''
    Now the next thing to do is to read the image
    cv2.imshow(“Title You want to give”, Image) and 
    then simply write cv2.waitKey(0). 
    This will display the image
'''

image = cv2.imread("a.jpg")  #image_Read
cv2.imshow("Orignal Img", image)   #display the image
cv2.waitKey(0)               #display the image 

'''
#To create a new image by converting the original image to greyscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  #cv2. cvtColor(input_image, flag) method is used to convert an image from one color space to another
cv2.imshow("Black & White", gray_image)
cv2.waitKey(0)

#next step is to invert the new grayscale image
inverted_image = 255 - gray_image
cv2.imshow("Inverted -ve Img", inverted_image)
cv2.waitKey()


#next step in the process is to blur the image by using the Gaussian Function in OpenCV
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

#final step is to invert the blurred image, then we can easily convert the image into a pencil sketch
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)


'''
#if you want to have a look at both the original image and the pencil sketch side by side
cv2.imshow("original image", image)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted_image = 255 - gray_image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=150.0)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)




