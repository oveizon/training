import random
c = 'CPU wins'
p = 'Player wins'
win = 0
while True:
    player = input('Rock Paper Scissors. To play the game type in R for rock, or S for scissors, or P for paper: ')
    Player = player.upper()
    options = ['R', 'S', 'P']
    CPU = random.choice(options)

    if Player not in options:
        print('error')
        continue
    

    elif CPU == Player :
        if Player == 'R':
             print('you both choose rock')
        elif Player == 'S':
            print('you both choose scissors')
        elif Player == 'P':
            print('you both choose paper')
        print("it's a tie")
        continue

    elif Player == 'R':
        if Player == 'S':
          print(' player(rock) : cpu(scissors)')
          print(p)
        else:
            print('player(rock) : cpu(paper)')
            print(c)

    elif Player == 'S':
        if CPU == 'P':
            print('player(scissors) : cpu(paper)')
            print(p)
        else:
            print('player(scissors) : cpu(rock)')
            print(c)

    elif Player == 'P':
        if CPU == 'R':
            print('player(paper) : cpu(rock)')
            print(p)
        else:
            print('player(paper) : cpu(scissors)')
            print(c)

    if win == c or p :
        break



    
