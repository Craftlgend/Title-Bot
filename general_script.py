from ot
from time import sleep
from adb import tap, screenshot, input
import cv2
from database import Player, session
import os



#picture recognition
method = cv2.TM_SQDIFF

template = cv2.imread('template.png')



def run(requested_title):
    print ('start')
    next_player = session.query(Player).filter_by(title = requested_title).order_by(Player.id).first()
    if next_player == None:
        exit
    else:
        discord_name = next_player.discord_name
        x_coord = next_player.x_coord
        y_coord = next_player.y_coord
        kingdom_type = next_player.kingdom_type

        tap(400, 20)
        sleep(.8)
        if kingdom_type == 'lk':
            tap(450, 150)
            sleep(.8)
            input(str("#21161"))
            sleep(.8)
            tap(450, 150)
  
        tap(640, 140)
        sleep(.8)
        input(str(x_coord))
        tap(790, 140)
        sleep(.3)
        tap(790, 140)
        sleep(.8)
        input(str(y_coord))
        sleep(.3)
        tap(885, 140)
        tap(885, 140)
        sleep(.9)
        tap(640, 360)
        sleep(1)
        screenshot()
        sleep(1)
        screenshot = cv2.imread('screenshot.png')
        result = cv2.matchTemplate(screenshot, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        press_x =(min_loc[0]+20)
        press_y = (min_loc[1]+20)
        print (press_x, press_y)
        tap(press_x, press_y)
        sleep(.8)
        
        tap(520, 395)
        sleep(.8)
        tap(643, 634)
        os.remove('screenshot.png')
        session.delete(next_player)
        session.commit()
        timer()
        


async def timer():
    sleep(90)