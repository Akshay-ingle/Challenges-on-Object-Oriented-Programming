class flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning= meaning
    def __str__(self):

        return self.word+'( '+self.meaning+' )'
flash=[]
print('welcome to flash application')
while(True):
    word=input('enter the name you want to add to  flashcrad : ')
    meaning= input('énter the meaning of the word:')

    flash.append(flashcard(word,meaning))
    option = int(input('enter 0,if you want to add another flashcard otherwise enter one :'))

    if(option):
        break 
    print('\nYour flashcards')
    for i in flash:
        print('>',i)       