#Matti Wachalski
#Name Generator Project
#10/18/24
print("Welcome to The What's Your Animal Game!")
print("Answer the questions to find out what your animal is.")
ans=(input("Water or Land?"))
if ans=="Water":
        ans=(input("Smart or Stupid?"))
        if ans=="Stupid":
            ans=(input("Big or Small?"))
            if ans=="Big":
                print("You are a Manatee!")
            else:
                print("You are a Jellyfish!")
        if ans=="Smart":
            ans=(input("Big or Small?"))
            if ans=="Big":
                print("You are a Dolphin!")
            else:
                print("You are an Octopus!")
if ans=="Land":
        ans=(input("Smart or Stupid?"))
        if ans=="Smart":
            ans=(input("Big or Small?"))
            if ans=="Big":
                print("You are an Elephant!")
            else:
                print("You are a Squirrel!")
        if ans=="Stupid":
            ans=(input("Big or Small?"))
            if ans=="Big":
                print("You are an Ostrich!")
            else:
                print("You are a Sloth!")





