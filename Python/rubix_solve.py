# INTRO: program to solve a rubix cube since I'm so out of practice
# INTRO: not the optimal program because I don't know the best way to solve a rubix cube

## EXP: functions to make rand rubix cube


# EXP: define a  rubix cube
# NOTE: change later to allow user to define cube
class Rubix:
    # EXP: define a solved cube
  	def __init__(self, bottom, front, left, back, right, top):
      self.bottom = [0,0,0,0,0,0,0,0,0]
      self.front = [1,1,1,1,1,1,1,1,1]
      self.left = [2,2,2,2,2,2,2,2,2]
      self.back = [3,3,3,3,3,3,3,3,3]
      self.right = [4,4,4,4,4,4,4,4,4]
      self.top = [5,5,5,5,5,5,5,5,5]

     # EXP: allow user to make move by inputting face and direction
     def clockMove(face):
         endState = [face[6], face[3], face[0], face[7], face[4], face[1], curstate[8], face[5], face[2]]
         return(endState)

    def counterMove(face):
        return = NULL
         
     def move(self,face,dir):



      #NOTE: dammit i forgot some configurations just don't exist


# function for each stage
