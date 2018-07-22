def board2list(row=1,col=1):
    l = []
    for x in range(row):
        l.append([y for y in range(col)])
    for x in range(row):
        for y in range(col):
            l[x][y]="."
    return l

def showlistboard(l):
    print("{}:".format(0), end = " |")
    for a in range(len(l[0])):
        print(" " + chr(97+a), end= " |")
    print()
    for x in range(len(l)):    
        print("{}:".format(x+1), end = " |")
        for y in range(len(l[x])):
            print(" " + str(l[x][y]), end = " |")
        print()

def initnewgame(l):
    l[(len(l)//2)-1][(len(l[0])//2)-1] = "X"
    l[(len(l)//2)][(len(l[0])//2)] = "X"
    l[(len(l)//2)-1][(len(l[0])//2)] = "O"
    l[(len(l)//2)][(len(l[0])//2)-1] = "O"
    return l

board = board2list(8,8)
initnewgame(board)
showlistboard(board)