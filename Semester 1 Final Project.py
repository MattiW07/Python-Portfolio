#Matti Wachalski
#Semester 1 Final Project

#Initialize
map_pieces = 0 #sets the first variable for the story
companions = 0 #sets the second variable for the story

#Functions
def Treasure_Island_Explorer(): #Defines the function for the whole game
     global map_pieces #makes the first varaible global
     global companions #makes the second variable global
     print("Welcome to the Treasure Island Explorer Game. You will have two tries to complete the game!") #introduces the user to the game
     for i in range(2):
        print("Imagine you are sailing towards a mysterious island that has a very valuable treasure. You must collect pieces of a map and find companions to help you find the treasure. Are you ready? Let's go!") #introduces the goal of the game that the user must strive to reach
        answer1 = input("You were told that the island was safe. However, as you sail along the coast of the island, you see pirates scanning the waters. Do you want to sail to them and try to make friends with them. If so, type Pirates. If you want to avoid them and sail to the other side of the island, type Other side")
        if answer1 == "Pirates":
            print("Ok, risky choice. You sail towards the pirates and pull into their dock.")
            answer2 = input("You walk up to the pirates as they stare you down. Do you want to be friendly or try to steal the piece of the map from their camp? If you want to be friendly, write Friendly, and if you want to steal the piece of the map from their camp, write Steal.")
            if answer2 == "Friendly":
                map_pieces = map_pieces + 1
                print("Good choice. You made friends with them and they ended up giving you a piece of the map. You now have " + str(map_pieces) + " piece of the map. You will now move on to find the second piece of the map.")
                answer3 = input("You keep walking and come across a treasure chest. You think you found the treasure itself, but that sounds too good to be true. You look inside and find the second piece of the map. However, it is covered in spiders. If you are fearless enough to get it, write Reach, and if you are scared and decide to bail on the mission, type Bail.")
                if answer3 == "Reach":
                    map_pieces = map_pieces + 1
                    print("Great Job. You were fearless enough to get the second piece. You combine the two pieces of the map and find the treasure. You have successfully completed the mission. You will now sail home with millions of dollars in gold!") #The user completes the game
                elif answer3 == "Bail":
                    print("You end up bailing on the mission and fail the missions. You sail home with half of the map, but nothing else!") #The user fails the game
            elif answer2 == "Steal":
                print("One of the pirates caught you and you will walk the plank. You failed the mission!")

        elif answer1 == "Other side":
            print("Ok, you went with the safer choice")
            answer4 = input("This side of the island doesn't have much. However, you see a man walking carrying an axe and walking along the shore. If you want to approach him, write Approach, and if you want to avoid him, type Avoid.")
            if answer4 == "Approach":
                companions = companions + 1
                print("The man turned out to be friendly and you have now gained a companion. You now have " + str(companions) + " companion.")
                print("The man tells you that he knows where the treasure is. He says that many have come to the island searching for treasure, but none have ever befriended him. You realize you only need one companion to find the treasure. He tells you where it is and you go find it. You have completed the missions. You will now sail home with millions of dollars in gold!") #The user completes the game
            elif answer4 == "Avoid":
                print("You wander into the island by yourself. You are soon surrounded by trees and don't know where you came from. You are now stranded and your dead body is found 20 days later. You failed the mission!") #The user fails the game

#Main
Treasure_Island_Explorer()
