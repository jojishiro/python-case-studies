import random

class camelot:
    def __init__(self, knight, combat):
        self.name = knight
        self.skills = combat

    def trials(self):
        if self.skills >= 6:
            return True
        else:
            return False
        
while True:

    shield = {}
    gold = random.randint(500,1000)
    quests = ["Training","Training Quest"]
    totalQuests = random.randint(80,160)
    name = raw_input("Name of the knight: ")
    if name == 'q' or name == 'Q':
        break
    
    techniques = input("Number of knight's fighting techniques(e.g 4): ") 
    knight = camelot(name, techniques)   

    if knight.name == 'Lancelot' or knight.name == 'lancelot':
        for quest in range(totalQuests):
            quests.append("Quest #"+str(quest))
        print "Welcome Sire, you've completed "+str(len(quests))+" quests already."

    elif knight.name != 'lancelot' or knight.name != 'Lancelot':
        flag = knight.trials()
        if flag == True:
            pay = ('Gold',gold)
            shield[knight.name] = "Approved" + " | Pay: " + str(pay)
        else:
            shield[knight.name] = "Rejected"

        print "Request status: " + str(shield.get(knight.name)) 

