from database import check_database_has_entries, check_if_title_in_database
from os import path, remove
import general_script
from time import sleep
from adb import tap


def main_algorythm():  #started when a title is requested
    open("Running.pid", "x")
    sleep(10)
    tap(60, 650)
    sleep(.8)
    while check_database_has_entries() == True:
        if path.isfile("Duke.pid") == False and check_if_title_in_database("Duke") == True:  #checks if the title is running and if the player is in database
            general_script.run("Duke")
        elif path.isfile("Architect.pid") == False and check_if_title_in_database("Architect") == True:
            general_script.run("Architect")
        elif path.isfile("Justice.pid") == False and check_if_title_in_database("Justice") == True:
            general_script.run("Justice")
        elif path.isfile("Scientist.pid") == False and check_if_title_in_database("Scientist") == True:
            general_script.run("Scientist")
        else:
            print("All titles are running, please wait...")
            sleep(10)
    tap(60, 650)
    remove("Running.pid")