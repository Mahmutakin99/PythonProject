from googletrans import Translator

# function that translates the entered text using google translate
def translateText(text, targetLang):
  translator = Translator()
  Translation = translator.translate(text, dest = targetLang)
  return Translation.text

while True:
    
    select=int(input("**********************************\n1 to start/continue processing Press 0 to stop/finish.\nProcess selection: "))
    if(select==0):
        select2=str(input("you have chosen to stop the transaction, should the transaction be executed? 'yes' or 'no'\nWhat's your choice: "))
        if(select2=='yes'):
            break
        elif(select2=='no'):
            continue
        else:
            print("you logged in incorrectly please correct")
            continue
    if (select > 1 or select < 0):
        print("Please enter the correct code for selection.")
        continue
    
    # text to translate
    text = input("\ntext to translate: ")

    # target language choice
    targetLang = input("1) Turkish\n2) English\n3) German\n4) Spanish\n5) Japanese\n6) French\n7) Russian\n\nEnter the code for a language in: ")

    if targetLang == '1':
        targetLang = "tr"
    elif targetLang == '2':
        targetLang = "en"
    elif targetLang == '3':
        targetLang = "de"
    elif targetLang == '4':
        targetLang = "es"
    elif targetLang == '5':
        targetLang = "ja"
    elif targetLang == '6':
        targetLang = "fr"
    elif targetLang == '7':
        targetLang = "ru"
    else: # To prevent possible errors
        print("An incorrect selection code please correct.")

    # text translation
    TranslatedText = translateText(text, targetLang)

    # Çevrilen metni ekrana yazdır
    print(f"**********************************\n({text}) when translated into the desired language --> {TranslatedText}")