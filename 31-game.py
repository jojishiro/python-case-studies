#31-Game
#PythonLab
import random as R
def createDeck():
    return [i for i in range(1,15)]
       
deck = [ createDeck(),createDeck(),
         createDeck(),createDeck() ]


Exit = False
while not Exit:
    cards = []
    mother = []
    s = 0
    choice = raw_input("Do you want to play? ")
    if choice == 'yes' or choice == 'y':
        firstCard = R.randint(1,14)
        secondCard = R.randint(1,14)
        cards.append(firstCard)
        cards.append(secondCard)

        mCard = R.randint(1,14)
        mSCard = R.randint(1,14)
        mother.append(firstCard)
        mother.append(secondCard)

        ms = sum(mother)
        s = sum(cards)
        print "Current sum: ",s
        while True:
            choice = raw_input("Another card?y/n: ")
            if choice == 'y':
                cards.append(R.randint(1,14))
                s += sum(cards)
                if s > 31:
                    print "You lost with ",s
                    break
                else:
                    print "Your current number: ",sum(cards)
            else:
                print "You hand: ",sum(cards)
                while True:
                    mother.append(R.randint(1,14))
                    ms += sum(mother)
                    if ms == 31 or (ms < 31 and (ms > s and s <= 31)):
                        print "Mother Wins"
                        print "Mother had ",ms
                        break
                    else:
                        print "You Won!"
                        print "Mother had ",ms
                        break
                break
        
    else:
        print "There's the door!"
            
        
        
                          
        
        

    
    

