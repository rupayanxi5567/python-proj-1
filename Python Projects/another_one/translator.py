from googletrans import Translator, LANGUAGES 
from googletrans.models import Translated 


lang = list(LANGUAGES.values())
print("Welcome to Translator of Rup")

input_text = input("Enter your text in English: \n")
output_lang = input("Please enter the langage [indonesian, japanese, armenian etc] in which you want to translate: \n").lower()

if output_lang not in lang:
    print("Sorry, this language is not available right now, we will be right back with more languages soon!")
else:
    translator = Translator()
    translated = translator.translate(text = input_text, src = "english", dest = output_lang )
    translated = str(translated).split(",")
    converted = translated[2]
    pronounciation = translated[3]
    print(converted)
    print(pronounciation)