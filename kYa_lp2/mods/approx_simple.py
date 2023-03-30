import cv2
import imutils

# load the the cirles and squares image and convert it to grayscale
image = cv2.imread(r"C:\Git\github\kYaRick\SolutionsSandbox\kYa_lp2\src\circles_and_squares.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# find contours in the image
cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# loop over the contours
for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.01 * peri, True)

	# draw the outline of the contour and draw the text on the image
	cv2.drawContours(image, [c], -1, (0, 255, 255), 2)
	(x, y, w, h) = cv2.boundingRect(approx)

	# if the approximated contour has 4 vertices, then we are examining
	# a rectangle or circle
	if len(approx) == 4:
		cv2.putText(image, "Rectangle", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
			0.5, (0, 255, 255), 2)
	else:
		cv2.putText(image, "Circle", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
			0.5, (0, 255, 255), 2)

# show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)
