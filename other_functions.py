from database import first_player_title
from adb import tap
from time import sleep
import cv2

method = cv2.TM_SQDIFF



def press_title(requested_title):
        print (requested_title)
        if requested_title == "duke":
            tap(520, 395)
        elif requested_title == "architect":
            tap(755, 395)
        elif requested_title == "justice":
            tap(295, 395)
        elif requested_title == "scientist":
            tap(982, 395)
        else:
            print("Error")

def lk(kingdom_type):
    if kingdom_type == 'lk':
        tap(450, 150)
        sleep(.8)
        input(str("#21161"))
        sleep(.8)
        tap(450, 150)

#picture recognition
def picture_recognition(template, picture):
        screenshot = cv2.imread(picture)
        result = cv2.matchTemplate(screenshot, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        return min_loc