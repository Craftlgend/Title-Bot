from other_functions import lk, press_title, picture_recognition, timer
from time import sleep
from adb import tap, screenshot, input
from cv2 import imread
from database import Player, session
from os import remove

template = imread('template.png')



def run(requested_title):
    next_player = session.query(Player).filter_by(title = requested_title).order_by(Player.id).first()
    if next_player == None:
        exit
    else:
        discord_name = next_player.discord_name
        x_coord = next_player.x_coord
        y_coord = next_player.y_coord
        kingdom_type = next_player.kingdom_type

        tap(400, 20)  #open the search menu
        sleep(.8)
        lk(kingdom_type)  #choose the right kingdom
        sleep(.8)
        tap(640, 140)  #input x-coordinate
        sleep(.8)
        input(str(x_coord))
        tap(790, 140)  #input y-coordinate
        sleep(.3)
        tap(790, 140)
        sleep(.8)
        input(str(y_coord))
        sleep(.3)
        tap(885, 140) #start search
        tap(885, 140)
        sleep(1)  #wait for map to load
        tap(640, 360)  #select city
        sleep(.8)
        screenshot()  #make screenshot
        sleep(1)
        coords = picture_recognition(template, 'screenshot.png')  #recognize the title-icon
        press_x =(coords[0]+20)
        press_y = (coords[1]+20)
        tap(press_x, press_y)  #press on title-icon
        sleep(.8)
        press_title(next_player.title)   #press on correct title
        sleep(.8)
        tap(643, 634)    #submit the requested title
        remove('screenshot.png')   #delete the screenshop
        session.delete(next_player)  #delete player from waitlist
        session.commit()  #submit to database
        timer(requested_title)