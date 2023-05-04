#i changed you movement system so that each room had its own block of code.
#this allows you to easily control where the player can move and do other event like picking up items or attacking
#the code I made is:
#  if "room" + str(room_number) == "room0": 
#     if player_input == "north":
#        room_number = 0
#        print(Room0)
#
#     if player_input == "west":
#        room_number = 0
#        print(Room0)
#
#     if player_input == "east":
#        room_number = 0
#        print(Room0)
#
#     if player_input == "south":
#        room_number = 0
#        print(Room0)
#
#     if player_input == "pickup":
#        print("you cannot pick anything up here.")
#
#     if player_input == "attack":
#        print("you cannot attack here")
#
#
#I added some new variable (mostly for event like picking things up or talking to people) and one of the is the room_number.
#The room_number variable is an interger that controls what room you are in.
#it tests what room you are in by concatonating the string "room" and the room_number as a string to see if it matches a room in the code
#
#In the if statement, it tests for 1 of 6 inputs: north, south, east, west, pickup, or attack
#If any one of those are selected it will run the code in that inputs if statement.
#for the movement, it usually changes the room number to the room number of the room your going into then print the text for that room and move on.
#Sometimes, though, there is an event. When that happened I made a variable to test if the event has happened or not.
#this just adds another if statement in the input if statement section to test if the event has happened; if it hasn't it runs it, if it has it doesn't run it.
#For some of these events you will need to add code to pick things up and add them to the inventory of the player.
#Other ones, like fighting, you will also have to implement
#
#The pickup and fight inputs usually give the same response of not being able to do it.
#change what you want them to do by just replacing the default print command I put.
#
#I also left several comments throughout the code that show where you need add certain thing
#
#lastly, I made you loop a while True: loop that runs forever, to exit the game at anytime input "break" and the game will end.
#
#Text me if you have any other questions

