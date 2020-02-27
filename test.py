# Define the world in terms of its size, wumpus location, pit locations, and gold location

xmax = 4; ymax = 4; xmin = 1; ymin = 1;
x = 1; y = 1; # Initial agent state
hasGold = False
hasArrow = True
wumpusAlive = True
wumpusKillFlag = False
bumpFlag = False;

wumpus = (3,1);
pits = [(1,3),(3,3)]
gold = (3,2);
score = 0;

headings = ['North','East','South','West']
headingCoords = [(0,1),(1,0),(0,-1),(-1,0)] # Movement direction

headingIndex = 1;

playing = True;

# Return the percept or take action based on the current location
def percept():
    global wumpusKillFlag, bumpFlag, playing, score
    percepts = []
    # Check if we are in the vicinity of a pit
    # Check to see if we fall into a pit or get eaten by the Wumpus
    breezeFlag = False
    if (x,y) in pits:
        print("You fell into a pit!")
        score = score - 1000
        playing = False
        return
    elif (x,y) == wumpus and wumpusAlive == True:
        print("You got eaten by the Wumpus!")
        score = score - 1000
        playing = False
        return
    for pit in pits:
        if abs(x - pit[0]) + abs(y - pit[1]) == 1 and not breezeFlag:
            percepts.append('a breeze');
            breezeFlag = True
    # Check if we are in the vicinity of the wumpus
    if abs(x - wumpus[0]) + abs(y - wumpus[1]) <= 1: percepts.append('a stench');
    # Check if we are near the gold
    if (x,y) == gold and not hasGold : percepts.append('glittering')
    if wumpusKillFlag:
        percepts.append('a scream')
        wumpusKillFlag = false
    if bumpFlag:
        percepts.append('bump')
        bumpFlag = False
    print("You are in square (%d,%d) and facing %s.  Your Score is %d." % (x,y,headings[headingIndex],score))
    if percepts:
        print("You perceive the following:")
        for p in percepts: print("\t%s" % p)
    else:
        print("You do not perceive anything out of the ordinary.")

if __name__ =="__main__":
    print("############# Wumpus World Game (Minerva Style) #############")
    print("Available Actions are: L = turn left, R = turn right, F = move forward, S = shoot arrow, G = grab, C = climb out.")
    percept() # Initial Percept
    validActions = ('L','R','F','C','G','S')
    while playing:
        # Check if the agent wants to exit the cave
        try:
            action = input("Please select an action (L,R,F,S,G,C)")
        except KeyboardInterrupt:
            delete_last_output()
            delete_last_output()
            continue
        if action not in validActions:
            print("Invalid action!  Please try again.")
            continue
        if action == 'C': # Climb out of the cave
            if x == 1 and y == 1:
                print("You have climbed out of the cave.")
                if hasGold: score = score + 1000;
                playing = False;
            else: print("There is no exit from the cave here!")
        elif action == 'L': # turn left
                headingIndex = (headingIndex - 1) % 4
                print("Turned to face %s" % headings[headingIndex]);
                score = score - 1;
        elif action == 'R': # turn right
                headingIndex = (headingIndex + 1) % 4
                print("Turned to face %s" % headings[headingIndex]);
                score = score - 1;
        elif action == 'F': # move forward if possible
            movementDir = headingCoords[headingIndex];
            newcoord = (movementDir[0]+x,movementDir[1] + y);
            if (1 <= newcoord[0] <= xmax) and (1 <= newcoord[1] <= ymax):
                x,y = newcoord;
                print("You move forward.")
            else:
                bumpFlag = True
                print("You cannot move further %s" % ())
            score = score - 1
        elif action == 'G': # Pick up gold
            if (x,y) == gold: print("You grabbed the gold!")
            hasGold = True
        elif action == 'S': # Shoot the arrow
            if hasArrow:
                # Vector from current position to wumpus
                toWumpus = (wumpus[0] - x,wumpus[1] - y)
                toWumpusMag = sqrt(toWumpus[0]**2 + toWumpus[1]**2)
                toWumpusNorm = (toWumpus[0]/toWumpusMag,toWumpus[1]/toWumpusMag);

                # Check the dot product with the heading (should be 1)
                if toWumpusNorm[0]*headingCoords[headingIndex][0] + toWumpusNorm[1]*headingCoords[headingIndex][1] == 1:
                    wumpusAlive = False
                    wumpusKillFlag = True
                    print("Your arrow hits!");
                else:
                    print("Your arrow misses!")
                hasArrow = false
                score = score - 10
            else:
                print("You have used up your only arrow!");
                score = score - 1
        if playing: percept()
    print("Your final score is %d" % score)
