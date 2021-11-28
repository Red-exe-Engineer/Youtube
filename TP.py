from mcpi.minecraft import Minecraft
from os import system

mc = Minecraft.create()

while True:
    system('clear')

    players = mc.getPlayerEntityIds()
    tp = input('{} player(s) are online: '.format(len(players)-1))

    if tp == 'exit':
        system('clear')
        break

    elif tp == 'tp':
        cords = input('TP to X, Y, Z: ')
        try:
            mc.player.setPos(cords)
        except:
            input('ERR: Could not TP you to "{}"'.format(cords))

    elif tp == 'help':
        system('clear')
        print('HELP:\n "exit" [quits the program]\n "tp" [TP to X, Y, Z]\n "help" [shows this]')
        input('Enter a number to TP to that player')

    else:
        try:
            mc.player.setPos(mc.entity.getPos(players[int(tp)]))
        except:
            input('ERR: Could not TP you to player "{}" or command not found\n     (type "help" for more info)'.format(tp))