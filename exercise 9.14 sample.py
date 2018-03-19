from random import randint

class Dice():
    def __init__(self,sides):
        self.side = sides
        self.roll = 0
        self.total = 0
        self.time = []


    def roll_die(self):
        """rolling dice 10 times
        """
        print("\nThe dice has sides: ",self.side)
        
        count=0
        for count in range(10):
            self.roll = randint(1,self.side)
            #print("The dice rolled now is:",self.roll)
            self.time.append(self.roll)
            self.total += self.roll
        print("The dice rolled 10 times gets: ", self.time)
        print("The total is:",self.total)


obj = Dice(6)
obj.roll_die() 

# for 10-sided dice
obj = Dice(10)
obj.roll_die() 

# for 20-sided dice
obj = Dice(20)
obj.roll_die() 

