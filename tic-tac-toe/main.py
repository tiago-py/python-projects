import os



turn = 1 # 1 - Player 1 | 2 - Player 2
clean = os.system("cls")
p_char = 'X'
c_char = 'O'
table = ['1','2','3',
         '4','5','6',
         '7','8','9']

def winner():
    global table
    for i in ['X','O']:
        # horizontal
        if table[0] == table[1] == table[2] == i: return i
        if table[3] == table[4] == table[5] == i: return i
        if table[6] == table[7] == table[8] == i: return i
        # vertical
        if table[0] == table[3] == table[6] == i: return i
        if table[1] == table[4] == table[7] == i: return i
        if table[2] == table[5] == table[8] == i: return i
        # diagonal
        if table[0] == table[4] == table[8] == i: return i
        if table[6] == table[4] == table[2] == i: return i
    return None

def view():
    global table
    
    print (" %s | %s | %s " % (table[0],table[1],table[2]))
    print( "---+---+---")
    print( " %s | %s | %s " % (table[3],table[4],table[5]))
    print( "---+---+---")
    print (" %s | %s | %s " % (table[6],table[7],table[8]))

def move(pos):
    global turn
    global table
    
    if not pos: return None
    if not 0 < pos < 10: return False
    if table[pos-1] in ['X','O']: return False

    table[pos-1] = ('O','X')[turn == 1]
    turn = (1,2)[turn == 1]

while True:
    os.system("cls")
    view()

    print ("Player %s: " % turn,)
    movement = int(input())
    move(movement)

    win = winner()
    if not win: continue
    if win == p_char:
        print ("Player 1 Wins!")
        input()
        exit()
    if win == c_char:
        print ("Player 2 Wins!")
        input()
        exit()