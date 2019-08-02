#!/usr/bin/python3

from random import randint
import sys,pprint

hw1opts = [('north',['south','east']),
            ('east',['west','north']),
            ('south',['north','west']),
            ('west',['east','south'])]
hw2opts = [('north',['south','west']),
            ('east',['west','south']),
            ('south',['north','east']),
            ('west',['east','north'])]

roomTypes = ['room','hallway1','hallway2']

directions = ['north','south','east','west']
knownRooms = []
rooms = {
         'Room1': {'north':'Hallway2','south':'Hallway3','east':'Room3','west':'Room10','status':'no blood','type':'room'},
         'Room2':{'east':'Room5','west':'Hallway2','south':'Room3','north':'Room4','status':'no blood','type':'room'},
         'Room3':{'north':'Room2','south':'Room4','west':'Room1','east':'Hallway5','status':'no blood','type':'room'},
         'Room4':{'north':'Room3','south':'Room2','east':'Hallway6','west':'Hallway4','status':'no blood','type':'room'},
         'Room5':{'north':'Hallway8','south':'Hallway7','east':'Room6','west':'Room2','status':'blood','type':'room'},
         'Room6':{'north':'Hallway11','south':'Room7','east':'Hallway10','west':'Room5','status':'blood','type':'room'},
         'Room7':{'north':'Room6','south':'Hallway9','east':'Room8','west':'Hallway7','status':'monster','type':'room'},
         'Room8':{'north':'Hallway10','south':'Room9','east':'Room10','west':'Room7','status':'blood','type':'room'},
         'Room9':{'north':'Room8','south':'Hallway12','east':'Hallway14','west':'Hallway11','status':'no blood','type':'room'},
         'Room10':{'north':'Hallway13','south':'Hallway14','west':'Room8','east':'Room1','status':'no blood','type':'room'},
         'Hallway1':{'west':'Hallway15','north': 'Hallway4','type':'hallway','status':''},
         'Hallway2':{'east':'Room2','south':'Room1','type':'hallway','status':''},
         'Hallway3':{'north':'Room1','west':'Hallway16','type':'hallway','status':''},
         'Hallway4':{'south':'Hallway1','east':'Room4','type':'hallway','status':''},
         'Hallway5':{'west':'Room3','south':'Hallway6','type':'hallway','status':''},
         'Hallway6':{'north':'Hallway5','west':'Room4','type':'hallway','status':''},
         'Hallway7':{'north':'Room5','east':'Room7','type':'hallway','status':''},
         'Hallway8':{'south':'Room5','east':'Hallway9','type':'hallway','status':''},
         'Hallway9':{'west':'Hallway8','north':'Room7','type':'hallway','status':''},
         'Hallway10':{'west':'Room6','south':'Room8','type':'hallway','status':''},
         'Hallway11':{'south':'Room6','east':'Room9','type':'hallway','status':''},
         'Hallway12':{'north':'Room9','east':'Hallway13','type':'hallway','status':''},
         'Hallway13':{'west':'Hallway12','south':'Room10','type':'hallway','status':''},
         'Hallway14':{'north':'Room10','west':'Room9','type':'hallway','status':''},
         'Hallway15':{'north':'Hallway16','east':'Hallway1','type':'hallway','status':''},
         'Hallway16':{'south':'Hallway15','east':'Hallway3','type':'hallway','status':''}
         }

def createBoard():
    roomsList = [('1','room')]
    numRooms = 1
    for i in range(2,17):
        if roomsList[i-2][1] == 'room':
            n = randint(0,2)
        else: n = 0
        if n == 0: numRooms += 1
        roomsList.append((str(i),roomTypes[n]))
