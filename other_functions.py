from adb import tap
from time import sleep
import cv2
from threading import Thread
from os import remove

method = cv2.TM_SQDIFF



def press_title(requested_title):
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

def timer(requested_title):
        if requested_title == "duke":
            Thread(target= duke).start()
        elif requested_title == "architect":
            Thread(target= architect).start()
        elif requested_title == "justice":
            Thread(target= justice).start()
        elif requested_title == "scientist":
            Thread(target= scientist).start()
        else:
            print("Error")     

def duke():
     open("duke.pid", "x")
     sleep(90)
     remove("duke.pid")
def architect():
     open("architect.pid", "x")
     sleep(90)
     remove("architect.pid")
def justice():
     open("justice.pid", "x")
     sleep(90)
     remove("justice.pid")
def scientist():
     open("scientist.pid", "x")
     sleep(90)
     remove("scientist.pid")
     
#picture recognition
def picture_recognition(template, picture):
        screenshot = cv2.imread(picture)
        result = cv2.matchTemplate(screenshot, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        return min_loc