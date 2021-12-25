from dll import DoublyLinkedList
import random
from datetime import datetime


class MyGame(DoublyLinkedList):
    def __init__(self):
        super().__init__()
        self.players = None

    def get_players(self):
        x = []
        n = self.start_node
        while n is not None:
            x.append(n.item)
            n = n.nref
        return x

    def show_players(self, players):
        print("Current players in the game:")
        for p in players:
            print('player'+p.__str__(), end=" ")
        print()

    def add_player(self, data):
        return super().insert_at_end(data)

    def select_it(self, players):
        idx = random.randint(0, len(players)-1)
        it = players[idx]
        x = players[idx:]
        y = players[:idx]
        # y = players[idx+1:]
        players = x + y
        return idx, it, players

    def select_goose(self, idx, it, players):
        tapped = 0
        idx = players.index(it)
        temp = [x for x in players if x != it]
        tapLimit = len(temp) * 2
        while True:
            tapped += 1
            if idx == len(temp):
                idx = 0
            if tapped >= tapLimit:
                print('{0:8}'.format('GOOSE'), end=' ')
                break
            elif random.random() > 0.5 and tapped > 2:
                print('{0:8}'.format('GOOSE'), end=' ')
                break
            else:
                print('{0:8}'.format('DUCK'), end=' ')
            idx += 1

        print()
        t = 0
        idx2 = 0
        while t < tapped:
            if idx2 == len(temp):
                idx2 = 0
            print('{0:8}'.format('player'+temp[idx2].__str__()), end=' ')
            t += 1
            idx2 += 1

        return temp[idx]

    def chase(self, it, goose, players):
        print('RUN!\n')
        r = random.random()
        winner, looser = [goose, it] if r > 0.5 else [it, goose]
        print('Player {0} won and back in the game, player {1} should leave the game\n'.format(
            winner, looser))

        # swap positions
        temp = players[players.index(goose)]
        players[players.index(goose)] = players[players.index(winner)]
        players[players.index(winner)] = temp

        players = [x for x in players if x != looser]
        self.delete_element_by_value(looser)

        # order by winner player
        winner_index = players.index(winner)
        temp = players[winner_index:]
        temp.extend(players[:winner_index])
        players = temp

        return players

    def start(self, players=None):
        if players == None:
            return

        [self.add_player(x) for x in range(1, 11)]
        self.players = players

        players = self.get_players()

        print("The game has initialized with {0} players".format(len(players)))
        print("--------------------------------------------------------------")
        while self.players > 2:
            idx, it, players = self.select_it(players)
            print('\nPlayer {0} was selected as "it"'.format(it))
            goose = self.select_goose(idx, it, players)
            print('\n\nPlayer {0} was selected as "goose"\n\n'.format(goose))
            players = self.chase(it, goose, players)
            self.show_players(players)
            if len(players) == 1:
                break
            print("--------------------------------------------------------------")
        print('-----------------------------------')
        print('Player {0} won the game!'.format(players[0]))
        print('-----------------------------------')


if __name__ == '__main__':
    game = MyGame()
    startTime = datetime.now().timestamp() * 1000
    game.start(players=10)
    stopTime = datetime.now().timestamp() * 1000
    print('The simulator spent {0:0.2f} ms'.format((stopTime-startTime)))
