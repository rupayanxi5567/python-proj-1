print("Welcome to Rup's Advanced Quiz Game")

playing = input("Do you want to play the game? (yes/no) ")

if playing.lower() != "yes":
    quit()
print("Okay let's play :)")
score = 0
print("Your score is ", score)

# game starts

print("Question-1")
answer = input("Who is the Guru of Karna? ")
if answer == "Dronacharya".lower() :
    print("You answer is correct. Explaination:- Yes, Karna is also student of Dronacharya. “The Vrishnis and the Andhakas, and princes from various lands, and the (adopted) son of Radha of the Suta caste, (Karna), all became pupils of Drona.")
    score += 1
    print("Your score is ", score )
else:
    print("You answer is incorrect. Explaination:- Karna is also student of Dronacharya. “The Vrishnis and the Andhakas, and princes from various lands, and the (adopted) son of Radha of the Suta caste, (Karna), all became pupils of Drona.")
    print("Score added 0 and your score is ",score )

print("Question-2")
answer = input("Who is the Guru of Dronacharya? ")
if answer == "Parashurama".lower() :
    print("You answer is correct. Explaination:- Parashurama imparted knowledge of celestial weapons to Drona along with the mantra of invocation and withdrawal of weapons. He had a huge range of weapons like Brahmastra, Brahmashira, Narayanastra, Rudra, Agneya, Vajra etc.")
    score += 1
    print("Your score is ", score )
else:
    print("You answer is incorrect. Explaination:- Parashurama imparted knowledge of celestial weapons to Drona along with the mantra of invocation and withdrawal of weapons. He had a huge range of weapons like Brahmastra, Brahmashira, Narayanastra, Rudra, Agneya, Vajra etc.")    
    
    print("Score added 0 and your score is ",score )

print("You scored ", (score/2)*100,"% in this game"  )