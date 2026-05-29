import random 
 
def game():
     print("You are playing the game...")
     score = random.randint(1, 62)
      # Fetch the hiscore 
     with open("hiscore.txt") as f:
         hiscore = f.read()
         if(hiscore != ""):
             hiscore = int(hiscore)
         else:
             hiscore = 0

     print(f"Your score :{score}")
     if(score>hiscore):
    


         # write the hiscore to the file

      return score 
     
game()