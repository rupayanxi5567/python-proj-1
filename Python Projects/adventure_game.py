user_name = input("Type your name: ")
print("Welcome", user_name, "to this amazing adventure game" )

answer = input("Hey, you are now on a dirty road. You can go to left or right, so where do you want to go now?: Left/Right ").lower()

if answer == "left":
    answer = input("You came to a river. You can now swim or walk arond it. Type 'SWIM' to swim or 'WALK' to walk. ").upper()

    if answer == "SWIM":
        print("You tried to swim and in the middle of the river you were eaten by a crocodile🐊 :) ")
    elif answer == "WALK":
        print("You walked for miles and died due to lack of water 💧 :) ")
    else:
        print("Invalid answer, you lose!")




elif answer == "right":
    answer = input("You came to a bridge which is wobblying. Do you want to cross that bridge or head back? Type 'CROSS' to cross the bridge and 'BACK' to go back").upper()
    if answer == "CROSS":
        answer = input("You meet a stranger in the middle of the bridge. He looks like wild and angry. Do you wanna talk to him? Type 'YES' to talk and 'NO' to ignore him. ").upper()
        if answer == "YES":
            print("You talked to him and kudos he gave you the gold and you win!!")
        elif answer == "NO":
            print("You ignore him and he gets offended and killed you with a knife 🔪")
        else:
            print("Invalid answer, you lose!")
    elif answer == "BACK":
        print("You turned back and saw a tiger🐅. You were eaten :) ")
    else:
        print("Invalid answer, you lose!")        

else:
    print("Invalid answer, you lose!")