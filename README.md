# Title-Bot for Rise of Kingdoms

Let's players request one of the 4 ingame titles in discord.

# Program explanation:

- Player requests title via command in discord.
- Player information is saved in the waitlist for the requested title
- once the player is first in the waitlist the program interacts with the emulator via adb(android-debug-bridge)
- program gives the player the requested title ingame with adb
- player has the title for 90 seconds
- next player in waitlist gets title

# File information:

- adb.py : allows the connection and the control of the emulator
- algorythm.py : runs through the waitlists to give the title once someone is in the waitlist and no one else has the title
- database.py : database creation and control
- discord_connect.py : takes care of all discord commands and connections
- general_script.py : gives the player the title
- other_functions.py : other needed functions and picture recognition functions
- webhook.py : other way to connect to discord