#    return board
    board = {
            '1':{'north':'13','east':'2','south':'5','west':'4','type':'','status':''},
            '2':{'north':'14','east':'3','south':'6','west':'1','type':'','status':''},
            '3':{'north':'15','east':'4','south':'7','west':'2','type':'','status':''},
            '4':{'north':'16','east':'1','south':'8','west':'3','type':'','status':''},
            '5':{'north':'1','east':'6','south':'9','west':'8','type':'','status':''},
            '6':{'north':'2','east':'7','south':'10','west':'5','type':'','status':''},
            '7':{'north':'3','east':'8','south':'11','west':'6','type':'','status':''},
            '8':{'north':'4','east':'5','south':'12','west':'7','type':'','status':''},
            '9':{'north':'5','east':'10','south':'13','west':'12','type':'','status':''},
            '10':{'north':'6','east':'11','south':'14','west':'9','type':'','status':''},
            '11':{'north':'7','east':'12','south':'15','west':'10','type':'','status':''},
            '12':{'north':'8','east':'9','south':'16','west':'11','type':'','status':''},
            '13':{'north':'9','east':'14','south':'1','west':'16','type':'','status':''},
            '14':{'north':'10','east':'15','south':'2','west':'13','type':'','status':''},
            '15':{'north':'11','east':'16','south':'3','west':'14','type':'','status':''},
            '16':{'north':'12','east':'13','south':'4','west':'15','type':'','status':''}
            }

    ## Fill in the dict with room types
    count = 1
    for room in roomsList:
        board[str(count)]['type'] = room[1]
        if board[str(count)]['type'] == 'room':
            board[str(count)]['status'] = 'no blood'
        count += 1
     
    print(roomsList)
    ## get random # if room put status as monster
    while True:
        rnum = randint(1,16)
        if board[str(rnum)]['type'] == 'room':
            board[str(rnum)]['status'] = 'monster'
            break
    #print('>>>>finding blood rooms...')
    print('Monster is in ' + str(rnum))
    
    ## Find rooms to put blood in
    for opt in directions:
        nextRoom = board[str(rnum)][opt]
        #print('first next room is : ' + nextRoom)
        while board[nextRoom]['type'] != 'room':
            if board[nextRoom]['type'] == 'hallway1':
                for hopt in hw1opts:
                    if opt  == hopt[0]:
                        optRoom = board[nextRoom][hopt[1][1]]
                        #print('next room is: ' + optRoom)
                        nextRoom = optRoom
                        opt = hopt[1][1]
                        break
            else:
                for hopt in hw2opts:
                    if opt == hopt[0]:
                        optRoom = board[nextRoom][hopt[1][1]]
                        #print('next room is: ' + optRoom)
                        nextRoom = optRoom
                        opt = hopt[1][1]
                        break
        board[nextRoom]['status'] = 'blood'

#    print(roomsList)
#    pprint.pprint(board)
#    print(numRooms)
    return board

def showInstructions():
    print('''
    RPG Game
    ========
    Commands:

    go [direction]
    shoot [direction]  ## shoot arrow

    ''')

    
def newshowStatus(move):
    print('------------------------')
    knownRooms.append(currentRoom)
    options = {}
    if board[currentRoom]['type'] == 'room':
        print('You are in a room')
        print('You see ' + board[currentRoom]['status'])
        print('You can go \n',end= '')
        for opt in directions:
            print('\t' + opt + ': ',end='')
            if board[currentRoom][opt] in knownRooms:
                optRoom = board[currentRoom][opt]
                print(board[optRoom]['type'] + ' (' + board[optRoom]['status'] + ')')
            else: 
                print('Unknown')
                optRoom = 'unknown'
            options[opt] = optRoom 
    else: #print("Hallway")
        print('You are in a hallway')
        if board[currentRoom]['type'] == 'hallway1': #print('Hallway1')
            print('You can go \n',end='')
            for opt in hw1opts:
                if opt[0]  == move:
                    optRoom = board[currentRoom][move]
                    print('\t' + opt[1][0] + ': ',end='')
                    print(board[optRoom]['type'])
                    print('\t' + opt[1][1] + ': ',end='')
                    print(board[optRoom]['type'])
                    options[opt[1][0]] = board[optRoom][opt[1][0]]
                    options[opt[1][1]] = board[optRoom][opt[1][1]]
        else: #print("Hallway2")
            print('You can go \n',end='')
            for opt in hw2opts:
                if opt[0]  == move:
                    optRoom = board[currentRoom][move]
                    print('\t' + opt[1][0] + ': ',end='')
                    print(board[optRoom]['type'])
                    print('\t' + opt[1][1] + ': ',end='')
                    print(board[optRoom]['type'])
                    options[opt[1][0]] = board[optRoom][opt[1][0]]
                    options[opt[1][1]] = board[optRoom][opt[1][1]]
    return options

board = createBoard()
currentRoom = '1'
#while int(currentRoom) < 6:
#    newshowStatus()
#    currentRoom = str(int(currentRoom) + 1)
#sys.exit()

#currentRoom = 'Room1'

showInstructions()

move = ['go','north']
while True:
    options = newshowStatus(move[1])
    move = ''
    while move == '':
       move = input('>')
    move = move.lower().split(' ')

    ## if command is 'go' 
    if move[0] == 'go':
        if move[1] in options.keys():
            currentRoom = board[currentRoom][move[1]]
            if board[currentRoom]['status'] == 'monster':
                print('\nThe wumpus got you! GAME OVER!\n')
                break
        else: 
            print('You can\'t go that way!')

        ## if command is 'shoot'
    if move[0] == 'shoot':
        if move[1] not in options.keys():
            print('\nThe wumpus got you!  GAME OVER!\n')
        else:
            nextRoom = board[currentRoom][move[1]]
            if board[nextRoom]['status'] == 'monster':
                print('\nCongratulations! You killed the wumpus! YOU WIN!\n')
            else:
                print('\nThe wumpus got you!  GAME OVER!\n')
        break

