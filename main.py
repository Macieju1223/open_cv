import cv2 as cv
import numpy as np

####------------------------------------------
haystack_img = cv.imread('images/cabbages.png', cv.IMREAD_UNCHANGED)
loock_img = cv.imread('check/cc4.png', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(haystack_img, loock_img, cv.TM_CCOEFF_NORMED)


# min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
# top_left = max_loc
#
# needle_w = loock_img.shape[1]
# needle_h = loock_img.shape[0]
# bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
#
# cv.rectangle(haystack_img, top_left, bottom_right, color=(0,255,0), thickness=2, lineType=cv.LINE_4)
# cv.imshow('result', haystack_img)
#
# cv.waitKey()
# ####------------------------------------------

treshold = 0.80

locations = np.where(result >= treshold)
locations = list(zip(*locations[::-1]))
print(locations)

if locations:
    needle_w = loock_img.shape[1]
    needle_h = loock_img.shape[0]
    line_color = (0,255,0)
    line_type = cv.LINE_4

    for loc in locations:
        top_left = loc
        bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
        cv.rectangle(haystack_img, top_left, bottom_right, line_color, line_type)

    cv.imshow('maches', haystack_img)
    cv.waitKey()