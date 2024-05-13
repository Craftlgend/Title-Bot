from database import check_database_has_entries, check_if_title_in_database
from os import path
import general_script
from time import sleep


async def main_algorythm():  #started when a title is requested
    while check_database_has_entries() == True:
        if path.isfile("duke.pid") == False and check_if_title_in_database("Duke") == True:  #checks if the title is running and if the player is in database
            general_script.run("Duke")
        elif path.isfile("architect.pid") == False and check_if_title_in_database("Architect") == True:
            general_script.run("Architect")
        elif path.isfile("justice.pid") == False and check_if_title_in_database("Justice") == True:
            general_script.run("Justice")
        elif path.isfile("scientist.pid") == False and check_if_title_in_database("Scientist") == True:
            general_script.run("Scientist")
        else:
            print("All titles are running, please wait...")
            sleep(10)