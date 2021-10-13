import cv2

def takeApic():
    # initialize the camera
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 0 -> index of camera
    s, img = cam.read()
    if s:  # frame captured without any errors
        cv2.namedWindow("cam-test", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("cam-test", img)
        cv2.waitKey(1000)
        cv2.imwrite("filename.jpg", img)  # save image
        cv2.destroyWindow("cam-test")