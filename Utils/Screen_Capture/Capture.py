import numpy as np
import cv2


def get_screen_image(sct):

    # Part of the screen to capture
    monitor = {"top": 221, "left": 275, "width": 300, "height": 240}

    # Get raw pixels from the screen, save it to a Numpy array
    img = np.array(sct.grab(monitor))

    # Load into Open CV and convert to gray
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return img_gray
