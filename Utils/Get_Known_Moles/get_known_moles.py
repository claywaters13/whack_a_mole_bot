import os
import cv2
from pathlib import Path


mole_pictures_directory = str(Path(os.getcwd())) + '/mole_images'


def get_moles():
    moles = []
    for entry in os.scandir(mole_pictures_directory):
        # Get path to this specific entry
        mole = entry.path

        # load image into open cv
        mole_img = cv2.imread(mole, cv2.IMREAD_COLOR)

        # convert to black and white
        mole_img_gray = cv2.cvtColor(mole_img, cv2.COLOR_BGR2GRAY)

        # append this image to a list to be returned
        moles.append(mole_img_gray)

    return moles
