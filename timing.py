import time
import duke
import scientist
import justice
import architect
from database import check_database_has_entries
from running_script import check_script_running

i = 0
players = check_database_has_entries
print (players)
while i < 6:
    
    if players == True:
        if check_script_running('duke') == False:
              duke.run()
              print("Duke is now running")

        elif check_script_running('scientist') == False:
              scientist.run()
              print("Scientist is now running")

        elif check_script_running('justice') ==  False:
               justice.run()
               print("Justice is now running")

        else:
               architect.run()
               print("Architect is now running")
    else:
          print ('repeating....')
          print(players)
          time.sleep(15) #wait


