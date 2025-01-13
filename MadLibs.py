#Matti Wachalski
#MadLibs Game

#Initialize

#Functions
def Mad_Libs_Game():
    print("Welcome to the Mad Libs Game!")
    print("Are you ready to play? Let's go!")
    adjective = input("Please insert an adjective:")
    name = input("What's your name? Remember to make the first letter capital!")
    noun = input("What is something you would consider as treasure. Make sure to keep it one word!")
    city = input("What's your favorite city?")
    adjective2 = input("What's your favorite adjective?")
    pluralnoun = input("Now, give me a noun, but make it plural:")
    animal = input("Next, tell me what your favorite animal is:")
    mythicalcreature = input("What's a mythical creature you want to feature in your story?")
    tool = input("What's a tool you like using?")
    adjective3 = input("Finally, give me another adjective!")
    print("One day, a " + adjective + " adventurer named " + name + " set out on a journey to find the legendary golden " + noun + ". The road was filled with " + pluralnoun + " and strange " + animal + "s. When they arrived to " + city + ", they discovered an ancient " + noun + " that glowed in the dark. All the sudden, a " + adjective2 + " " + mythicalcreature + " appeared and scared them away. However, " + name + " knew the golden " + noun + " had to be rescued. " + name + " took his " + adjective3 + " " + tool + " and got the golden " + noun + ". The treasure has been rescued! exclaimed " + name + ".")

#Main
Mad_Libs_Game()


