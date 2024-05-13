import time
import duke
import scientist
import justice
import architect
from database import check_database_has_entries
from database import first_player_title
from running_script import check_script_running

i = 0


while i < 6:
    players = check_database_has_entries()
    print (players)
    if players == True:
        if first_player_title() == 'Duke':
              duke.run()
              print("Duke is now running")

        elif first_player_title() == 'Scientist':
              scientist.run()
              print("Scientist is now running")

        elif first_player_title() ==  'Justice':
               justice.run()
               print("Justice is now running")

        else:
               architect.run()
               print("Architect is now running")
    else:
          print ('repeating....')
          print(players)
          time.sleep(10)


