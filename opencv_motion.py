import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
if not capture.isOpened():
    print("capture open failed")
    exit()

while True:
    ret, img01 = capture.read()
    ret, img02 = capture.read()
    ret, img03 = capture.read()
    if not ret:
        print("capture read failed")
        break

    gray_img01 = cv2.cvtColor(img01, cv2.COLOR_BGR2GRAY)
    gray_img02 = cv2.cvtColor(img02, cv2.COLOR_BGR2GRAY)
    gray_img03 = cv2.cvtColor(img03, cv2.COLOR_BGR2GRAY)

    difference_01 = cv2.absdiff(gray_img01, gray_img02)
    difference_02 = cv2.absdiff(gray_img02, gray_img03)

    ret, difference_01 = cv2.threshold(difference_01, 20, 255, cv2.THRESH_BINARY)
    ret, difference_02 = cv2.threshold(difference_02, 20, 255, cv2.THRESH_BINARY)

    diff = cv2.bitwise_and(difference_01, difference_02)
    diff_cnt = cv2.countNonZero(diff)

    cv2.imshow("motion", diff)

    print(diff_cnt)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()