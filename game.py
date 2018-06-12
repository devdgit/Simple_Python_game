import random

class Game:
          def __init__(self, name, bal):
                  self.name = name
                  self.bal =bal
    
          def win(self):
                 winning = random.randint(1,10)
                 #self.bal += winning
                 print "You Won The Game. Points earned: " + str(winning)

          def lose(self):
                  lossing = random.randint(1,100)
                  self.bal -= lossing
                  print"You Lost The Game. Points lost:" + str(lossing)

user_name = raw_input("What is your name?\n").lower()
myname = Game(user_name, 10000)
if(user_name.isalpha()):
 print "Welcome " + myname.name + "!!!\n"
else:
 print("NAME SHOULD CONTAIN ONLY ALPHABETS!!")
 exit();
print "You are being rewarded with 10k points!!!\n"
print "Let's play the game!!!"
while True: 
         value = random.randint(1,100)
         n = raw_input("Enter a number between 1 to 100:\n")
         if value == n:
          myname.win()
          print "\nNow your balance is ==>" + str(myname.bal)
         else:
          myname.lose()
          print "\nNow your balance is ==>" + str(myname.bal)
