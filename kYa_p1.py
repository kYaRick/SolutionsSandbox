#libs scope:
import numpy as np
import cv2


#~~~~~~~~~~~~ Config flags ~~~~~~~~~~~~#
IMG_DEMO_TIME = 2000                #ms
IS_SHOW_TASK_1 = False
IS_SHOW_TASK_2 = False
IS_SHOW_TASK_3 = False
IS_SHOW_TASK_4 = False
IS_SHOW_TASK_5 = False

#Sources path:
img = cv2.imread("src/giraffe.png")
img2 = cv2.imread("src/wynn.png")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


#region 1 - Loading, Displaying, and Saving Images Quiz
#~> info:
# - Height represents the number of pixel rows in the image or the number of pixels in each column of the image array.
# - Width represents the number of pixel columns in the image or the number of pixels in each row of the image array.
# - Number of Channels represents the number of components used to represent each pixel.
if IS_SHOW_TASK_1:
    print("#1 - Image info:")
    print(f"\theight: {img.shape[0]}")
    print(f"\twidth: {img.shape[1]}")
    print(f"\tNofC: {img.shape[2]}")    #RGB

    cv2.imshow("Window title - 'Hi, I am your img-object!'", img)
    cv2.waitKey(IMG_DEMO_TIME)
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
#region 2 - Image Basics Quiz
if IS_SHOW_TASK_2:
    rows = 383
    columns = 972
    pixels = rows * columns
    print("#2 - Pixels in the image with {} rows and {} columns: {}".format(rows, columns, pixels))

    b, g, r = cv2.split(img)

    bgr_b = cv2.merge((b, np.zeros_like(b), np.zeros_like(b)))
    bgr_g = cv2.merge((np.zeros_like(g), g, np.zeros_like(g)))
    bgr_r = cv2.merge((np.zeros_like(r), np.zeros_like(r), r))

    cv2.imshow('Blue channel', bgr_b)
    cv2.imshow('Green channel', bgr_g)
    cv2.imshow('Red channel', bgr_r)
    cv2.waitKey(IMG_DEMO_TIME)
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
#region 3 - Drawing Quiz
if IS_SHOW_TASK_3:
    canvas = np.zeros((200, 300, 3), dtype="uint8")
    canvas[:] = 255
    cv2.rectangle(canvas, (10, 10), (60, 60), (255, 0, 0), -1)
    cv2.imshow("Task 3", canvas)
    cv2.waitKey(IMG_DEMO_TIME)
#~> "Corect answers"
# - What is the correct line of code to construct a blank canvas with a width of 300 pixels and a height of 200 pixels?
#   -- canvas = np.zeros((200, 300), dtype="uint8")
# - What is the correct line of code to draw a blue, filled-in rectangle starting at point (10, 10) and ending at point (60, 60)?
#   -- cv2.rectangle(canvas, (10, 10), (60, 60), (255, 0, 0), -1)
#endregion
#region 4 - Translation Quiz
#info: https://pyimagesearch.com/2021/02/03/opencv-image-translation/
if IS_SHOW_TASK_4:
    a_matrix = np.array([[1, 0, 30], [0, 1, -50]], dtype=np.float32)
    u50r30 = cv2.warpAffine(img, a_matrix, (img.shape[1], img.shape[0])) 

    a_matrix = np.array([[1, 0, -10], [0, 1, 90]], dtype=np.float32)
    d90l10 = cv2.warpAffine(img, a_matrix, (img.shape[1], img.shape[0]))

    a_matrix = np.array([[1, 0, -15], [0, 1, -20]], dtype=np.float32)
    u15l20 = cv2.warpAffine(img, a_matrix, (img.shape[1], img.shape[0]))

    cv2.imshow("Image: u50r30", u50r30)
    cv2.imshow("Image: d90l10", d90l10)
    cv2.imshow("Image: u15l20", u15l20)
    cv2.waitKey(IMG_DEMO_TIME)
    cv2.destroyAllWindows()
#~> "Corect answers"
# - Define a translation matrix to shift an image 30 pixels up and 50 pixels to the right.
#   -- M = np.float32([[1, 0, 50], [0, 1, -30]])
# - Define a translation matrix to shift an image 90 pixels down and 10 pixels to to the left.
#   -- M = np.float32([[1, 0, -10], [0, 1, 90]])
# - Define a translation matrix to shift an image 15 pixels to the left and 20 pixels up.
#   -- M = np.float32([[1, 0, -15], [0, 1, -20]])
#endregion
#region 5 - Rotation Quiz
if IS_SHOW_TASK_5:
    
    def rotate(in_image, angle, t_x = 0, t_y = 0, is_clockwise = True):
        height, width = img2.shape[:2]

        if (t_x == 0 and t_y == 0):
            t_x = width//2
            t_y = height//2

        angle = -angle if is_clockwise else angle 

        a_matrix = cv2.getRotationMatrix2D((t_x, t_y), angle, 1)
        return cv2.warpAffine(in_image, a_matrix, (width, height))
    
    list([1, 2, 3]).reverse

    print(f"After rotated the image 30 degrees clockwise at point x=335 and y=254,\n\tpixel state next: {rotate(img2, 30)[254, 335]}")
    print(f"After rotated the image 110 degrees counter-clockwise at point x=312 and y=136,\n\tpixel state next: {rotate(img2, -110)[136, 312]}")
    print(f"After rotated the image 88 degrees counter-clockwise x=10 and y=10,\n\tpixel state next: {rotate(img2, -88, 50, 50)[10, 10]}")

#~> "Corect answers"
# - Use OpenCV to rotate the image 30 degrees clockwise. What is the value of the pixel located at x=335 and y=254? (wynn.png)
#   -- R=95, G=93, B=61
# - Now rotate the image 110 degrees counter-clockwise. What is the value of the pixel located at x=312, y=136? (wynn.png)
#   -- R=180, G=141, B=148
# - Change the call to cv2.getRotationMatrix2D to rotate the image 88 degrees counter-clockwise about coordinate (50, 50). What is the value of the pixel located at point (10, 10)? (wynn.png)
#   -- R=28, G=81, B=67
#endregion