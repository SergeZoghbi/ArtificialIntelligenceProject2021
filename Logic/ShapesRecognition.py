import cv2


def is_circle(gray):
    gray = cv2.medianBlur(gray, 15)
    rows = gray.shape[0]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=30,
                               minRadius=1, maxRadius=500)
    if circles is not None:
        return True
    else:
        return False


def shapes_recognition(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print('Error opening image!')
        return -1
    # converting image into grayscale image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # setting threshold of gray image
    _, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # using a findContours() function
    contours, _ = cv2.findContours(
        threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    i = 0
    result = ''
    # list for storing names of shapes
    for contour in contours:

        # here we are ignoring first counter because
        # findcontour function detects whole image as shape
        if i == 0:
            i = 1
            continue

        # cv2.approxPloyDP() function to approximate the shape
        approx = cv2.approxPolyDP(
            contour, 0.01 * cv2.arcLength(contour, True), True)

        lenApprox = len(approx)

        if lenApprox == 3:
            return 'Triangle'

        elif lenApprox == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)
            # a square will have an aspect ratio that is approximately
            # equal to one, otherwise, the shape is a rectangle
            shape = "Square" if 0.95 <= ar <= 1.05 else "Quadrilateral"
            return shape

        elif lenApprox == 5:
            return 'Pentagon'

        elif lenApprox == 6:
            return 'Hexagon'

        elif is_circle(gray):
            return 'Circle'
