import time
import cv2
import pyautogui
import random
import mss

from Utils.Screen_Capture.Capture import get_screen_image
from Utils.Get_Known_Moles.get_known_moles import get_moles
from Utils.Label_Moles.find_moles_on_screen import find_moles

# Get known mole images for pattern matching
known_moles = get_moles()

run_time = 60  # minutes
start_time = time.time()

with mss.mss() as sct:
    while True:
        # Track time for monitoring frames per second FPS
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        screenshot = get_screen_image(sct)

        # Label any known moles on screenshot
        labeled_screenshot, locations = find_moles(screenshot, known_moles)

        # Display the labeled picture in a good location
        cv2.namedWindow('labeled_game')
        cv2.imshow('labeled_game', labeled_screenshot)
        cv2.moveWindow('labeled_game', 100, 600)

        # Click on a random mole and wait
        if len(locations) > 0:
            # Pick a random mole to select
            random_selection = locations[random.randint(0, len(locations)-1)]
            x, y = random_selection

            pyautogui.moveTo(x=x, y=y)
            pyautogui.click()
            # time.sleep(0.01)

        # Print a statement monitoring FPS
        print("fps: {}".format(1 / (time.time() - last_time)))

        # Press "q" to quit
        key = cv2.waitKey(1)
        if key == ord('q'):
            cv2.destroyAllWindows()
            break

        elapsed_time = time.time() - start_time

        if elapsed_time > run_time * 60:
            print("time elapsed")
            break