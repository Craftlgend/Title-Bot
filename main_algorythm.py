from database import first_player_title, check_database_has_entries


async def main_algorythm():
    while check_database_has_entries() == True:
        title_requested = first_player_title()
        print (title_requested)
        title_requested.run()