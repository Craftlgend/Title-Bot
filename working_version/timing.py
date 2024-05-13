import time
import Duke
import Scientist
import Justice
import Architect
from database import check_database_has_entries
from database import first_player_title
from running_script import check_script_running

i = 0


while i < 6:
    players = check_database_has_entries()
    print (players)
    if players == True:
        if first_player_title() == 'Duke':
              Duke.run()
              print("Duke is now running")

        elif first_player_title() == 'Scientist':
              Scientist.run()
              print("Scientist is now running")

        elif first_player_title() ==  'Justice':
               Justice.run()
               print("Justice is now running")

        else:
               Architect.run()
               print("Architect is now running")
    else:
          print ('repeating....')
          print(players)
          time.sleep(10)


