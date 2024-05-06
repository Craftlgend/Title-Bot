from database import first_player_title, check_database_has_entries


async def main_algorythm():
    while check_database_has_entries() == True:
        title_requested = first_player_title()
        print (title_requested)
        if title_requested == "duke":
            print ("duke was requested")
        elif title_requested == "architect":
            print ("architect was requested")
        elif title_requested == "justice":
            print ("justice was requested")
        elif title_requested == "scientist":
            print ()
        else:
            print("Error")