# libs scope:
import cv2
import numpy as np


# ~~~~~~~~~~~~ Config flags ~~~~~~~~~~~~#
# Timming:
IMG_DEMO_TIME = 2000  # ms

# Task flags:
IS_SHOW_TASK_1 = False
IS_SHOW_TASK_2 = False
IS_SHOW_TASK_3 = False
IS_SHOW_TASK_4 = False
IS_SHOW_TASK_5 = False
IS_SHOW_TASK_6 = False
IS_SHOW_TASK_7 = False
IS_SHOW_TASK_8 = False
IS_SHOW_TASK_9 = False
IS_SHOW_TASK_10 = False
IS_SHOW_TASK_11 = False
IS_SHOW_TASK_12 = False

# Sources path:
img = cv2.imread("src/giraffe.png")
img2 = cv2.imread("src/wynn.png")
img3 = cv2.imread("src/florida_trip_small.png")
img4 = cv2.imread("src/florida_trip.png")
img5 = cv2.imread("src/grand_canyon.png")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# region Global scope
def rotate(in_image, angle, t_x=0, t_y=0):
    if (t_x == 0 and t_y == 0):
        t_y, t_x = in_image.shape[:2]
        t_x //= 2
        t_y //= 2

    M = cv2.getRotationMatrix2D((t_x, t_y), angle, 1)
    return cv2.warpAffine(in_image, M, (in_image.shape[1], in_image.shape[0]))
# endregion
# region 1 - Loading, Displaying, and Saving Images Quiz
# ~> info:
# - Height represents the number of pixel rows in the image or the number of pixels in each column of the image array.
# - Width represents the number of pixel columns in the image or the number of pixels in each row of the image array.
# - Number of Channels represents the number of components used to represent each pixel.
if IS_SHOW_TASK_1:
    print("#1 - Image info:")
    print(f"\theight: {img.shape[0]}")
    print(f"\twidth: {img.shape[1]}")
    print(f"\tNofC: {img.shape[2]}")  # RGB

    cv2.imshow("Window title - 'Hi, I am your img-object!'", img)
    cv2.waitKey(IMG_DEMO_TIME)
# ~> "Corect answers"
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
# endregion
# region 2 - Image Basics Quiz
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
    print(
        f"\tred: {some_pixel_sate[-1]}, green:{some_pixel_sate[1]}, blue: {some_pixel_sate[0]}")
# ~> "Corect answers"
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
# endregion
# region 3 - Drawing Quiz
if IS_SHOW_TASK_3:
    canvas = np.zeros((200, 300, 3), dtype="uint8")
    canvas[:] = 255
    cv2.rectangle(canvas, (10, 10), (60, 60), (255, 0, 0), -1)
    cv2.imshow("Task 3", canvas)
    cv2.waitKey(IMG_DEMO_TIME)
# ~> "Corect answers"
# - What is the correct line of code to construct a blank canvas with a width of 300 pixels and a height of 200 pixels?
#   -- canvas = np.zeros((200, 300), dtype="uint8")
# - What is the correct line of code to draw a blue, filled-in rectangle starting at point (10, 10) and ending at point (60, 60)?
#   -- cv2.rectangle(canvas, (10, 10), (60, 60), (255, 0, 0), -1)
# endregion
# region 4 - Translation Quiz
# info: https://pyimagesearch.com/2021/02/03/opencv-image-translation/
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
# ~> "Corect answers"
# - Define a translation matrix to shift an image 30 pixels up and 50 pixels to the right.
#   -- M = np.float32([[1, 0, 50], [0, 1, -30]])
# - Define a translation matrix to shift an image 90 pixels down and 10 pixels to to the left.
#   -- M = np.float32([[1, 0, -10], [0, 1, 90]])
# - Define a translation matrix to shift an image 15 pixels to the left and 20 pixels up.
#   -- M = np.float32([[1, 0, -15], [0, 1, -20]])
# endregion
# region 5 - Rotation Quiz
if IS_SHOW_TASK_5:
    print(
        f"After rotated the image 30 degrees clockwise at point x=335 and y=254,\n\tpixel state next: {rotate(img2, 30)[254, 335]}")
    print(
        f"After rotated the image 110 degrees counter-clockwise at point x=312 and y=136,\n\tpixel state next: {rotate(img2, -110)[136, 312]}")
    print(
        f"After rotated the image 88 degrees counter-clockwise x=10 and y=10,\n\tpixel state next: {rotate(img2, -88, 50, 50)[10, 10]}")

