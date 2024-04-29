import time
import justice
import duke
import scientist
import justice
import architect
from database import check_database_has_entries
from running_script import check_script_running

i = 0

async def start():
    while i < 6:
       if check_database_has_entries == True:
           if check_script_running('duke') == False:
              duke.run()

           elif check_script_running('scientist') == False:
              scientist.run()

           elif check_script_running('justice') ==  False:
               justice.run()

           else:
               architect.run()
           
       else:
            return

