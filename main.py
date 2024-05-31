import numpy as np
import cv2
from PIL import Image
import pytesseract
import re

filename = 'ktp.png'

# Open the image with PIL
pil_img = Image.open(filename)

# Convert the PIL image to an OpenCV image (numpy array)
img = np.array(pil_img)

norm_img = np.zeros((img.shape[0], img.shape[1]))
final_img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)

# Convert the normalized image to grayscale
gray_img = cv2.cvtColor(final_img, cv2.COLOR_BGR2GRAY)

# Now apply threshold and Gaussian blur on the grayscale image
# thresh_img = cv2.threshold(gray_img, 100, 255, cv2.THRESH_BINARY)[1]
# blurred_img = cv2.GaussianBlur(thresh_img, (1, 1), 0)

# Save the blurred image
# cv2.imwrite('exported.jpg', blurred_img)

text = pytesseract.image_to_string(gray_img)

lines = text.split('\n')
for line in lines:
    if "NIK" in line:
        print(line)