# ~> "Corect answers"
# - Use OpenCV to rotate the image 30 degrees clockwise. What is the value of the pixel located at x=335 and y=254? (wynn.png)
#   -- R=88, G=129, B=162
# - Now rotate the image 110 degrees counter-clockwise. What is the value of the pixel located at x=312, y=136? (wynn.png)
#   -- R=39, G=111, B=166
# - Change the call to cv2.getRotationMatrix2D to rotate the image 88 degrees counter-clockwise about coordinate (50, 50). What is the value of the pixel located at point (10, 10)? (wynn.png)
#   -- R=180, G=141, B=148
# endregion
# region 6 - Resizing Quiz
if IS_SHOW_TASK_6:
    local_img_resz = cv2.resize(img3, (100, int(
        img.shape[0] * (100 / img.shape[1]))), interpolation=cv2.INTER_NEAREST)
    print("The pixel value located at x=20, y=74",  local_img_resz[74, 20])
    local_img_resz = cv2.resize(
        img3, (img.shape[1]*2, img.shape[0]*2), interpolation=cv2.INTER_CUBIC)
    print("The pixel value located at x=170, y=367",  local_img_resz[367, 170])

# ~> "Corect answers"
# - Why do we keep in mind the aspect ratio of an image when resizing?
#   -- Because ignoring the aspect ratio when resizing an image can lead to distorted and squished output images.
# - Download the source code to this lesson and use the florida_trip_small.png small image to answer the following question.
#   Resize the image to have a width of 100px using the cv2.INTER_NEAREST interpolation method.
#   What is (approximately) the pixel value located at x=20, y=74?
#   -- R=16, G=19, B=26
# - Now, use the same image to make the image twice it’s original size using cv2.INTER_CUBIC interpolation.
#   What is the value of the pixel located at x=170, y=367 in our resized image?
#   -- R=20, G=20, B=25
# endregion
# region 7 - Flipping Quiz
if IS_SHOW_TASK_7:
    img_rotated = rotate(cv2.flip(img4, 1), -45)
    print("The pixel value located at x=441, y=189",
          cv2.flip(img_rotated, 0)[189, 441])
# ~> "Corect answers"
# - Download the source code and images associated with this lesson.
#   Then, use the florida_trip.png to answer the following question.
#   Use OpenCV to flip the image horizontally — what is the value of the pixel located at x=259, y=235?
#   -- R=183, G=192, B=189
# - Use the original image from the previous question and flip it horizontally,
#   followed by a 45 degree counter-clockwise rotation, and lastly a vertical flip.
#   What is (approximately) the pixel value located at x=441, y=189?
#   -- R=195, G=149, B=133
# endregion
# region 8 - Cropping Quiz
if IS_SHOW_TASK_8:
    cv2.imshow("People", img4[173:235, 13:81])
    cv2.imshow("Boat", img4[124:212, 225:380])
    cv2.waitKey(IMG_DEMO_TIME)
# ~> "Corect answers"
# - What is the correct order to supply starting and ending coordinates to a NumPy array slice?
#   -- startY:endY, startX:endX
# - Download the source code and image to this lesson. Then, use the florida_trip.png 
#   image to answer the following question. What is the most appropriate NumPy array 
#   slice to crop the people in the background from the florida_trip.png image?
#   -- image[173:235, 13:81]
# - Use the same image from the previous question and determine the best NumPy 
#   slice to extract the boat/building-like structure from the background of florida_trip.png.
#   -- image[124:212, 225:380]
# endregion
# region 9 - Image Arithmetic Quiz
if IS_SHOW_TASK_9:
    def conv_uint8(num): 
        return 0 if num < 1 else 255 if num > 255 else num

    result = cv2.add(np.array([200]), np.array([68]))
    print(f"cv2 sum result: {conv_uint8(result)}")
    result = np.uint8(200) + np.uint8(68)
    print(f"numpu sum result: {result}")
    result = cv2.add(np.array([1]), np.array([-251]))
    print(f"cv2 sub result: {conv_uint8(result)}")
    result = np.uint8(1) - np.uint8(251)
    print(f"numpu sub result: {result}")

    result = cv2.add(img5, np.ones_like(img5).astype(np.uint8) * 75)
    print("grand_canyon.png after added value of 75\n\tresult pixel (x=61, y=152) state: ", result[152, 61])
