import cv2

img = cv2.imread('test.jpg', cv2.IMREAD_COLOR)

print(img.shape)

img[100:200, 50:100] = [0, 0, 0]

cv2.imshow('test', img)

cv2.waitKey()

cv2.destroyAllWindows()