def main():
#BEFORE GAME START
    player_name = input("Enter your character's name: \n")
    inventory = ["", ""]
    player_position = ""
    item1 = "Samurai_katana"
    item1_collected = False
    Room5_zombiesgone = False

    controls = ("CONTROLS:\n\nWEST\nEAST\nNORTH\nSOUTH\nPICKUP\nATTACK\n")

    Room1 = ("You look around from the car you took to the mall, there are 4 ways you can go. Hallways to your north, west, and east. And south is the exit.")
    Room2 = ("As you enter the room you see it used to be a cafe of some kind, you try one of the machines but it doesn't work. Dang. You decide to get back to your job and see a hallway to the west")
    Room3 = ("You walk into a crossroads, the south is taken out so no going that way. The west leads to an apple store which you're guessing is abandoned, and north leads you to an abandoned office.")
    Room4 = ("As you enter the apple store you see it has already been looted, the technology wouldn't have been any help since it would have been dead. To your west you see an opening to a pretty large room.")
    Room5z = ("As you enter the doorway to your west you see a horde of zombies, you know a few bullets will make them scatter and allow you to move on, but for now you can't go west until you get those bullets")
    Room5noz = ("You enter the doorway into a large area where you had scattered zombies earlier.")
    Room6 = ("With the zombies scattered you continue through the large area but see nothing of interest other than a door to your north.")
    Room7_weaponnotcollected = ("As you enter the room you don't see anything, but out of the corner of your eye you see a baseball bat in a barrel")
    Room7 = ("When you enter the room you see nothing of value.")
    Room8_weaponnotcollected = ("You decide to go north into the office building, and you manage to find a samurai katana. The only way you can go from here is north out the back door, our south through the way you just came.")
    Room8 = ("You decide to go north into the office building. The only way you can go from here is north out the back door, our south through the way you just came.")
    Room9z = ("As you leave through the backdoor, you see a disturbing sight. There is a horde of zombies just ahead of you, but you can scatter them with a couple of bullets.")
    Room9noz = ("You enter a deserted hallway you scattered zombies in.")
    Room10 = ("As you go east from your car, you see a long, uninteresting hallway that looks like it goes on for a while.")
    Room11 = ("The long, boring hallway continues on")
    Room12z = ("As you are walking down the long, boring hallway you eventually come upon a small horde of zombies, you can kill them all with some bullets.")
    Room12noz = ("The long, boring hallway continues on")
    Room13 = ("Now that there aren't any zombies here, you see the boring hallway finally comes to an end in a room just east from where you are, which opens into a hunting store.")
    Room14 = ("You don't see any bullets in the hunting store, but you see a key which looks like it could open a locked door.")
    Room15 = ("As you enter the room from the hallway, you see trash scattered around the area, and traces of zombies. You don't see any zombies near you but it is clear they were here at one point. The building continues north")
    Room16 = ("As you trudge through the long building, you finally come across a door. When you open it you see it opens into something into some other area to your north")
    Room17 = ("When you open the door, you come upon a massive area, with beautiful statues now covered in moss, you guess this is the center of the mall. There are paths in all directions.")
    Room18 = ("This hallway looks like it once was a beautiful piece of architecture, but now there is greenery covering all of it. It makes it beautiful in a weird way. The hallway continues west or east")
    Room19 = ("Since the zombies are scattered, this area is trashed with junk thrown everywhere. This room looks like it could have been a food court in the past. There are hallways south, west, and east.")
    Room20 = ("As you continue going west, you can hear some noises coming from a building just west from where you are.")
    Room21_isaacnotsaved = (f"As you enter the store, you see your friend Isaac, '{player_name}! I thought you weren't gonna find me, you must've dealt with the zombies since you made it here. I am gonna go to the car and place my supplies there, see you there!' With Isaac leaving, you see nothing else in this room.")
    Room21_isaacsaved = ("As you enter the room, you see some stray rats scrambling around, how did these rats cause all this ruckus?")
    Room22_weaponnotcollected = ("You decide to go east, and as you are walking across the hallway, you see a shotgun to the right. The hallway continues on East")
    Room22 = ("You decide to go east as the hallway continues")
    Room23 = ("You enter a weird art store, there aren't any paintings that catch your attention, the art room continues east")
    Room24_normal = ("You continue going down the art store until you come to a dead end, with a picture of a man smiling at you, he looks friendly.")
    Room24_trueending = ("You continue going down the art store until you come to the end, where you see a picture of a man smiling at you, he looks friendly.")
    Room25 = ("You decide to go north and come up to an escalator. Well it used to be, now since there isn't power it is basically just a staircase. It continues north.")
    Room26 = ("As you ascend the stairs, they seemed to go on forever. Once you reach the top, to your north you see a locked door. You see that it needs a key to be opened")
    Room27_nokey = ("You can't continue until you find a way through the locked door")
    Room27 = ("As you open the door you come across a beautiful room, untouched by nature with hallways north, east, and west. The north seems to head to a boys bathroom, and the east is a girls bathroom.")
    Room28_weaponnotcollected = ("As you enter the room, you realise this is a police department for the mall, you see a baton hanging up on the wall")
    Room28_weaponcollected = ("When you enter the room, you realise this is a police department for the mall.")
    Room29 = ("When you enter the girls bathroom, the only thing there remotely close to a girl are the rats running around.")
    Room30_tazznotsaved = (f"As you enter the bathroom, you hear a massive fart and plop. 'Is that you Tazz?' you call out. All the sudden a stall opens and you see Tazz come out of it. '{player_name}! You got me at a bad time but I was stuck here and needed to do my thing yknow. I actually gathered some food for the colony, I will meet you at the car!'")
    Room30_tazzsaved = (f"You enter the boys bathroom and hear a disfunctional toilet constantly flushing, how is that thing still working?")
    Zombies_in_room = ("You can't go this way with zombies right there!")
    Locked_door_room = ("You can't continue until you find a way through this door!")
