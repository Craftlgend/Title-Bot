import time
#import adb
import cv2
from database import Player, session



duke = ('duke')


x = 75
y = 896

next_player = session.query(Player).filter_by(title = duke).first()
print (next_player)

#adb.tap(x, y)
#duke_active
time.sleep(10)
duke_active = 0

    







def add():
    #add to the list of players
    pass

