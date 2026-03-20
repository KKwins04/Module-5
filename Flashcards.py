class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word +'('+self.meaning+')'
    
flash = []
print("Welcome to flashcard application")

while True:
    word = input('Please enter the word you want to add to your card: ')
    meaning = input('Please enter the meaning of the word you added to your card: ')

    flash.append(flashcard(word, ' ', meaning))
    option = int(input("Enter 0, if you want to add another flashcard. Otherwise, enter 1: "))

    if(option):
        break

print('\nYour flashcards')
for i in flash:
    print('>', i)