# ~> "Corect answers"
# - Assuming 8-bit, unsigned integers, what is the output of 200 + 68 using OpenCV?
#   -- 255, but in my case I get in my case I get 268, although this is not correct, 
#       because if we turn to the resources, the processor uses an 8-bit system according 
#       to the RGB format, accordingly the maximum value will be 255 and if exceeded it will be 255.
# - Assuming 8-bit, unsigned integers, what is the output of 200 + 68 using NumPy?
#   -- 12
# - Again, assuming 8-bit unsigned integers, what is the output of 1 – 251 using OpenCV?
#   -- 0
# - What about the output of 1 – 251 using NumPy?
#   -- 6
# - Add value of 75 to all pixels to the grand_canyon.png image using the cv2.add function. 
#   What is the value of the pixel located at x=61, y=152?
#   -- R=176, G=117, B=99
# endregion
# region 10 - Bitwise Operations Quiz
if IS_SHOW_TASK_10:
    pass
# ~> "Corect answers"
# - What is the difference between a bitwise AND and OR?
#   -- A bitwise AND is only true when both inputs are > 0; a bitwise OR is true when either inputs are > 0.
# - What is the difference between a bitwise OR and XOR?
#   -- A bitwise OR is true when either input is > 0; 
#      a bitwise XOR is true if one of the inputs is > 0, but not both
# - What does the NOT operator do?
#   -- Inverts the "ON" and "OFF" pixels
# endregion
# region 11 - Masking Quiz
if IS_SHOW_TASK_11:
    # create a black image with a white square
    img = np.zeros((500, 500), dtype=np.uint8)
    cv2.rectangle(img, (100, 100), (400, 400), 255, -1)

    # display the image
    cv2.imshow('Task 11.1', img)

    x, y = 0, 0
    cv2.rectangle(img2, (x - 5, y - 5), (x + 5, y + 5), 255, -1)
    cv2.imshow('Task 11.2', img2)

    cv2.waitKey(IMG_DEMO_TIME)
    cv2.destroyAllWindows()
# ~> "Corect answers"
# - What function would you use to draw a square mask?
#   -- cv2.square
# - What is the correct code to draw a 10 x 10 square mask centered at coordinates (x, y)?
# - info:
#   here, we use cv2.rectangle() to draw a rectangle (which is a square, since both sides are equal) 
#   on the mask image. The first argument specifies the image on which to draw the rectangle, 
#   the second argument is the starting point of the rectangle, and the third argument is the ending 
#   point of the rectangle.
#   In this case, we specify the starting point as (x - 5, y - 5) and the ending point as (x + 5, y + 5). 
#   Since we want a 10 x 10 square, we subtract 5 from the x and y coordinates to get the starting point 
#   and add 5 to the x and y coordinates to get the ending point. The fourth argument specifies the color 
#   of the rectangle, which is 255 (white) in this case. Finally, the fifth argument specifies the thickness 
#   of the rectangle, which is -1 (filled rectangle) in this case.
#   -- cv2.rectangle(mask, (x - 5, y - 5), (x + 5, y + 5), 255, -1)
# endregion
# region 12 - Splitting and Merging Quiz
if IS_SHOW_TASK_12:
    print("Red channel (x=180, y=94): ", cv2.split(img3)[-1][94, 180])
    print("Green channel (x=73, y=13): ", cv2.split(img3)[1][78, 13])
    print("Blue channel (x=80, y=5): ", cv2.split(img3)[-1][5, 80])
# ~> "Corect answers"
# - What is the value of the Red channel at x=180, y=94?
#   -- 198
# - The value of the Blue channel at x=13, y=78
#   -- 82
# - And the Green channel at x=80, y=5?
#   -- 240
# endregion