#GAME START

    print("After some Chinese scientist had a failed experiment, zombies began to appear all throughout the world and cause a meltdown of humanity")
    print("You and some friends managed to make a small colony near NUAMES high-school, but the situation is dire. You are starving and in need of supplies")
    print("You, Tazz, and Isaac were all 'volunteered' to go and get supplies for the colony, you arrived at your destination and while you got to work fixing the car, Isaac and Tazz headed out for supplies")
    print("But then, you got a distress call from Isaac and Tazz, Isaac got cornered by zombies and Tazz locked himself in a room to escape some zombies chasing him, and they both need help, so it is time to save your friends!")
    print(f"{Room1}")
    print("You have no weapons, so you are hoping to find some around the mall.")
    player_position = Room1
    player_input = ""

    room_number = 1
    room9NoZ = False
    room12NoZ = False
    issacSaved = False
    tazzSaved = False
    shotgunPickedUp = False
    keyPickedUp = False
    batonPickedUp = False

    while True:
        player_input = ""
        player_input = input("What do you want to do?\n").lower()
        print("room" + str(room_number))

        if player_input == "break":
              break

        if "room" + str(room_number) == "room1": #Room 1
                if player_input == "north":
                    room_number = 15
                    print(Room15)
                if player_input == "west":
                      room_number = 2
                      print(Room2)
                if player_input == "east":
                      room_number = 10
                      print(Room10)
                if player_input == "south":
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room2": #Room 2
                if player_input == "north":
                    print("you cannot go this way.")
                if player_input == "west":
                      room_number = 3
                      print(Room3)
                if player_input == "east":
                      room_number = 1
                      print(Room1)
                if player_input == "south":
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")
                
        elif "room" + str(room_number) == "room3": #Room 3
                if player_input == "north":
                    room_number = 8
                    if item1_collected:
                        print(Room8)
                    if not(item1_collected):
                          print(Room8_weaponnotcollected)
                if player_input == "west":
                      room_number = 4
                      print(Room4)
                if player_input == "east":
                      room_number = 2
                      print(Room2)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      pass #add code here to pick up the baseball bat
                if player_input == "attack":
                      print("you cannot attack here")
                      
                
        elif "room" + str(room_number) == "room4": #Room 4
                if player_input == "north":
                    #room_number = 8
                    print("You cannot go this way.")
                if player_input == "west":
                      room_number = 5
                      if Room5_zombiesgone == False: #this will push you back to room 4 if the zombies are still there; there is currently no way to kill the zombies. I didn't know how you wanted to do that so I'll let you do it.
                        print(Room5z)
                        room_number = 4
                      elif Room5_zombiesgone == True:
                        print(Room5noz)  
                if player_input == "east":
                      room_number = 3
                      print(Room3)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")
        
        elif "room" + str(room_number) == "room5": #Room 5
                if player_input == "north":
                    #room_number = 8
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 6
                      print(Room4)
                if player_input == "east":
                      room_number = 4
                      print(Room2)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")
                
        elif "room" + str(room_number) == "room6": #Room 6
                if player_input == "north":
                    room_number = 7
                    if item1_collected: #this section has the baseball bat which I assume you should be able to pick up, there is only code for a samuri sword though so i didn't know what do do here
                        print(Room7) #I just put this as an if statement testing to see if item1_collected is true or not, if it is true than it doesn't say anything about the baseball bat, if it is false it does
                    if not(item1_collected): #feel free to fix this if you want/need to.
                        print(Room7_weaponnotcollected)
                if player_input == "west":
                      #room_number = 6
                      print("you cannot go this way.")
                if player_input == "east":
                      room_number = 4
                      print(Room2)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      pass #add you code to pick up the baseball bat here
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room7": #Room 7
                if player_input == "north":
                    #room_number = 0
                    print("You cannot go this way")
                if player_input == "west":
                      #room_number = 0
                      print("you cannot got this way.")
                if player_input == "east":
                      #room_number = 0
                      print("You cannot go this way")
                if player_input == "south":
                    room_number = 6
                    print(Room6)
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")
        
        elif "room" + str(room_number) == "room8": #Room 8
                if player_input == "north":
                    room_number = 9
                    if room9NoZ == False: #from how the text went, i assumed you wouldn't actually have to fight the zombies so I just made it a one time event with the room9NoZ bool. if it is true the event wont happen again
                        print(Room9z)
                        room9Noz = True
                    elif room9NoZ == True:
                          print(Room9noz)
                if player_input == "west":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "east":
                      #room_number = 0
                      print("you cannot go this way.")
                if player_input == "south":
                    room_number = 3
                    print(Room3)
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room9": #Room 9
                if player_input == "north":
                    room_number = 19
                    print(Room19)
                if player_input == "west":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "east":
                      #room_number = 0
                      print("You cannot go this way")
                if player_input == "south":
                    room_number = 8
                    print(Room8)
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room10": #Room 10
                if player_input == "north":
                    #room_number = 8
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 1
                      print(Room1)
                if player_input == "east":
                      room_number = 11
                      print(Room11)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room11": #Room 11
                if player_input == "north":
                    #room_number = 0
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 10
                      print(Room10)
                if player_input == "east":
                      room_number = 12
                      if room12NoZ == False: #I added an event for the zombies being in room 12.
                        print(Room12z)
                      elif room12NoZ == True:
                        print(Room12noz)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack": #You'll need to add code to fight the zombies here - currently you can just go right past them because nothing is stoping you.
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room12": #Room 12
                if player_input == "north":
                    #room_number = 8
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 11
                      print(Room11)
                if player_input == "east":
                      room_number = 13
                      print(Room13)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")
        
        elif "room" + str(room_number) == "room13": #Room 13
                if player_input == "north":
                    #room_number = 0
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 12
                      print(Room12noz)
                if player_input == "east":
                      room_number = 14
                      print(Room14)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room14": #Room 14
                if player_input == "north":
                    #room_number = 0
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 13
                      print(Room13)
                if player_input == "east":
                      #room_number = 0
                      print("you cannot go this way.")
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      keyPickedUp = True #this code allows the player to pick up the key - also make sure to add code to add the weapon to the player inventory
                      print("You picked up the key")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room15": #Room 15
                if player_input == "north":
                    room_number = 16
                    print(Room16)
                if player_input == "west":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "east":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "south":
                    room_number = 1
                    print(Room1)
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room16": #Room 16
                if player_input == "north":
                    room_number = 17
                    print(Room17)
                if player_input == "west":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "east":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "south":
                    room_number = 15
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")
        
        elif "room" + str(room_number) == "room17": #Room 17
                if player_input == "north":
                    room_number = 25
                    print(Room25)
                if player_input == "west":
                      room_number = 18
                      print(Room18)
                if player_input == "east":
                      room_number = 22
                      if shotgunPickedUp == False: #one time event to pick up the shotgun
                        print(Room22_weaponnotcollected)
                      elif shotgunPickedUp == True:
                        print(Room22)
                if player_input == "south":
                    room_number = 16
                    print(Room16)
                if player_input == "pickup":
                      pass #put code here for picking up the shotgun - make sure to set the shotgunPickedUp variable to True.
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room18": #Room 18
                if player_input == "north":
                    #room_number = 8
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 19
                      print(Room19)
                if player_input == "east":
                      room_number = 17
                      print(Room17)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room19": #Room 19 something I noticed about this room is that you have to fight zombies when coming from the south but can go straight through when coming from the east, you can fix this if you want; just an observation.
                if player_input == "north":
                    #room_number = 8
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 20
                      print(Room20)
                if player_input == "east":
                      room_number = 18
                      print(Room18)
                if player_input == "south":
                    room_number = 9
                    print(Room9noz)
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")
        
        elif "room" + str(room_number) == "room20": #Room 20
                if player_input == "north":
                    #room_number = 0
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 21
                      if issacSaved == False: #another single time event using a boolen
                        print(Room21_isaacnotsaved)
                      if issacSaved == True:
                            print(Room21_isaacsaved)
                if player_input == "east":
                      room_number = 4
                      print(Room2)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room21": #Room 21
                if player_input == "north":
                    #room_number = 0
                    print("You cannot go this way")
                if player_input == "west":
                      #room_number = 0
                      print("You cannot go this way")
                if player_input == "east":
                      room_number = 20
                      print(Room20)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room22": #Room 22
                if player_input == "north":
                    #room_number = 8
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 17
                      print(Room17)
                if player_input == "east":
                      room_number = 23
                      print(Room23)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room23": #Room 23
                if player_input == "north":
                    #room_number = 0
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 22
                      print(Room22)
                if player_input == "east":
                      room_number = 24
                      print(Room24_normal) #this says it has a normal room and an ending but they are both the same, im going to assume this isn't finished so I just put the normal room 24
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room24": #Room 24
                if player_input == "north":
                    #room_number = 0
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 23
                      print(Room4)
                if player_input == "east":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room25": #Room 25
                if player_input == "north":
                    room_number = 26
                    print(Room26)
                if player_input == "west":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "east":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "south":
                    room_number = 17
                    print(Room17)
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room26": #Room 26
                if player_input == "north":
                    room_number = 27
                    if keyPickedUp == False: #only lets the player in the locked door if they have the key
                          print(Room27_nokey)
                    elif keyPickedUp == True:
                          print(Room27)
                if player_input == "west":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "east":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "south":
                    room_number = 25
                    print(Room25)
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room27": #Room 27
                if player_input == "north":
                    room_number = 30
                    if tazzSaved == False: #one time event to pick up the baton
                          print(Room30_tazznotsaved)
                    elif tazzSaved == True:      
                          print(Room30_tazzsaved)
                if player_input == "west":
                      room_number = 28
                      if batonPickedUp == False:
                            print(Room28_weaponnotcollected)
                      elif batonPickedUp == True:
                            print(Room28_weaponcollected)
                if player_input == "east":
                      room_number = 4
                      print(Room2)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      pass #add code to pick up baton - make sure to set the batonPickUp Variable to True.
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room28": #Room 28
                if player_input == "north":
                    #room_number = 0
                    print("You cannot go this way")
                if player_input == "west":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "east":
                      room_number = 27
                      print(Room27)
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room29": #Room 29
                if player_input == "north":
                    #room_number = 0
                    print("You cannot go this way")
                if player_input == "west":
                      room_number = 27
                      print(Room27)
                if player_input == "east":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "south":
                    #room_number = 0
                    print("you cannot go this way.")
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

        elif "room" + str(room_number) == "room30": #Room 30
                if player_input == "north":
                    #room_number = 0
                    print("You cannot go this way")
                if player_input == "west":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "east":
                      #room_number = 0
                      print("You cannot go this way.")
                if player_input == "south":
                    room_number = 27
                    print(Room27)
                if player_input == "pickup":
                      print("you cannot pick anything up here.")
                if player_input == "attack":
                      print("you cannot attack here")

if __name__ == "__main__":
        main()

