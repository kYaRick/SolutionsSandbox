#libs scope:
import numpy as np
import cv2


#~~~~~~~~~~~~ Config flags ~~~~~~~~~~~~#
IMG_DEMO_TIME = 1000                #ms
SHOW_IMAGE_TASK_1 = False
SHOW_BGR_CHANNELS_TASK_2 = False;

img = cv2.imread("src/giraffe.png")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


#region Loading, Displaying, and Saving Images Quiz
#~> info:
# - Height represents the number of pixel rows in the image or the number of pixels in each column of the image array.
# - Width represents the number of pixel columns in the image or the number of pixels in each row of the image array.
# - Number of Channels represents the number of components used to represent each pixel.
print("#1 - Image info:")
print(f"\theight: {img.shape[0]}")
print(f"\twidth: {img.shape[1]}")
print(f"\tNofC: {img.shape[2]}")    #RGB

if SHOW_IMAGE_TASK_1:
    cv2.imshow("Window title - 'Hi, I am your img-object!'", img)
    cv2.waitKey()
#~> "Corect answers"
# - What is the shape of the NumPy array? (giraffe.png) 
#   -- (300, 400, 3)
# - What is the width and height of the image? (giraffe.png) 
#   -- width=400, height=500
# - What does the cv2.imread function do? 
#   -- Loads an image from disk.
# - What does the cv2.imshow function do? 
#   -- Displays the image to our screen.
# - Why is the cv2.waitKey function important? 
#   -- Without it, our image would be displayed to screen, but would close automatically.
# - Why do we use command line arguments?
#   -- To ensure variables can be supplied at script runtime.
# - Suppose we wanted to add a command line argument that requires a user to supply an 
# output image filename. What would that line of code look like?
#   -- So, my answer based on https://stackoverflow.com/questions/50756306/syntax-for-ap-add-argument:
#   -- ap.add_argument("-o", "--output", required=True)
#endregion

#region Image Basics Quiz
rows = 383
columns = 972
pixels = rows * columns
print("#2 - Pixels in the image with {} rows and {} columns: {}".format(rows, columns, pixels))

if SHOW_BGR_CHANNELS_TASK_2:
    b, g, r = cv2.split(img)

    bgr_b = cv2.merge((b, np.zeros_like(b), np.zeros_like(b)))
    bgr_g = cv2.merge((np.zeros_like(g), g, np.zeros_like(g)))
    bgr_r = cv2.merge((np.zeros_like(r), np.zeros_like(r), r))

    cv2.imshow('Blue channel', bgr_b)
    cv2.imshow('Green channel', bgr_g)
    cv2.imshow('Red channel', bgr_r)
    cv2.waitKey()
    cv2.destroyAllWindows()

some_pixel_sate = img[225, 111]
print("Value of the pixel located at point x=111 and y=225, next:")
print(f"\tred: {some_pixel_sate[-1]}, green:{some_pixel_sate[1]}, blue: {some_pixel_sate[0]}")
#~> "Corect answers"
# - Suppose we have an image with 383 rows and 972 columns...
#   -- 372,276
# - Pixels in the RGB and grayscale color space are (normally) represented in the range:
#   -- 0 .. 255
# - OpenCV represents RGB images in which order?
#   -- BGR
# - Images are most commonly represented in which color space?
#   -- RGB
# - Suppose we wanted to construct the color blue using OpenCV. Of the options below, which is the correct representation of the color blue in OpenCV?
#   -- (255, 0, 0)
# - This time, let’s construct the color red using OpenCV. How would we define this triplet?
#   -- (0, 0, 255)
# - The point (0, 0) corresponds to which corner of the image?
#   -- Top-left
# - Both Python and NumPy are zero-indexed?
#   -- Yes, both Python and NumPy are zero-indexed, meaning that the first element of an array or list is at index 0.
# - Download the code associated with this lesson. What is the (approximate) value of the pixel located at point x=111 and y=225?
#   -- I didn't search for the tutorial files so I just did it with the giraffe image and got this:
#   -- Blue: 154 Green: 192 Red: 238
#endregion