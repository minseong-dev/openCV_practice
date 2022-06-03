import cv2

img = cv2.imread('test.jpg')

img_gray = (0.299 * img[:, :, 2]) + (0.587 * img[:, :, 1]) + (0.114 * img[:, :, 0])

cv2.imwrite('test_gray.jpg', img_gray)
img_gray = cv2.imread('test_gray.jpg')

cv2.imshow('output', img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()