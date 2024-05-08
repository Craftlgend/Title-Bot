from database import first_player_title
from adb import tap
from time import sleep
import cv2

method = cv2.TM_SQDIFF



def press_title():
        title_requested = first_player_title()
        print (title_requested)
        if title_requested == "duke":
            tap(520, 395)
        elif title_requested == "architect":
            tap(755, 395)
        elif title_requested == "justice":
            tap(295, 395)
        elif title_requested == "scientist":
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