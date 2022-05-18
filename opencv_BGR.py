import cv2

imgfile = 'test.jpg'
img = cv2.imread(imgfile, cv2.IMREAD_COLOR)
p = img[200, 100]
print(p)
img[200, 100] = [0, 0, 0]
cv2.imshow('test', img)
cv2.waitKey()
cv2.destroyAllWindows()