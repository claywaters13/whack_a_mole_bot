import numpy as np
import cv2
import time


def find_moles(screenshot, known_moles):
    labeled_screenshot = screenshot
    locations = []
    for mole in known_moles:

        # Save dimensions of mole for drawing box
        mole_w, mole_h = mole.shape[::-1]

        # Process the Image
        processed_screenshot = cv2.matchTemplate(screenshot, mole, cv2.TM_CCOEFF_NORMED)

        # Determine a threshold for pattern matching
        threshold = 0.7

        # Store the coordinates of a matching pattern
        loc = np.where(processed_screenshot > threshold)
        # if len(loc[0]) > 0:
        #     locations.append(loc)

        for pt in zip(*loc[::-1]):
            labeled_screenshot = cv2.rectangle(labeled_screenshot, pt, (pt[0] + mole_w, pt[1] + mole_h), (0, 255, 255), 2)
            locations.append((int(pt[0]+0.5*mole_w + 275), int(pt[1] + 0.5*mole_h + 221)))

    return labeled_screenshot, locations