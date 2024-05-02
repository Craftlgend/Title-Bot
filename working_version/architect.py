import time
import adb
import cv2
from database import Player, session
import os


#picture recognition
method = cv2.TM_SQDIFF

template = cv2.imread('template.png')

architect = ('Architect')

def run():
    print ('start')
    next_player = session.query(Player).filter_by(title = architect).order_by(Player.id).first()
    if next_player == None:
        exit
    else:
        discord_name = next_player.discord_name
        x_coord = next_player.x_coord
        y_coord = next_player.y_coord
        kingdom_type = next_player.kingdom_type

        adb.tap(400, 20)
        time.sleep(.8)
        if kingdom_type == 'lk':
            adb.tap(450, 150)
            time.sleep(.8)
            adb.tap(450, 150)


        
        adb.tap(640, 140)
        time.sleep(.8)
        adb.input(str(x_coord))
        adb.tap(790, 140)
        time.sleep(.3)
        adb.tap(790, 140)
        time.sleep(.8)
        adb.input(str(y_coord))
        time.sleep(.3)
        adb.tap(885, 140)
        adb.tap(885, 140)
        time.sleep(.9)
        adb.tap(640, 360)
        time.sleep(1)
        adb.screenshot()
        time.sleep(1)
        screenshot = cv2.imread('screenshot.png')
        result = cv2.matchTemplate(screenshot, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        press_x =(min_loc[0]+20)
        press_y = (min_loc[1]+20)
        print (press_x, press_y)
        adb.tap(press_x, press_y)
        time.sleep(.8)
        adb.tap(755, 395)
        time.sleep(.8)
        adb.tap(643, 634)
        os.remove('screenshot.png')
        session.delete(next_player)
        session.commit()
        timer()


async def timer():
    time.sleep(90)