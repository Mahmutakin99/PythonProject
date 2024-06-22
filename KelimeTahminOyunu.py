from random import choice

# We create a bool value to terminate the outermost loop if the user wants to exit the application.
Accuracy = False

while True:
  if Accuracy == True:
    # If the user guessed the word correctly, we ask if they want to quit the game.
      choice = input("You guessed the word correctly, do you want to start a new game (yes or no):\n--> ").lower()
      if choice == 'yes':
          Accuracy = False
          continue
      elif choice == 'no':
          break
      else:
        # we take precautions in case the user enters something wrong.
          print("incorrect entry exiting the program")
          continue
    
  # We create a list of words. you can add the words you want and remove the words you don't want.
  Words=['GalataSaray', 'Book', 'Wind', 'Pen', 'Flower', 'Computer', 'Sea', 'Cat', 'Tree', 'Star',
 'Music', 'Mountain', 'Clock', 'Coffee', 'Table', 'Chair', 'Phone', 'Picture', 'Hat', 'Apple',
 'Glass', 'Plate', 'Television', 'Bag', 'Shoe', 'Pants', 'Jacket', 'Glasses', 'Lamp',
 'Map', 'Building', 'Bridge', 'Train', 'Car', 'Bicycle', 'Plane', 'Balloon', 'House', 'Street', 'Park',
 'Garden', 'Child', 'Baby', 'Rain', 'Snow', 'Sun', 'Sand', 'Cloud', 'Bird', 'Fish', 'Lake', 'River',
 'Forest', 'Island', 'Lighthouse', 'Route', 'Bus', 'Calendar', 'Notebook', 'Pencil case', 'Eraser', 'Paint', 'Brush',
 'Canvas', 'Kitchen', 'Bathroom', 'Bed', 'Room', 'Living room', 'Corridor', 'Frame', 'Lock', 'Key', 'Fruit',
 'Vegetable', 'Chocolate', 'Ice cream', 'Cake', 'Bread', 'Cheese', 'Olive', 'Tomato', 'Cucumber', 'Pepper',
 'Potato', 'Carrot', 'Onion', 'Garlic', 'Parsley', 'Dill', 'Mint', 'Lemon', 'Orange', 'Tangerine',
 'Watermelon', 'Melon', 'Cherry', 'Strawberry', 'Banana', 'Grape', 'Apple', 'Pear']

  # We select a random word from our list of words using the choice function from the random module, which allows us to choose randomly.
  Word = choice(Words).lower()
  # We create a list of characters consisting of '_' of the length of our randomly chosen word.
  Prediction = []
  for _ in range(len(Word)):
      Prediction.append('_')
      # or
      # Prediction += '_'
  while True:
    print(Prediction)
    # We ask the user to guess the word by taking a letter
    inp1=input("Enter a letter, write a prediction to guess:\n--> ").lower()
    # we ask the user if he/she has a guess, if so, we ask him/her to enter a guess, 
    # if correct, the guess is correct, if incorrect, the guess is incorrect, we tell him/her to enter a guess or letter again
    if inp1 == 'prediction':
      inp2 = input("enter your prediction:\n--> ").lower()
      if inp2 == Word:
        print(f"Congratulations, our word: {Word}")
        Accuracy = True
        break
      else:
        print("Wrong prediction, try again")
        continue
    
    # If the entered letter is in our word, we replace the '_' character with the letter in the appropriate order in the prediction list.
    i = 0
    for letter in Word:
      if letter == inp1:
        Prediction[i] = letter
      i += 1
    
    #we check if there are any '_' characters left in the guess list because the word must be guessed to end the game
    x = 0
    for Character in Prediction:
      if Character == '_':
        x += 1
    if x == 0:
      print(Prediction)
      Accuracy = True
      break