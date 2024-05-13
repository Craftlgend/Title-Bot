from adb import tap
from time import sleep
from cv2 import imread, matchTemplate, minMaxLoc, TM_SQDIFF
from threading import Thread
from os import remove

method = TM_SQDIFF


#presses on the title that was requested
def press_title(requested_title):
        if requested_title == "Duke":
            tap(520, 395)
        elif requested_title == "Architect":
            tap(755, 395)
        elif requested_title == "Justice":
            tap(295, 395)
        elif requested_title == "Scientist":
            tap(982, 395)
        else:
            print("Error")

#types the kingdom if requested
def lk(kingdom_type):
    if kingdom_type == 'lk':
        tap(450, 150)
        sleep(.8)
        input(str("#21161"))
        sleep(.8)
        tap(450, 150)

#starts the timers for the titles
def timer(requested_title):
        if requested_title == "Duke":
            Thread(target= Duke).start()
        elif requested_title == "Architect":
            Thread(target= Architect).start()
        elif requested_title == "Justice":
            Thread(target= Justice).start()
        elif requested_title == "Scientist":
            Thread(target= Scientist).start()
        else:
            print("Error")     

def Duke():
     open("Duke.pid", "x")
     sleep(90)
     remove("Duke.pid")
def Architect():
     open("Architect.pid", "x")
     sleep(90)
     remove("Architect.pid")
def Justice():
     open("Justice.pid", "x")
     sleep(90)
     remove("Justice.pid")
def Scientist():
     open("Scientist.pid", "x")
     sleep(90)
     remove("Scientist.pid")
     
#picture recognition
def picture_recognition(template, picture):
        screenshot = imread(picture)
        result = matchTemplate(screenshot, template, method)
        min_val, max_val, min_loc, max_loc = minMaxLoc(result)
        return min_loc